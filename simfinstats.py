import os
import pyhdb
from analytics import Analytics
from bottle import get, post, request, response, run, redirect, template, static_file, route  # or route


@get('/login')  # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Hostname: <input name="hostname" type="text" />
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login')  # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    hostname = request.forms.get('hostname')

    connection = pyhdb.connect(
        host=hostname,
        port=30015,
        user=username,
        password=password
    )

    global cursor
    cursor = connection.cursor()
    redirect("/home")


@get('/home')
def do_home():
    return template("home.tpl", name='ranjan')


@get('/plot/rplot/<link>')
def do_rplot(link):
    global cursor
    print(link)
    if link == "link":
        return "<img src='%s'/>" % ("/plot/rplot/er")
    else:
        response.content_type = 'image/jpeg'
        return Analytics(cursor).get_r_plot()


@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root=os.path.join(os.path.dirname(__file__), 'static'))


run(host='localhost', port=8080, debug=True, reloader=True)
