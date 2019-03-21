# The file contains code to create JSON file

# Imported the necessary module
import json

# Defined createJSON class


class createJSON:

    # Created ranges dictionary
    ranges = {
        "min-temperature": 20,
        "max-temperature": 30,
        "min-humidity": 50,
        "max-humidity": 60

        }

    # Function to create JSON file using ranges dictionary
    def create_JSON(self, path, fileName):
        filePath = path + '/' + fileName + '.json'
        with open(filePath, "w") as fp:
            json.dump(self.ranges, fp, indent=4)

# Created object to call create_JSON
x = createJSON()
x.create_JSON("C:/Users/sanch/PIoT_Assignment", "config")
