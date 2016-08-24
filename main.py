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
                <input type = "digit" name = "rotation"/>
            </label>
            <label>
            Rotation Type:
            <label> Caesar</label>
            <input type = "radio" name = "rot_type" value = "Caesar"/>
            <label> Rot 13</label>
            <input type = "radio" name = "rot_type" value = "Rot 13"/>
            </label>
        <input type = "submit" value = "Rotate"/>
        </form>
        """

        response = page_header + input_form + page_footer
        self.response.write(response)

class rotate(webapp2.RequestHandler):

    def post(self):
        mess = str(self.request.get("message"))
        rot = int(self.request.get("rotation"))
        new_mess = encrypt(mess,rot)

        rotType = str(self.request.get("rot_type"))

        if not rot:
            rot = 13

        if rotType == "Caesar":
            new_mess = encrypt(mess,rot)
        if rotType == "Rot 13":
            new_mess = encrypt(mess,13)

        output = """The old message was: """ + mess + """ and the new message is: """ + new_mess

        response = page_header + output + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/input', rotate)
], debug=True)
