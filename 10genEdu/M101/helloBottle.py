from bottle import route, run, template

@route('/hello')
@route('/hello/<name>')
def hello(name='World!'):
    return template('<b1>Hello, {{name}}</b1>', name=name)

run(host='localhost', port=8080, debug=True)
