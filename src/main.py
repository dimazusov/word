#/usr/local/python3
from flask import Flask
import declension
import parse
app = Flask(__name__)

# на вход слово, на выход возможные варианты
@app.route("/parse/<word>")
def parseRoute(word):
    return parse.handler(word)

# на вход слово, слово в нормальной форме, форма склонения, на выход склоненная форма
@app.route("/declension", methods=['POST'])
def declensionRoute():
    return declension.handler()

if __name__ == "__main__":
    app.run()