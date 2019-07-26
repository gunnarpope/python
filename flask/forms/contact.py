from flask import Flask, render_template
from wtforms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)
