# Importing the Flask Module
from flask import Flask

# Creating an Object out of the Flask class
app = Flask(__name__)

# Using decorator for creating the path of my application (homepath)
@app.route('/')
def home():    # Creating the home page
    return "Hello! This is the flask application running!!! This is PW Class!!"

# Calling the main function
if __name__ == "__main__":
    app.run(debug=True)
