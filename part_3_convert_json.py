import json
import cc_dat_utils

#Part 3
#Load your custom JSON file
with open("data/bea_test_part3.json", "r") as file:
    json_data = json.load(file)

#Convert JSON data to CCLevelPack
cc_level_pack = cc_dat_utils.make_cc_level_pack_from_json(json_data)

#Save converted data to DAT file
print(cc_level_pack)
output_dat_file = "data/bea_test_part3.dat"
cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, output_dat_file)

print("Conversion complete! Saved as {output_dat_file}")
