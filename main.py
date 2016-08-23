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
        you wish to encrypt it. If no rotation specified
        it will default to 13.</p>
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
        <input type = "submit" value = "Rotate"/>
        """

        response = page_header + input_form + page_footer
        self.response.write(response)

class rotate(webapp2.RequestHandler):

    def post(self):
        mess = str(self.request.get("message"))
        rot = int(self.request.get("rot"))
        new_mess = encrypt(mess,rot)

        if rot:
            rot = 13

        if mess:
            error = "Message is empty, please enter a message to encrpt"

        output = 'The old message was: ' + mess '<p>The new message is: ' + new_mess +'</p>'

        if not error:
            response = page_header + error + page_footer
        response = page_header + output +

        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/input', rotate)
], debug=True)
