# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
xml_file = os.path.abspath("/Users/Jack/Dropbox/Tutorials/python/datastructureinpython/icndb.xml")
xml_file_new = os.path.abspath("/Users/Jack/Dropbox/Tutorials/python/datastructureinpython/icndb_new.xml")

tree = ET.parse(xml_file)
services = tree.getroot()
#for child in services:
#    print child.tag, child.attrib


for service in services.findall('service'):
    id = service.get('id')
    if id == '2':
        name = service.find('name').text
        #virtual_machines = service.find('virtual_machines').text
        for virtual_machine in service.findall('virtual_machines'):
            for vm in virtual_machine.findall('VM'):
                ip = vm.find('ip').text
                vm_name = vm.find('vm_name').text
                zone = vm.find('zone').text
                print ip, vm_name, text
        type = service.find('type').text
        prefix = service.find('prefix').text
        min_clients = service.find('min_clients').text
        max_clients = service.find('max_clients').text
        print id, name, type, prefix, min_clients, max_clients

# find all the VM tag
for vm in services.iter('VM'):
    ip = vm.find('ip').text
    vm_name = vm.find('vm_name').text
    zone = vm.find('zone').text
    print ip, vm_name, zone


# find all the service tag
for service in services.iter('service'):
    id = service.get('id')
    print service.tag, id
    
for service in services.findall('service'):
    id = service.get('id')
    print service.tag, id

# modify xml, write to xml_file_new
for service in services.findall('service'):
    id = service.get('id')
    if id == '1':
        services.remove(service)
        
tree.write(xml_file_new)

    
#tree.write(xml_file_new)

