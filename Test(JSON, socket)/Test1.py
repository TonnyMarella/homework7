import json

input_info = {
    "atmospheric composition": 15,
    "density": 5700,
    "illumination": 35,
    "axial tilt": 48,
    "terrain": 86,
    "acceleration of gravity": 12,
    "mass": 62345,
    "radius": 6378,
    "deviation from sphericity":  15,
    "flatness": 34,
    "ocean depth": 1887,
    "ocean composition": 65
}

with open("test.json", "w") as file:
    json.dump(input_info, file, indent=3)

result = {"same": {}, "different": {}}

with open("test.json", "r") as file:
    with open("ocean.json", "w") as end_file:
        date = json.load(file)
        for key, values in date.items():
            if values % 2 == 0 and values < 100:
                result["same"][key] = values
            else:
                result["different"][key] = values
        json.dump(result, end_file, indent=4)

