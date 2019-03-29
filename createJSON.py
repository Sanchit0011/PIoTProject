# The file contains code to create JSON file

# Imported the necessary modules
import json
import os

# Defined createJSON class


class createJSON:

    # Created ranges dictionary
    ranges = {
        "min-temperature": 20,
        "max-temperature": 30,
        "min-humidity": 30,
        "max-humidity": 40

        }

    # Function to create JSON file using ranges dictionary
    def create_JSON(self):
        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        filePath = rel_path + 'config.json'
        with open(filePath, "w") as fp:
            json.dump(self.ranges, fp, indent=4)

# Created object to call create_JSON
x = createJSON()
x.create_JSON()
