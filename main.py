from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def homepage():
    return render_template('telalogin.html')


@app.route('/cadastrocartao')
def cadastrocartao():
    return render_template('cadastrocartao.html')


@app.route('/cadastracompras')
def cadastracompras():
    return render_template('cadastracompras.html')

@app.route('/listacartao')
def listacartao():
    return render_template('listacartao.html')


@app.route('/relatoriodegastos')
def relatoriodegastos():
    return render_template('relatorioDeGastos.html')


@app.route('/visualizarfatura')
def visualizarfatura():
    return render_template('visualizarFatura.html')

@app.route('/dashboardhome')
def dashboardHome():
    return render_template('dashboardhome.html')

if __name__ == '__main__':
    app.run(debug=True)
