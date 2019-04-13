# age = 25;
age = input("How old are you? ")
seconds_of_life = (int(age) * 365 * 24 * 60 * 60)

# print("You have lived for " + str(seconds_of_life) + " seconds or" + age + " years.")
print("You have lived for {} seconds or {} years.".format(seconds_of_life, age))
