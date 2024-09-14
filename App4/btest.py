from bottle import route, run, template, redirect

@route('/')
def home():
    return template('''
        <h1>Home Page</h1>
        <p>Welcome to the home page!</p>
        <form action="/about" method="get">
            <input type="submit" value="Go to About Page">
        </form>
    ''')

@route('/about')
def about():
    return template('''
        <h1>About Page</h1>
        <p>This is the about page.</p>
        <form action="/" method="get">
            <input type="submit" value="Go to Home Page">
        </form>
    ''')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)