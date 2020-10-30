import sys, json;

hhmiNames = ["HHMI", "Howard Hughes Medical Institute", "Janelia Research Campus"]

def isAffiliated(author):
    if author["affiliations"]:
        return any([affiliation["name"].find(name) != -1 for affiliation in author["affiliations"] for name in hhmiNames])

data = json.load(sys.stdin)
for record in data:
    numAffiliations = 0
    for authorNum, author in enumerate(record["authors"], start=1):
        if isAffiliated(author):
            numAffiliations = numAffiliations + 1
            if authorNum == 1 or authorNum == len(record["authors"]) or numAffiliations == 2:
                print(record["lens_id"])
                break