import json

def print_pokemon_stats(pokemon):
    print("Name:", pokemon["Name"])
    print("Typ:", "/".join(pokemon["Typ"]))
    print("Beschreibung:", pokemon["Beschreibung"])
    print("Größe:", pokemon["Größe"])
    if "Angriff" in pokemon:
        print("Angriff:", pokemon["Angriff"])
    if "Schaden" in pokemon:
        print("Schaden:", pokemon["Schaden"])
    # Hier können weitere Kampfstats hinzugefügt werden, falls vorhanden
    print()

def save_to_json(pokemon_list):
    with open("pokemon_data.json", "w") as json_file:
        json.dump(pokemon_list, json_file)

def load_from_json():
    try:
        with open("pokemon_data.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

# Lade die vorhandenen Pokémon-Daten aus der JSON-Datei oder erstelle eine leere Liste, wenn die Datei nicht existiert
pokemon_list = load_from_json()

print("Willkommen in der Pokémon Kampfstats-App!")

while True:
    print("Verfügbare Pokémon:")
    for index, pokemon in enumerate(pokemon_list, start=1):
        print(f"{index}. {pokemon['Name']}")

    user_choice = input("Gib die Nummer des gewünschten Pokémon ein, 'add' um ein neues Pokémon hinzuzufügen oder 'exit' zum Beenden: ")

    if user_choice.lower() == "exit":
        # Speichere die Pokémon-Daten in die JSON-Datei, bevor das Programm beendet wird
        save_to_json(pokemon_list)
        print("Auf Wiedersehen!")
        break
    elif user_choice.lower() == "add":
        # Benutzer soll ein neues Pokémon hinzufügen
        name = input("Name des neuen Pokémon: ")
        typ = input("Typ des neuen Pokémon (Trenne mehrere Typen mit einem Komma): ").split(",")
        beschreibung = input("Beschreibung des neuen Pokémon: ")
        größe = input("Größe des neuen Pokémon: ")

        # Erstelle ein neues Pokémon-Objekt und füge es zur Liste hinzu
        new_pokemon = {
            "Name": name,
            "Typ": typ,
            "Beschreibung": beschreibung,
            "Größe": größe
        }
        pokemon_list.append(new_pokemon)
        print(f"{name} wurde zur Pokémon-Liste hinzugefügt!\n")
    else:
        try:
            index = int(user_choice) - 1
            selected_pokemon = pokemon_list[index]
            print("\nKampfstats für", selected_pokemon["Name"] + ":")
            print_pokemon_stats(selected_pokemon)
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Bitte gib die Nummer eines Pokémon aus der Liste ein.")
