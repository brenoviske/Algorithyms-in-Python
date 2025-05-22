from flask import Flask, render_template, request, url_for
import numpy as np 
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def homepage():
    message = ''
    if request.method == 'POST':
        number = int(request.form.get('number'))
        divisor = 0
        if number >=1 :
            for counter in range ( 1 , number + 1 ):
                if number % counter == 0:
                    divisor+=1
        if divisor == 2 or divisor == 1:
            message = f'The number {number} is prime'
        else:
            message = f'The number {number} is not prime'
    return render_template('index.html',message = message)

@app.route('/evensodds.html', methods=['GET','POST'])
def homepage2():
    evens = []        
    odds = []
    if request.method == 'POST':
        number = int(request.form.get('number'))
        for counter in range ( 1 , number + 1):
            if counter % 2 == 0:
                evens.append(counter)
            else:
                odds.append(counter)
    display = f'Evens: {evens}, Odds:{odds}'
    return render_template('evensodds.html',display=display)
        
if __name__ == '__main__':
    app.run(debug= True)