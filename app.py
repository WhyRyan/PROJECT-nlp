from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/postmethod',methods=['POST'])
def get_post_javascript_data():
    jsdata=request.form['javascript_data']
    return jsdata



if __name__== "__main__":
    app.run(debug=True,port=8000)
