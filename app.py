from flask import Flask , render_template , request
import json
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/' , methods=['POST'])
def taking_input():
        var_html= request.form['html_text']
        var_css= request.form['css_text']
        api_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}
        #calling api
        r = requests.post("https://uncss-online.com:443/api/uncss", headers=api_headers, data={"inputHtml": var_html , "inputCss": var_css}).text
        y = json.loads(r)

        return render_template('output.html' , output=(y['outputCss']))
if __name__ == "__main__":
    app.run()