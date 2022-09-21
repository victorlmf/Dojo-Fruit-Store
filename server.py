from flask import Flask, url_for, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html')

# with redirct to another route
# @app.route('/checkout/<strawberries>/<raspberries>/<apples>/<first_names>/<last_names>/<ids>')         
# def index_checkout(strawberries,raspberries,apples,first_names,last_names,ids):
#     return render_template("checkout.html",strawberry=strawberries,raspberry=raspberries,apple=apples,first_name=first_names, last_name=last_names, student_id=ids)

# @app.route('/checkout', methods=['POST','GET'])         
# def checkout():
#     if request.method == 'POST':
#         strawberry = int(request.form['strawberry'])
#         raspberry = int(request.form['raspberry'])
#         apple = int(request.form['apple'])
#         total_fruits = strawberry + raspberry + apple
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         student_id = request.form['student_id']
#         print(f"Charging {first_name} {last_name} for {total_fruits} fruits.")
#         return redirect(url_for("index_checkout",strawberries=strawberry,raspberries=raspberry,apples=apple,first_names=first_name, last_names=last_name, ids=student_id))
#     else:
#         return render_template('index.html')

# with render_tempalte back to the 'checkout' route
@app.route('/checkout', methods=['POST','GET'])         
def checkout():
    if request.method == 'POST':
        strawberry = int(request.form['strawberry'])
        raspberry = int(request.form['raspberry'])
        apple = int(request.form['apple'])
        total_fruits = strawberry + raspberry + apple
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student_id = request.form['student_id']
        print(f"Charging {first_name} {last_name} for {total_fruits} fruits.")
        return render_template('checkout.html',strawberries=strawberry,raspberries=raspberry,apples=apple,first_names=first_name, last_names=last_name, ids=student_id)
    else:
        return render_template('index.html')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
