from csdata import gd

from client.Session import Session

gd.session = Session.session("username")

print(gd.session['username'])