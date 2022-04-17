#!/usr/bin/env python

interface = input('enter interface type and number: ')
vlan = input('enter VLAN number: ')

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']


print('-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
