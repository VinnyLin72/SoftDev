#Vincent Lin
#SoftDev pd7
#K13 -- Echo Echo Echo
#2018 --09 --27

from flask import Flask, render_template, request #importing necessary functions

app = Flask(__name__)

@app.route('/')
def form(): #creating the form from a template
    return render_template('form.html')

@app.route('/auth')
def auth(): #creating the app's response
    return render_template('auth.html', user = request.args['username'], mthd = request.method)

if __name__ == '__main__':
    app.debug = True #Set False for production
    app.run()
