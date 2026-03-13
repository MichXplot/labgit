london_co = {
    "r1": {"location": "21 New Globe Walk", "vendor": "Cisco", "model": "4451", "ios": "15.4", "ip": "10.255.0.1"},
    "r2": {"location": "21 New Globe Walk", "vendor": "Cisco", "model": "4451", "ios": "15.4", "ip": "10.255.0.2"},
    "sw1": {"location": "21 New Globe Walk", "vendor": "Cisco", "model": "3850", "ios": "3.6.XE", "ip": "10.255.0.101", "vlans": "10,20,30", "routing": True},
}

d = {
    "vendor": [],
    "model": [],
    "ip": []
}

for device in london_co:
    d["vendor"].append(london_co[device]["vendor"])
    d["model"].append(london_co[device]["model"])
    d["ip"].append(london_co[device]["ip"])

def test_dict():
    print(d)
    assert "3850" in d["model"]
    assert "10.255.0.2" in d["ip"]
    print("OK")

test_dict()