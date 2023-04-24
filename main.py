# Margarita Chistiakova
# 10/12/2022
# Additional project about functions


def print_two(*movies):
  movie1, movie2 = movies
  print(f"movie1: {movie1}, movie2: {movie2}")

def print_one(movie1):
  print(f"movie1: {movie1}")

print_two("Scream", "The Craft")
print_one("Scream")

def year_of_premiere(year1,year2):
  print(f"The movie 'Scream' appeared in {year1}.")
  print(f"The movie 'The Craft' was published in {year2}.")

# I am going to give the function numbers directly
year_of_premiere(1996, 1996)

print("Wow! I didn't know that both of them were released in 1996!")

# I will try to do it with variables
scream = 1996
the_craft = 1996
year_of_premiere(scream, the_craft)

year_of_premiere(1900 + 90 + 6, 100 + 900 + 500 + 490 + 6)

#Cool
