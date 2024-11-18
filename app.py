from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
orders = []

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/pizza-order', methods=["GET", "POST"])
def pizza_order():
    if request.method == "POST":
        _name = request.form.get("name")
        _phone = request.form.get("phone")
        _size = request.form.get("size")
        _toppings = request.form.getlist("toppings")
        _quantity = request.form.get("quantity")
        _delivery_time = request.form.get("delivery_time")
        _comments = request.form.get("comments")

        order = {
            "name": _name,
            "phone": _phone,
            "size": _size,
            "toppings": _toppings,
            "quantity": _quantity,
            "delivery_time": _delivery_time,
            "comments": _comments
        }
        orders.append(order)
        return redirect(url_for('order_summary'))

    return render_template('pizza_order.html')

@app.route('/order-summary', methods=["GET"])
def order_summary():
    return render_template('order_summary.html', orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
