from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)  # Used for session.

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo


if __name__ == '__main__':
    print(__doc__)
    app.run(debug=True)

