# SEC290.12179.B1.FA2023
# Abraham Vallejos-Soto
# 9/15/2023
# Week 4 Programming Assignment

print()
cars = {
    "Honda": "Civic",
    "Toyota": "Corolla",
    "Nissan": "Altima"
}

print("Cars results before adding new information: \n{}".format(cars))
print()

cars["Hyundai"] = "Elantra"
print("Cars results after adding new information: \n{}".format(cars))
print()

if "Honda" in cars:
    print("Yes! Honda is in the dictionary")
else:
    print("Sorry my guy!")

print()

models = cars.values()
if "Test" in models:
    print("Yes! Exist in cars models!")
else:
    print('Model "Test" not found!')
print()

for car, model in cars.items():  # The variables "car" and "model" are new to a logic understanding to print!
    print("{} makes cars like {}".format(car, model))

print()
for key in cars:
    print("{} makes cars like {}".format(key, cars[key]))
print()
