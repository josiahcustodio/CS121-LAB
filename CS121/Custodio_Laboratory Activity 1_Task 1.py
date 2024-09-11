try:
    Year = int(input("Enter the year: "))
except ValueError:
    print("Please enter a valid year.")
    Year = int(input("Enter the year: "))

Genre = input("Enter the genre: ")
Album = input("Enter the album: ")
Title = input("Enter the song title: ")
Artist = input("Enter the artist: ")

print("-------------------------")
print("SONG DETAILS")
print("-------------------------")

print(f"Year Released: {Year}")
print(f"Genre: {Genre}")
print(f"Album: {Album}")
print(f"Title: {Title}")
print(f"Artist: {Artist}")
