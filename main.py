from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')
i = 0
pas = 0
ema = 0


@app.route('/delit')
def delit():
    global pas, ema, i
    pas = 0
    ema = 0
    i = 0
    return main()


@app.route('/')
@app.route('/main')
def main():
    global i, pas, ema
    print(i, pas, ema)
    return render_template('main.html', ema=ema, pas=pas)


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    global i, ema, pas
    i = 1
    if request.method == 'GET':
        return f'''         <!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, 
                                    initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" />
                                    <title>reg</title>
                                  </head>
                                  <body>
                                    <h1>Регистрация</h1>
                                    <div>
                                        <form class="login_form" method="post">
                                            <input type="email" class="form-control" id="email" 
                                            aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                            <input type="password" class="form-control" id="password" 
                                            placeholder="Введите пароль" name="password">
                                            <button href="/main" type="submit" class="btn btn-primary">Записаться
                                            </button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''
    elif request.method == 'POST':
        ema = request.form['email']
        pas = request.form['password']
        return main()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
