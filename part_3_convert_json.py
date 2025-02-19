import cc_classes
import cc_dat_utils
import json

#Part 3
#Load your custom JSON file
json_data = json.load(open("data/bea_test_part3.json", 'r'))
print(json_data)
#Convert JSON data to CCLevelPack
pack = cc_classes.CCLevelPack()
for level_json in json_data["levels"]:
    level = cc_classes.CCLevel()
    level.level_number = level_json["level_number"]
    #level.time = level_json["time"]
    #level.num_chips = level_json["num_chips"]
    #level.upper_layer = level_json["upper_layer"]
    #level.lower_layer = level_json["lower_layer"]
    #level.optional_fields = level_json["optional_fields"]
    pack.add_level(level)
print(pack)
#Save converted data to DAT file
