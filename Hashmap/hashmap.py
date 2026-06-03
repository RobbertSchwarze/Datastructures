# Maak een hashmap, dit is eigenlijk gewoon een dictionary.

studenten = {}

# Toevoegen
studenten["Jan"] = 20
studenten["Emma"] = 22
studenten["Tom"] = 19

# Ophalen
print(studenten["Jan"])

# Updaten
studenten["Jan"] = 21

# Verwijderen
del studenten["Tom"]

print(studenten)

# Wat slaat een HashMap op?
# Een HashMap bewaart gegevens als key-value pairs:

# "Jan" -> 20
# "Emma" -> 22
# "Tom" -> 19

# Key = unieke identifier
# Value = bijbehorende data

