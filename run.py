import os
import json
from flask import Flask, render_template, request, flash
# First we are importing a Flask class.
# This is an instance of the Flask class.
app = Flask(__name__)
app.secret_key = 'some_secret'
# The first argument of the Flask class is the name of the package, as we are using a single module, I can use __name__
# Which is a built in Python module.

# In python a decorator starts with an @, this is a way of wrapping funtions
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    data = []
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title='About', company=data)

@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash("Thanks {}, we have received your message.".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title='Contact')

@app.route('/careers')
def careers():
    return render_template("careers.html", page_title='Careers')

# if __name__ == '__main__':
#     app.run(host=os.environ.get('IP'),
#     port = int('8080'),
#     debug=True)


# if __name__ == '__main__':
#     app.run(host = '0.0.0.0',
#     port = int('8080'),
#     debug=True)

# if __name__ == '__main__': # __main__ is the name of the default module in python.
#     app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)

    #
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)