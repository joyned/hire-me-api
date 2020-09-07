from app.repository.user import UserRepository


def get_users_profiles():
    users_profiles = []
    for row in UserRepository.get_users_profiles():
        user_profile = {
            'id': row[0],
            'constante': row[1]
        }
        users_profiles.append(user_profile)
    return users_profiles
