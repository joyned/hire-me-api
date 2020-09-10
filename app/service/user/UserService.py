from app.model.context import HireMeContext
from app.repository.user import UserRepository

from werkzeug.security import check_password_hash, generate_password_hash


def get_users_profiles():
    users_profiles = []
    for row in UserRepository.get_users_profiles():
        user_profile = {
            'id': row[0],
            'constante': row[1]
        }
        users_profiles.append(user_profile)
    return users_profiles


def change_user_password(request):
    data = request.get_json()
    context = HireMeContext()
    context.build(request)

    current_password = UserRepository.get_current_password_hash(context.user_id)

    current_password_matches = check_password_hash(current_password, data.get('currentPassword'))

    if current_password_matches:
        new_password_hash = generate_password_hash(data.get('newPassword'))
        UserRepository.update_user_password(context.user_id, new_password_hash)
        return "Changed!"
    else:
        raise Exception("Wrong password!")





