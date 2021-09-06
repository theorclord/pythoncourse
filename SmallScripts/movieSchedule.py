currentMovies = {
    'The Grinch':"11:00",
    "Rudolph":"13:00",
}

print("We're showing the following movies:")
for x in currentMovies:
    print(x)

movieToSee = input("What movie would you like the showtime for?\n")

showtime = currentMovies[movieToSee]
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movieToSee,"is playing at", showtime)