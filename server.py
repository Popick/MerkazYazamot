from flask import Flask, request, render_template, Response, stream_with_context, send_file, session
from flask_bcrypt import Bcrypt
from flask import Markup
import codecs
import json
import mimetypes

app = Flask(__name__, template_folder='templates', static_folder='static')
bcrypt = Bcrypt(app )
app.secret_key = "o03af53aUrJHZAjD0eKWgWVTqS7XL7FU"

data_portals_focused = {}
data_focused = {}


def open_html_file(file_name):
    f = codecs.open(file_name, "r", 'utf-8')
    txt = f.read()
    f.close()
    return txt


def open_image(img):
    with open(img, "rb") as image_file:
        return image_file.read()


@app.route('/<js_file>.js')
def open_js(js_file):
    return open_html_file("assets/" + js_file + ".js")


@app.route('/<css_file>.css')
def open_css(css_file):
    return open_html_file("assets/" + css_file + ".css")


@app.route('/<xlsx_file>.xlsx')
def open_xlsx(xlsx_file):
    path = "xlsx//" + session['username'] + "//output.xlsx"
    return send_file(path, as_attachment=True)


@app.route('/imgs/<image>')
def back_png(image):
    mimetypes.add_type('image/svg+xml', '.svg')
    return open_image('imgs/' + image)


@app.route('/<html_file>')
def open_html(html_file):
    return render_template(html_file + ".html")
    # if 'username' in session:
    #     return render_template(html_file + ".html")
    # else:
    #     return render_template("login.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login_me', methods=['POST'])
def login():
    if bcrypt.check_password_hash(b'$2b$12$AFcYR1LllEgT5hw/1TdNme.O8Hv3MFSxFJKmfXdWl/MHYJ0azPibe',
                                  request.get_json(force=True)["Password"]):
        session['username'] = request.get_json(force=True)["Username"]
        send = {"accepted": "True", "Username": session["username"]}
        ip_address = request.remote_addr
        print("IP registered: " + ip_address + " under the name: " + session["username"])
        return send

    else:
        send = {"accepted": "False"}
        return send


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="443", debug=True, ssl_context="adhoc")
