"""
це код для перетворення одних довжин в інші
1. '/' - Перенаправлення користувача з самого початку щоб він зміг ввести якесь число
2. '/convert2' - основна логіка та видавання результату в JSON форматі.
"""

from flask import render_template, jsonify, Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def convert1():
    """перенаправлення на сорінку конвертації числ"""
    return render_template("convertation.html")


@app.route("/convert2", methods=["POST", "GET"])
def convert2():
    """
    Хендлер конвертації
    перетворює числа які йому надаються з html через js
    повертає значення JSON.
    """
    convert_from = request.form.get("convert_from")
    convert_to = request.form.get("convert_to")
    number_to = request.form.get("number_to")


    try:
        result = (float(number_to) * float(convert_from)) / float(convert_to)
    except (ValueError, ZeroDivisionError):
        result = "Invalid input or division by zero"

    print(f"Conversion result: {result}")
    response_data = {'message': result}
    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(port=80019, debug=True)
