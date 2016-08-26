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
    #the /input needs to go in the tuple at the end
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
                <input type = "number" name = "rotation"/>
            </label>
            <label>
            <p>Rotation Type:</p>
            <label><p>Caesar
                <input type = "radio" name = "rot_type" value = "c"/>
            </label>
            <label> Rot 13
                    <input type = "radio" name = "rot_type" value = "rt"/>
            </label>
            </p>
            <input type = "submit" value = "Encrypt"/>
            </label>
        </form>
        """

        response = page_header + input_form + page_footer
        self.response.write(response)

class rotate(webapp2.RequestHandler):

    def post(self):
        rotType = str(self.request.get("rot_type"))


        if rotType == "c":
            mess = cgi.escape(str(self.request.get("message")), quote = "True")
            rot = int(self.request.get("rotation"))
        if rotType == "rt":
            rot = 13
            mess = cgi.escape(str(self.request.get("message")), quote = "True")
        new_mess = encrypt(mess, rot)

        output = """The old message was: """ + mess + """ and the new message is: """ + new_mess

        response = page_header + output + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/input', rotate)
], debug=True)
