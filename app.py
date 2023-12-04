import helpers
from flask import Flask, flash, render_template, request
import time

# Configure application
app = Flask(__name__)

app.secret_key = 'FORTNITE'


#Home Page Merge Sort Proteins
@app.route("/", methods=["GET", "POST"])
def home():

    #If generate button is clicked
    if request.method == "POST":

        #Read and Sort Data
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)

        #Get time of Merge Sort
        start_time = time.time()
        helpers.merge_sort_protein(food_data_map)
        end_time = time.time()
        elapsed_time = end_time - start_time

        #Check for user input
        order = request.form.get("order")
        size = int(request.form.get("list"))
        protein = []
        for i in range(size):
            protein.append(food_data_map[i].Description)

        if order == "Low to High":
            protein.reverse()
        if order == "High to Low":
            protein = protein

        #Display Time elapsed and render list
        flash("Merge Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listP.html", protein = protein)

    #Render home page with input options
    else:
        opts = ["Low to High", "High to Low"]
        return render_template('mergeP.html', opts = opts)


#Merge Sort Carbohydrates
@app.route("/mergeC", methods=["GET", "POST"])
def mergeC():

    # If generate button is clicked
    if request.method == "POST":

        # Read and Sort Data
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)

        # Get time of Merge Sort
        start_time = time.time()
        helpers.merge_sort_carb(food_data_map)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check for user input
        order = request.form.get("order")
        size = int(request.form.get("list"))
        carbohydrates = []
        for i in range(size):
            carbohydrates.append(food_data_map[i].Description)

        if order == "Low to High":
            carbohydrates.reverse()
        if order == "High to Low":
            carbohydrates = carbohydrates

        # Display Time elapsed and render list
        flash("Merge Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listC.html", carbohydrates = carbohydrates)

    #Render Merge Carbs with input options
    else:
        opts = ["Low to High", "High to Low"]
        return render_template('mergeC.html', opts = opts)


#Merge Sort Fats
@app.route("/mergeF", methods=["GET", "POST"])
def mergeF():

    # If generate button is clicked
    if request.method == "POST":

        # Read and Sort Data
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)

        # Get time of Merge Sort
        start_time = time.time()
        helpers.merge_sort_fat(food_data_map)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check for user input
        order = request.form.get("order")
        size = int(request.form.get("list"))
        fats = []
        for i in range(size):
            fats.append(food_data_map[i].Description)

        if order == "Low to High":
            fats.reverse()
        if order == "High to Low":
            fats = fats

        # Display Time elapsed and render list
        flash("Merge Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listF.html", fats=fats)

    #Render Merge Fats with input options
    else:
        opts = ["Low to High", "High to Low"]
        return render_template('mergeF.html', opts = opts)


#Quick Sort Fats
@app.route("/quickF", methods=["GET", "POST"])
def quickF():

    # If generate button is clicked
    if request.method == "POST":

        # Read and Sort Data
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)

        # Get time of Quick Sort
        start_time = time.time()
        helpers.quicksort("fats",food_data_map, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check for user input
        order = request.form.get("order")
        size = int(request.form.get("list"))
        fats = []
        for i in range(size):
            fats.append(food_data_map[i].Description)

        if order == "Low to High":
            fats.reverse()
        if order == "High to Low":
            fats = fats

        # Display Time elapsed and render list
        flash("Quick Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listF.html", fats=fats)

    #Render Quick Fats with input options
    else:
        opts = ["Low to High", "High to Low"]
        return render_template('quickF.html', opts =opts)


#Quick Sort Carbohydrates
@app.route("/quickC", methods=["GET", "POST"])
def quickC():

    # If generate button is clicked
    if request.method == "POST":

        # Read and Sort Data
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)

        # Get time of Quick Sort
        start_time = time.time()
        helpers.quicksort("carb", food_data_map, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check for user input
        order = request.form.get("order")
        size = int(request.form.get("list"))
        carbohydrates = []
        for i in range(size):
            carbohydrates.append(food_data_map[i].Description)

        if order == "Low to High":
            carbohydrates.reverse()
        if order == "High to Low":
            carbohydrates = carbohydrates

        # Display Time elapsed and render list
        flash("Quick Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listC.html", carbohydrates= carbohydrates)

    #Render Quick Carbs with input options
    else:
        opts = ["Low to High", "High to Low"]
        return render_template('quickC.html', opts =opts)


#Quick Sort Protein
@app.route("/quickP",methods=["GET", "POST"])
def quickP():

    # If generate button is clicked
    if request.method == "POST":

        # Read and Sort Data
        food_data_map = []
        helpers.read_csv_and_populate_map("food.csv", food_data_map)

        # Get time of Quick Sort
        start_time = time.time()
        helpers.quicksort("protein", food_data_map, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check for user input
        order = request.form.get("order")
        size = int(request.form.get("list"))
        protein = []
        for i in range(size):
            protein.append(food_data_map[i].Description)

        if order == "Low to High":
            protein.reverse()
        if order == "High to Low":
            protein = protein

        # Display Time elapsed and render list
        flash("Quick Sort took " + str(elapsed_time) + " seconds", "time")
        return render_template("listP.html", protein=protein)

    #Render Quick Protein with input options
    else:
        opts = ["Low to High", "High to Low"]
        return render_template('quickP.html', opts = opts)


# 3 seperate list pages for Protein, Carbs, Fats

@app.route("/listP", methods=["GET"])
def list():

    return render_template("listP.html")

@app.route("/listC", methods=["GET"])
def list2():

    return render_template("listC.html")

@app.route("/listF", methods=["GET"])
def list3():

    return render_template("listF.html")









