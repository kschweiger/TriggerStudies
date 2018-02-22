import json, yaml

def count(filename):
    data = None
    with open(filename, 'r') as f:
        data = yaml.safe_load(f) #json loads all entries as unicode (u'..')
    DSEvents = 0
    for _file in data["data"]:
        try:
            _file["file"][0]["nevents"]
        except KeyError:
            print "nEvents missing"
        else:
            DSEvents += _file["file"][0]["nevents"]

    print DSEvents


if __name__ == "__main__":
    filename = "EphemeralHLTPhysics1-Run2017F.json"
    count(filename)
