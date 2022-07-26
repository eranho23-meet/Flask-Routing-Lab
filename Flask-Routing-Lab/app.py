from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shopcart')
def cart():
    return render_template('cart.html', carted=[])


@app.route('/product-egg')
def egg():
    return render_template('product.html', object='egg', price='2')


@app.route('/product-carrot')
def carrot():
    return render_template('product.html', object='carrot', price='1')


@app.route('/product-ALMwater')
def AlmondWater():
    return render_template('product.html', object='almond water', price='10')


@app.route('/product-birdcage')
def birdcage():
    return render_template('product.html', object='birdcage', price='5')


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
