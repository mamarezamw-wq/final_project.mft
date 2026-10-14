# Movie lists
romantic = ["Titanic", "The Notebook", "La La Land", "Pride and Prejudice", "Me Before You"]
horror = ["The Conjuring", "It", "Annabelle", "Insidious", "Hereditary"]
action = ["John Wick", "Mad Max", "Die Hard", "The Dark Knight", "Mission Impossible"]

all_movies = romantic + horror + action

print("=== Movie List ===")
for i in range(len(all_movies)):
    print(i + 1, "-", all_movies[i])

# Choose 5 movies for the wishlist
wishlist = []

while len(wishlist) < 5:
    number = int(input("Enter the movie number: "))

    if number < 1 or number > len(all_movies):
        print("Invalid number, try again")
    elif all_movies[number - 1] in wishlist:
        print("You already chose this movie")
    else:
        wishlist.append(all_movies[number - 1])
        print("Added! Movies chosen:", len(wishlist), "of 5")

print("\n=== Your Wishlist ===")
for movie in wishlist:
    print("-", movie)

# Count genres
romantic_count = 0
horror_count = 0
action_count = 0

for movie in wishlist:
    if movie in romantic:
        romantic_count += 1
    elif movie in horror:
        horror_count += 1
    elif movie in action:
        action_count += 1

print("\nRomantic:", romantic_count)
print("Horror:", horror_count)
print("Action:", action_count)

# Find the favorite genre
if romantic_count >= horror_count and romantic_count >= action_count:
    top_genre = "romantic"
elif horror_count >= romantic_count and horror_count >= action_count:
    top_genre = "horror"
else:
    top_genre = "action"

match top_genre:
    case "romantic":
        favorite = romantic
        genre_name = "romantic"
    case "horror":
        favorite = horror
        genre_name = "horror"
    case "action":
        favorite = action
        genre_name = "action"

# Recommend the first movie of that genre that is not in the wishlist
for movie in favorite:
    if movie not in wishlist:
        print("\nBecause most of your picks were", genre_name + ",")
        print("we recommend:", movie)
        break
