from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Rat</title>
                  </head>
                  <body>
                    <div align="right">
                      <button type="submit" class="btn btn-primary">зарегестрироваться</button>
                      <button type="submit" class="btn btn-primary">войти</button>
                    </div>
                    <h1 align="center">RAT</h1>
                    <h3 style="margin-top: 100px;" align="center">Base</h3>
                    <img src="data/Chest.jpg" />
                  </body>
                </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
