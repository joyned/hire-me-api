class EmailMessage:
    def __init__(self):
        self.to = None
        self.cc = None
        self.cco = None
        self.body = None
        self.from_name = None
        self.from_email = None
        self.subject = None

    def get_body(self):
        email_body = self.build_email_header()
        email_body += self.build_email_body()
        email_body += self.build_email_footer()
        return email_body

    def build_email_header(self):
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {
                        font-family: "Poppins",sans-serif !important;
                    }
                    .email-header {
                        width: 100%;
                        text-align: center;
                    }
                    .logo {
                        width: 20%;
                    }
                    .separator {
                        background-color: #ff656a;
                        margin-top: 0;
                        margin-bottom: 0;
                        border-top: 3px solid rgba(0, 0, 0, 0.1)
                    }
                    .email-body {
                        padding: 3%;
                    }
                </style>
            </head>
            <body>
                <div class="email-header">
                    <img class="logo"
                        src="cid:header-logo"
                        alt="logo">
                    <hr class="separator">
                </div>
        """

    def build_email_body(self):
        return """
            <div class="email-body">
                <div class="email-content" style="text-align: center;">
                    {0}
                </div>
            </div>
        """.format(self.body)

    def build_email_footer(self):
        return """
            <div class="email-footer">
                <hr class="separator">

                <div class="footer-content">
                </div>
            </div>
        </body>

        </html>
        """
