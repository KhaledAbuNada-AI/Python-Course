info = {
    "Naem": "KhaledNada",
    "Age": 21,
    "University major": "Software engineering",
    "Graduation Year": 2021,
}

print(info["Naem"])
get_info = info.get("University major", "No Key")
get_info1 = info.get("Graduation", "No Key")
print(get_info)
print(get_info1)

print(info.keys())
print(info.values())
print(info.popitem())
print(info)



