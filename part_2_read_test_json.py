import test_data
import json

from test_data import GameLibrary

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
   # for game in json_data["games"]:
        #print(game)
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
reader = open(input_json_file, 'r')
#Use the json module to load the data from the file
json_data = json.load(reader)
reader.close()
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library = make_game_library_from_json(json_data)
#Print out the resulting GameLibrary data using print()
print(game_library)
### End Add Code Here ###