print("Madlib!")
print()

sentence = "There are many _(adjective)_ ways to choose an _(noun)_ to watch. First, you could ask for recommendations from your friends and _(noun)_. Just don't ask uncle _(male)_ he only watches _(verb)_ movies with _(verb)_ in them. Maybe in _(city)_ the movies suck to watch? You know your cousin _(female)_ could give you some advice though she really loves _(celebrity)_ to way to much to watch any other movie. Though if you pirate the movies you could watch _(number)_'s of them!!"
print(sentence)

print()
print()
adjective = input("Please enter a adjecive: ").strip()
noun = input("Please enter a noun: ").strip()
noun2 = input("Please enter another noun: ").strip()
male = input("Please enter a name of a male: ").strip()
verb = input("Please enter a verb: ").strip()
verb2 = input("Please enter a verb: ").strip()
city = input("Please enter a city name: ").strip()
female = input("Please enter a name of a female: ").strip()
celebrity = input("Please enter a celebrity name: ").strip()
number = int(input("Please enter a number: "))

print()
print()
madlib = "There are many _{}_ ways to choose an _{}_ to watch. First, you could ask for recommendations from your friends and _{}_. Just don't ask uncle _{}_ she only watches _{}_ movies with _{}_ in them. Maybe in _{}_ the movies suck to watch? You know your cousin _{}_ could give you some advice though she really loves _{}_ to way to much to watch any other movie. Though if you pirate the movies you could watch _{}_'s of them!!".format(adjective, noun, noun2, male, verb, verb2, city, female, celebrity, number)

print(madlib)