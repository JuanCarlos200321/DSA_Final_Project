import csv


class FoodData:
    def __init__(self):
        self.Category = ""
        self.Description = ""
        self.DataBankNumber = 0
        self.Alpha_Carotene = 0
        self.Beta_Carotene = 0
        self.Beta_Cryptoxanthin = 0
        self.Carbohydrate = 0.0
        self.Cholesterol = 0
        self.Choline = 0.0
        self.Fiber = 0.0
        self.Lutein_and_Zeaxanthin = 0
        self.Lycopene = 0
        self.Niacin = 0.0
        self.Protein = 0.0
        self.Retinol = 0
        self.Riboflavin = 0.0
        self.Selenium = 0.0
        self.Sugar = 0.0
        self.Thiamin = 0.0
        self.Water = 0.0
        self.Monosaturated_Fat = 0.0
        self.Polysaturated_Fat = 0.0
        self.Saturated_Fat = 0.0
        self.Total_Lipid = 0.0
        self.Calcium = 0
        self.Copper = 0.0
        self.Iron = 0.0
        self.Magnesium = 0
        self.Phosphorus = 0
        self.Potassium = 0
        self.Sodium = 0
        self.Zinc = 0.0
        self.Vitamin_A = 0
        self.Vitamin_B = 0.0
        self.Vitamin_B6 = 0.0
        self.Vitamin_C = 0.0
        self.Vitamin_E = 0.0
        self.Vitamin_K = 0.0


def read_csv_and_populate_map(filename, data_map):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)
        i = 1

        for row in reader:
            x = FoodData()

            x.Category = row[0]
            x.Description = row[1]
            x.DataBankNumber = int(row[2])
            x.Alpha_Carotene = int(row[3])
            x.Beta_Carotene = int(row[4])
            x.Beta_Cryptoxanthin = int(row[5])
            x.Carbohydrate = float(row[6])
            x.Cholesterol = int(row[7])
            x.Choline = float(row[8])
            x.Fiber = float(row[9])
            x.Lutein_and_Zeaxanthin = int(row[10])
            x.Lycopene = int(row[11])
            x.Niacin = float(row[12])
            x.Protein = float(row[13])
            x.Retinol = int(row[14])
            x.Riboflavin = float(row[15])
            x.Selenium = float(row[16])
            x.Sugar = float(row[17])
            x.Thiamin = float(row[18])
            x.Water = float(row[19])
            x.Monosaturated_Fat = float(row[20])
            x.Polysaturated_Fat = float(row[21])
            x.Saturated_Fat = float(row[22])
            x.Total_Lipid = float(row[23])
            x.Calcium = int(row[24])
            x.Copper = float(row[25])
            x.Iron = float(row[26])
            x.Magnesium = int(row[27])
            x.Phosphorus = int(row[28])
            x.Potassium = int(row[29])
            x.Sodium = int(row[30])
            x.Zinc = float(row[31])
            x.Vitamin_A = int(row[32])
            x.Vitamin_B = float(row[33])
            x.Vitamin_B6 = float(row[34])
            x.Vitamin_C = float(row[35])
            x.Vitamin_E = float(row[36])
            x.Vitamin_K = float(row[37])

            data_map.append(x)


def merge_sort_protein(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_protein(left_half)
        merge_sort_protein(right_half)

        i = j = k = 0


        while i < len(left_half) and j < len(right_half):
            if per_calorie_calc(left_half[i], "protein") > per_calorie_calc(right_half[j], "protein"):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def merge_sort_carb(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_carb(left_half)
        merge_sort_carb(right_half)

        i = j = k = 0


        while i < len(left_half) and j < len(right_half):
            if per_calorie_calc(left_half[i], "carb") > per_calorie_calc(right_half[j], "carb"):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1


        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def merge_sort_fat(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_fat(left_half)
        merge_sort_fat(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if per_calorie_calc(left_half[i], "fats") > per_calorie_calc(right_half[j], "fats"):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def per_calorie_calc(obj, type):
    total = obj.Protein * 4 + obj.Carbohydrate * 4 + obj.Total_Lipid * 9

    if total == 0 or total < 1:
        return 0

    if type == "protein":
        return (obj.Protein * 4 / total)

    elif type == "carb":
        return (obj.Carbohydrate * 4 / total)
    elif type == "fats":
        return (obj.Total_Lipid * 9 / total)
    elif type == "total":
        return total
    else:
        return 0

def partition(arr, begin, end, type):
  pivot = begin
  for i in range(begin + 1, end + 1):
      if per_calorie_calc(arr[i], type) >= per_calorie_calc(arr[begin], type):
          pivot += 1
          arr[i], arr[pivot] = arr[pivot], arr[i]
  arr[pivot], arr[begin] = arr[begin], arr[pivot]
  return pivot

def quicksort( type, arr, begin=0, end=None):
  if end is None:
      end = len(arr) - 1

  def _quicksort(arr, begin, end):
      if begin >= end:
          return
      pivot = partition(arr, begin, end, type)
      _quicksort(arr, begin, pivot - 1)
      _quicksort(arr, pivot + 1, end)

  return _quicksort(arr, begin, end)
