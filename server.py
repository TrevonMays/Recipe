from flask_app import app, render_template
from flask_app.controllers import users, recipes
from flask_bcrypt import Bcrypt


if __name__ == '__main__':
    app.run(debug=True)

