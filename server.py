from dojo_flask_app import app
from dojo_flask_app.controllers import users,posts

if __name__ == "__main__":
    app.run(debug=True, port=5001)