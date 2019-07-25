from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/success/<name>/<pin>')
def success(name, pin):
   return 'welcome %s with pin %s' % (name, pin)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['username']
      pin  = request.form['pin']
      return redirect(url_for('success',name = user, pin=pin))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
