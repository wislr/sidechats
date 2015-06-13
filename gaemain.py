import webapp2 as the_webapp
import json, filelinks, random
from google.appengine.ext.webapp.util import run_wsgi_app


class MainHandler(the_webapp.RequestHandler):
    def get(self, branch):
        version = str(self.request.get("version"))
        if version:
            url = "itms-services:///?action=download-manifest&url=https://s3-us-west-1.amazonaws.com/polymath-beta/Sidechat_%s_%s.plist"
            self.redirect(url % (branch, version))
        else:
            url = "itms-services:///?action=download-manifest&url=https://s3-us-west-1.amazonaws.com/polymath-beta/Sidechat_%s.plist"
            self.redirect(url % branch)


class CodingTestHandler(the_webapp.RequestHandler):
    def get(self):
        sample_files = random.sample(filelinks.challenge_files, random.randrange(40, 60))
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(sample_files))


handlers = [('/builds/(.*)/', MainHandler),
            ('/builds/(.*)', MainHandler),
            ('/codingtest/files/', CodingTestHandler)]
application = the_webapp.WSGIApplication(handlers, debug=True)


if __name__ == "__main__":
    run_wsgi_app(application)

