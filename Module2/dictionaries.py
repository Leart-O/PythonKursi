#collection of items, mutable not indexable, works on a pair key:value
contact_info={
    "Alma":"049123456",
    "Erin":"049876543"
}
print(contact_info)
alma_info=contact_info["Alma"]
print(alma_info)
contact_info["Orkidea"]="049900800"
contact_info["orkidea"]="049900800"
del contact_info["orkidea"]
print(contact_info)
keys=contact_info.keys()
print(keys)
values=contact_info.values()
print(values)
items=contact_info.items()
print(items) #prints out key-value pairs as lists
