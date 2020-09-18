from flask import Flask, jsonify, request, send_from_directory, url_for, redirect, make_response
import jwt
import os

SECRET = os.getenv("SECRET")

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return """
        <h2>Request access</h2>
        <form method=POST>
            <input name=filename placeholder=filename>
            <input type=submit>
        </form>
        <a href="flag.txt">flag.txt</a>
        <a href="meme.jpg">meme.jpg</a>
        <a href="hints.txt">hints.txt</a>
        """

    filename = request.form['filename']
    if filename == 'flag.txt':
        return "sorry, can't give you access to that"

    msg = f"<p>you now have access to view {request.form['filename']}<p>"
    msg += "<a href=/>home</a>"
    resp = make_response(msg)

    token = jwt.encode({'filename': filename}, SECRET, algorithm='HS256')
    resp.set_cookie('jwt', token)
    return resp

@app.route('/<filename>')
def get_file(filename):
    try:
        token = request.cookies.get('jwt').encode('utf-8')
        json = jwt.decode(token, SECRET, algorithms=['HS256'])
    except NameError:
        return "invalid token"

    if json['filename'] == filename:
        return redirect(url_for('static', filename=filename))
    else:
        return "401 unauthorized"

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
