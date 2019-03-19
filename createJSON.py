import json
import requests

class createJSON:
    ranges = {
        "min-temperature": 20,
        "max-temperature": 30,
        "min-humidity": 50,
        "max-humidity": 60
        
        }
    
    def create_JSON(self,path,fileName):
        filePath = path + '/' + fileName + '.json'
        with open(filePath, "w") as fp:
            json.dump(self.ranges, fp)
        
x = createJSON()
x.create_JSON("C:/Users/sanch/PIoT_Assignment", "config")


    