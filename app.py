import helpers
from flask import Flask, flash, render_template, request
import time


# Configure application
app = Flask(__name__)

app.secret_key = 'FORTNITE'

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)
        start_time = time.time()
        helpers.merge_sort_protein(food_data_map)
        end_time = time.time()
        elapsed_time = end_time - start_time


        order = request.form.get("order")
        size = int(request.form.get("list"))
        protein = []
        for i in range(size):
            protein.append(food_data_map[i].Description)


        if order == "Low to High":
            protein.reverse()
        if order == "High to Low":
            protein = protein

        flash("Merge Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listP.html", protein = protein)

    else:
        opts = ["Low to High", "High to Low"]
        return render_template('mergeP.html', opts = opts)

@app.route("/mergeC", methods=["GET", "POST"])
def mergeC():
    if request.method == "POST":
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)
        start_time = time.time()
        helpers.merge_sort_carb(food_data_map)
        end_time = time.time()
        elapsed_time = end_time - start_time

        order = request.form.get("order")
        size = int(request.form.get("list"))
        carbohydrates = []
        for i in range(size):
            carbohydrates.append(food_data_map[i].Description)

        if order == "Low to High":
            carbohydrates.reverse()
        if order == "High to Low":
            carbohydrates = carbohydrates

        flash("Merge Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listC.html", carbohydrates = carbohydrates)

    else:
        opts = ["Low to High", "High to Low"]
        return render_template('mergeC.html', opts = opts)

@app.route("/mergeF", methods=["GET", "POST"])
def mergeF():
    if request.method == "POST":
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)
        start_time = time.time()
        helpers.merge_sort_fat(food_data_map)
        end_time = time.time()
        elapsed_time = end_time - start_time

        order = request.form.get("order")
        size = int(request.form.get("list"))


        fats = []
        for i in range(size):
            fats.append(food_data_map[i].Description)

        if order == "Low to High":
            fats.reverse()
        if order == "High to Low":
            fats = fats

        flash("Merge Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listF.html", fats=fats)

    else:
        opts = ["Low to High", "High to Low"]
        return render_template('mergeF.html', opts = opts)

@app.route("/quickF", methods=["GET", "POST"])
def quickF():
    if request.method == "POST":
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)
        start_time = time.time()
        helpers.quicksort("fats",food_data_map, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time

        order = request.form.get("order")
        size = int(request.form.get("list"))


        fats = []
        for i in range(size):
            fats.append(food_data_map[i].Description)

        if order == "Low to High":
            fats.reverse()
        if order == "High to Low":
            fats = fats

        flash("Quick Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listF.html", fats=fats)

    else:
        opts = ["Low to High", "High to Low"]
        return render_template('quickF.html', opts =opts)

@app.route("/quickC", methods=["GET", "POST"])
def quickC():
    if request.method == "POST":
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)
        start_time = time.time()
        helpers.quicksort("carb", food_data_map, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time

        order = request.form.get("order")
        size = int(request.form.get("list"))
        carbohydrates = []
        for i in range(size):
            carbohydrates.append(food_data_map[i].Description)

        if order == "Low to High":
            carbohydrates.reverse()
        if order == "High to Low":
            carbohydrates = carbohydrates

        flash("Quick Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listC.html", carbohydrates= carbohydrates)

    else:
        opts = ["Low to High", "High to Low"]
        return render_template('quickC.html', opts =opts)

@app.route("/quickP",methods=["GET", "POST"])
def quickP():
    if request.method == "POST":
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)
        start_time = time.time()
        helpers.quicksort("protein", food_data_map, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time

        order = request.form.get("order")
        size = int(request.form.get("list"))
        protein = []
        for i in range(size):
            protein.append(food_data_map[i].Description)

        if order == "Low to High":
            protein.reverse()
        if order == "High to Low":
            protein = protein

        flash("Quick Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listP.html", protein=protein)

    else:
        opts = ["Low to High", "High to Low"]
        return render_template('quickP.html', opts = opts)

@app.route("/listP", methods=["GET"])
def list():

    return render_template("listP.html")

@app.route("/listC", methods=["GET"])
def list2():

    return render_template("listC.html")

@app.route("/listF", methods=["GET"])
def list3():

    return render_template("listF.html")









