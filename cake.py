def cakes(recipe, available):
    variants = []
    for key, value in recipe.items():
        if key in available.keys():
            variants.append(available.get(key) / value)
            print(variants)
        else:
            return 0
    return int(min(variants))


recipe = {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200}
available = {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}
print(cakes(recipe, available))

# recipe {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200}
# and available ingredients {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}

# recipe {'flour': 500, 'eggs': 1, 'sugar': 200}
# and available ingredients {'flour': 1200, 'eggs': 5, 'milk': 200, 'sugar': 1200}

# print(' '.join(sorted(recipe.keys())))
#  print(' '.join(sorted(available.keys())))
# if ' '.join(recipe.keys()).split() in ' '.join(available.keys()).split():

