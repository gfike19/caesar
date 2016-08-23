import webapp2
import cgi
from caesar import *
from helpers import *

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Ciphers</title>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    #get paramters
    def get(self):
        input_form = """
        <p>Enter the message you want to encrypt and how
        you wish to encrypt it.</p>
        <form action = "/input" method = "post">
            <label>
                Message:
                <input type = "text" name = "message"/>
            </label>
            <label>
                Rotation Amount:
                <input type = "number" name = "rot"/>
            <label>
        </form>
        <input type = "submit" value = "Caesar"/>
        <input type = "submit" value = "Rot 13"/>
        """

        response = page_header + input_form + page_footer
        self.response.write(response)

class caesarFunc(webapp2.RequestHandler):

    def post(self):
        mess = str(self.request.get("message"))
        rot = int(self.request.get("rot"))
        new_mess = encrypt(mess,rot)

        output = """
        The old message was: """ + mess + """ and the new message is: """ + new_mess

        response = page_header + output + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/caesar', caesarFunc)
], debug=True)
