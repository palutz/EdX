import bottle
import pymongo


# this is the handler for the root address of the web server
@bottle.route('/')
def index():
    from pymongo import Connection

    conn = Connection('localhost', 27017)
    db = conn.patati
    # db = conn.test
    # names = db.names
    names = db.nomi
    item = names.find_one()

    return '<b> Hello %s!<b>' %item['name']


bottle.run(host='localhost', port=8082)
