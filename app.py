from flask import Flask, render_template
app = Flask(__name__)

@app.route('/HOME')
def home():
    return render_template('home.html')

@app.route('/CARS')
def cars():
    return render_template('cars.html')

@app.route('/CARS/FORTUNER')
def fortuner():
    return render_template('fortuner.html')

if __name__=='__main__':
    app.run(debug='True')