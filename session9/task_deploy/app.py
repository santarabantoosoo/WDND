from flask import Flask 
# from waitress import serve    fo windows 

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

# waitress-serve --port 8000 app:app   for windows 

if __name__ == "__main__":
    app.run()

    
    
