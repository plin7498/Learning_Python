from bottle import route, run, get, post, request




@get('/login')
def login_form():
    return '''  <form method = "POST">
                <input name="name" type="text" />
                <input name="password" type="password" />
                <input type="submit" value="Login" />
                </form>
                <input name = "show" type = "text" value = "h"> haha </text>
                '''

@post('/login')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    if password == 'ha':
        return 'right'
    else:
        return 'wrong'

run(host='localhost', port=8080)
