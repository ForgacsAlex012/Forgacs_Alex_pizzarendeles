from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
orders = []

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/pizza-order', methods=["GET", "POST"])
def pizza_order():
    if request.method =="POST":
        _name = request.form.get("name")
        _phone = request.form.get("phone")
        _size = request.form.get("size")
        order ={
            "name": _name,
            "phone": _phone,
            "size": _size}
        orders.append(order)
        print(orders)
    return render_template('pizza_order.html')

if __name__ == "__main__":
    app.run(debug=True)