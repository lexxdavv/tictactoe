# #8-12
# def sandwich_order(*items):
#     print("Sandwich order:")
#     for item in items:
#         print("- " + item)
#     print("Enjoy your sandwich!\n")

# sandwich_order('turkey', 'bacon', 'lettuce', 'tomato', 'mayo')
# sandwich_order('peanut butter', 'jelly')
# sandwich_order('ham', 'cheese')
# #8-13
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('lexi', 'davis',
#                              location='chicago',
#                              hobbies=['coding', 'gaming', 'cooking'])
# print(user_profile)


#8-14
def make_car(manufacturer, model_name, **car_info):
  car = {}
  car['manufacturer'] = manufacturer
  car['model_name'] = model_name
  # for key, value in car_info.items():
  #     car[key] = value
  car = car | car_info
  return car


car = make_car('tesla', 'model s', color='white', interior="red")
print(car)
