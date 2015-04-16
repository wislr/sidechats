import webapp2 as the_webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainHandler(the_webapp.RequestHandler):
    def get(self, branch):
        url = "itms-services:///?action=download-manifest&url=https://s3-us-west-1.amazonaws.com/polymath-beta/Sidechat_%s.plist"
        self.redirect(url % branch)


handlers = [('/builds/(.*)/', MainHandler),
            ('/builds/(.*)', MainHandler)]
application = the_webapp.WSGIApplication(handlers, debug=True)


if __name__ == "__main__":
    run_wsgi_app(application)

