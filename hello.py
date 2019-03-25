from flask import Flask, render_template, request
import codecs
app = Flask(__name__)

@app.route('/')
def hello():
    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template('programing_record.html', lines = lines)

@app.route('/confirm', methods=["POST"])
def confirm():
    lang = request.form["name"]
    article = request.form["article"]
    file = codecs.open("articles.txt", "a", "utf-8")
    file.write(lang + "," + article + "\n")
    file.close()
    return render_template('confirm.html', lang = lang, article = article)
    
    
@app.route('/select', methods=["POST"])
def select_lang():
    lang = request.form["name"]
    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template('javascript.html', lang = lang, lines = lines)

@app.route('/register_site')
def register_site():
    return render_template('register_site.html')

@app.route('/site', methods=["POST"])
def set_site():
    lang = request.form["name"]
    site = request.form["site"]
    file = codecs.open("sites.txt", "a", "utf-8")
    file.write(lang + "," + site + "\n")
    file.close()
    return render_template('confirm.html', lang = lang, article = site)

@app.route('/check_your_site')
def check_site():
    file = codecs.open("sites.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template('check_sites.html', lines = lines)
    