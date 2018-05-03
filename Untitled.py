favorite_foods = {"Christiane":["Takuyaki,","Potatoes,","Donuts"],
                  "Alex":["Sushi,","Burgers,","Pizza"],
                  "Benngy":["Tuna Casserole,","Burgers,","Salmon"]}
for person in favorite_foods:
    print(person, end=": ")
    for food in favorite_foods[person]:
        print(food, end=" ")
    print()
