from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    imc = ''
    if request.method=='POST' and 'massa' in request.form and 'altura' in request.form:
        w = float(request.form.get('massa'))
        h = float(request.form.get('altura'))
        imc = w/((h/100)**2)
    
    return render_template("index.htm",imc=imc)



if __name__ == "__main__":
    app.run()
