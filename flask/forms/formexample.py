from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

from flask_wtf import Form
from wtforms import validators, ValidationError
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField


class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])

   submit = SubmitField("Send")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
      	return render_template('success.html')
      else if request.method == 'GET':
         return render_template('contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)

