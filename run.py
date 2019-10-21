import os
from flask import Flask, render_template
# First we are importing a Flask class. 
# This is an instance of the Flask class. 
app = Flask(__name__)
# The first argument of the Flask class is the name of the package, as we are using a single module, I can use __name__
# Which is a built in Python module. 

# In python a decorator starts with an @, this is a way of wrapping funtions
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port = int('8080'),
    debug=True)


# if __name__ == '__main__':
#     app.run(host = '0.0.0.0',
#     port = int('8080'),
#     debug=True)

# if __name__ == '__main__': # __main__ is the name of the default module in python. 
#     app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
    
    # 
    #     
    # app.run(host=os.environ.get('IP'),
    #         port=int(os.environ.get('PORT')),
    #         debug=True)    