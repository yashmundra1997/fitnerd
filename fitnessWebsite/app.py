from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/bmi')
def BMI():
    return render_template('bmi.html')
@app.route('/men')
def Men():
    return render_template('men.html')
@app.route('/women')
def Women():
    return render_template('women.html')
@app.route('/common')
def Common():
    return render_template('common.html')
@app.route('/aboutUs')
def AboutUs():
    return render_template('aboutUs.html')
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')
if __name__=='__main__':
    app.run()