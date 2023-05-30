# from flask import Flask, render_template, request
from flask import Flask

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# # @app.route("/")
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username == 'admin' and password == 'password':
#             return 'Login Successful!'
#         else:
#             return 'Login Failed!'
#     # asd= render_template('home.html')
#     # print(asd)

#     return render_template('home.html')


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'


@app.route('/')
def test():
    return 'Testing pythonanywhere!'

if __name__ == '__main__':
    print('start program')
    app.run()
