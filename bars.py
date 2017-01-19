import json
import math

def load_data(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    return data


def get_biggest_bar(data):
    biggest_bar = max(data, key = lambda i: i['SeatsCount'])
    return (biggest_bar['Name'], biggest_bar['SeatsCount'])

def get_smallest_bar(data):
    biggest_bar = min(data, key = lambda i: i['SeatsCount'])
    return (biggest_bar['Name'], biggest_bar['SeatsCount'])

def get_distance(x1, y1, x2, y2):
    distance = math.sqrt((float(x2)-x1)**2+(float(y2)-y1)**2)
    return distance

def get_closest_bar(data, longitude, latitude):
    closest_bar = min([{"Name": bar['Name'], "Address": bar['Address'], "Distance" : get_distance(latitude, longitude, bar['Latitude_WGS84'], bar['Longitude_WGS84'])} for bar in data], key = lambda i: i["Distance"])
    return closest_bar


if __name__ == '__main__':
    filepath = input("Enter path to your json file: ")
    data = load_data(filepath)
    biggest_bar = get_biggest_bar(data)
    print("The biggest bar is %s and the number of seats there: %d" % biggest_bar)
    smallest_bar = get_smallest_bar(data)
    print("The smallest bar is %s and the number of seats there: %d" % smallest_bar)
    latitude = float(input("Enter latitude of your location, f.e. 45.56: "))
    longitude = float(input("Enter longitude of your location, f.e. 47.67: "))
    closest_bar = get_closest_bar(data, longitude, latitude)
    print("The closest bar is {} and its address {}".format(closest_bar["Name"],closest_bar["Address"]))
