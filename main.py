import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Ciphers</title>
</head>
<body>
    <h1>
        <a href="/">Ciphers</a>
    </h1>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
