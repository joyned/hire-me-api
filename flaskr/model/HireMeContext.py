import flaskr.security.TokenValidator as TokenUtil


class HireMeContext:
    def __init__(self):
        self.user_id = 0
        self.candidate_id = 0
        self.user_name = ''

    def build(self, request):
        token_decoded = TokenUtil.token_decode(request)
        self.user_id = token_decoded['user_id']
        self.candidate_id = token_decoded['candidate_id']
        self.user_name = token_decoded['user_name']
