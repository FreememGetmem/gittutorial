from flask import Flask, render_template, request, redirect, url_for
### Jina2 Template Engine

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><head><title>Welcome</title></head><body><h1>Welcome to this Flask best Application ! </h1></body></html>'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
   if request.method == 'POST':
       name = request.form['name']
       return 'Hello, {}!'.format(name)
   return render_template('form.html')

#@app.route('/submit', methods=['GET', 'POST'])
#def submit():
#   if request.method == 'POST':
#       name = request.form['name']
#       return 'Hello, {}!'.format(name)
#   return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    ##return 'The marks you got is ' + str(score)
    res = ""
    if score >=50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result.html', result=res)

# Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    ##return 'The marks you got is ' + str(score)
    res = ""
    if score >=50:
        res = "Passed"
    else:
        res = "Failed"
    exp = {'score':score, 'result':res}
    return render_template('result1.html', result=exp)

# Variable Rule
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', result=score)
    
# Variable Rule
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result=score)

# Variable Rule
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science + maths + c + datascience)/4
        #return 'The total score is {}'.format(total_score)
    
    return redirect(url_for('successres', score=total_score))
    
    #return render_template('result.html', result=total_score)

if __name__ == "__name__":
    app.run(debug=True)