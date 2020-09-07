import app.security.TokenValidator as TokenUtil


class HireMeContext:
    def __init__(self):
        self.user_id = 0
        self.person_id = 0
        self.person_name = ''
        self.user_profile_id = 0

    def build(self, request):
        token_decoded = TokenUtil.token_decode(request)
        self.user_id = token_decoded['user_id']
        self.person_id = token_decoded['person_id']
        self.person_name = token_decoded['person_name']
        self.user_profile_id = token_decoded['user_profile_id']
