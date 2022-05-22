access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

mode = {
    'access': {'acc' : access_template},
    'trunk': {
        'trunk_template' : [
            "switchport trunk encapsulation dot1q",
            "switchport mode trunk",
            "switchport trunk allowed vlan {}",
             ]
        }
}

print(mode['access'].values())
