from flask import Flask

app = Flask("test")

@app.get("/")
def index():
    return "<h1>Test Render</h1>"

if __name__ == "__main__":
    app.run()