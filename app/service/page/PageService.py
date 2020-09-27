from app.model.context.HireMeContext import HireMeContext
from app.model.page.Pages import Pages
from app.repository.page import PageRepository


def get_pages(user_profile_id):
    page_list = []
    res = PageRepository.get_all_pages_by_user_id(user_profile_id)
    for row in res:
        page = Pages()
        page.id = row[0]
        page.constant = row[1]
        page.name = row[2]
        page.icon = row[3]
        page_list.append(page.serialize())
    return page_list


def get_pages_by_request(request):
    context = HireMeContext()
    context.build(request)

    return get_pages(user_profile_id=context.user_profile_id)


def check_permisson(request):
    data = request.get_json()
    context = HireMeContext()
    context.build(request)
    res = PageRepository.check_permission(context.user_profile_id, data['pageId'])
    if res is None:
        return {"message": 'Permission denied!'}
    else:
        return {"load": True}


def register_page(request):
    data = request.get_json()
    context = HireMeContext()
    context.build(request)

    last_page_id = PageRepository.insert_new_page(data)

    if not last_page_id == 0:
        for user_profile_id in data.get('pagePermission'):
            PageRepository.insert_page_permission(last_page_id, user_profile_id)
