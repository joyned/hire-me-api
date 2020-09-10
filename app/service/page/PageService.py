
from app.model.context.HireMeContext import HireMeContext
from app.model.page.Pages import Pages
from app.repository.page.PageRepository import *


def get_pages(user_profile_id):
    page_list = []
    res = get_all_pages_by_user_id(user_profile_id)
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
    res = check_permission(context.user_profile_id, data['pageId'])
    if res is None:
        return {"message": 'Permission denied!'}
    else:
        return {"load": True}
