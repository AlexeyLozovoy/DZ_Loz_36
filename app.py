from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title='Главная')


@app.route('/project')
def prodject():
    return render_template("project.html", title='Наши проэкты')


@app.route('/abaut')
def abaut():
    return render_template("abaut.html", title='О нас')


@app.route('/api')
def api():
    import json, random
    obj = None
    with open('example.json', 'r') as file:
        obj = json.load(file)

    obj['temperature'] = random.randint(15, 30)
    obj['humidity'] = random.randint(10, 100)
    ob = random.randint(0, 1)
    if ob == 1:
        obj['boiler']['isRun'] = True
    else:
        obj['boiler']['isRun'] = False
    obj['meter']['electricity']['consumption'] = random.randint(0, 5)
    obj['meter']['gas']['consumption'] = random.randint(0, 5)
    obj['meter']['water']['consumption'] = random.randint(0, 5)

    # Получение параметра из GET-запроса
    param = request.args.get('param')
    if param:
        keys = param.split('.')
        val = obj
        try:
            for key in keys:
                val = val[key]
            obj = val
        except KeyError:
            obj = None

    return json.dumps(obj)


@app.route('/get')
def get():
    return render_template("get.html", title='GETs')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
