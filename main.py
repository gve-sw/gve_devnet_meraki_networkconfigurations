import json
import requests

base_url = "https://api.meraki.com/api/v1/"
api_key = " "
network_id = " "


def get_organizations():
    url = f"{base_url}organizations"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def get_networks(organization_id):
    url = f"{base_url}organizations/{organization_id}/networks"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def get_devices(network_id):
    url = f"{base_url}networks/{network_id}/devices"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def get_vlan(network_id):
    url = f"{base_url}networks/{network_id}/appliance/vlans"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def create_vlan(network_id, vlan, vlan_name, subnet, device_id):
    """
    Create vlan: https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan
    """
    url = f"{base_url}networks/{network_id}/appliance/vlans"
    payload = {
        "id": vlan,
        "name": vlan_name,
        "subnet": subnet,
        "applianceIp": device_id
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
    return response.json()


def update_vlan(network_id, vlan, appliance_ip):
    """
    Update network applince vlan: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan
    """
    url = f"{base_url}networks/{network_id}/appliance/vlans/{vlan}"
    payload = {
        "applianceIp": appliance_ip
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('PUT', url, headers=headers, data=json.dumps(payload))
    return response.json()


def get_network_appliance_ports(network_id):
    url = f"https://api.meraki.com/api/v1/networks/{network_id}/appliance/ports"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def update_network_appliance_port(network_id, port_id, vlan):
    """
    Update Network Appliance Port: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port
    """
    url = f"https://api.meraki.com/api/v1/networks/{network_id}/appliance/ports/{port_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    payload = {
        "enabled": "true",
        "type": "access",
        "dropUntaggedTraffic": "false",
        "vlan": vlan,
        "accessPolicy": "open"
    }
    response = requests.request('PUT', url, headers=headers, data=json.dumps(payload))
    return response.json()


def get_network_switch_settings(serial):
    url = f"{base_url}devices/{serial}/switch/ports"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def update_network_switch_settings(serial, port_id, vlan):
    """
    Update Network Switch Settings: https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings
    """
    url = f"{base_url}devices/{serial}/switch/ports/{port_id}"
    payload = {
        "name": "My switch port",
        "vlan": vlan
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('PUT', url, headers=headers, data=json.dumps(payload))
    return response.json()


def get_network_switch_static_routes(serial):
    url = f"{base_url}devices/{serial}/switch/routing/staticRoutes"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def update_network_switch_static_routes(serial, static_route_id, name, subnet, next_hop_ip):
    """
    Update Network Switch Static Route: https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route
    """
    url = f"{base_url}devices/{serial}/switch/routing/staticRoutes/{static_route_id}"
    payload = {
        "name": name,
        "subnet": subnet,
        "nextHopIp": next_hop_ip
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('PUT', url, headers=headers, data=json.dumps(payload))
    return response.json()


def get_device_management_interface(serial):
    """
    Get Device Management Interface: https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface
    """
    url = f"{base_url}devices/{serial}/managementInterface"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('PUT', url, headers=headers)
    return response.json()


def update_device_management_interface(serial, ip, vlan):
    """
    Update Device Management Interface: https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface
    """
    url = f"{base_url}devices/{serial}/managementInterface"
    payload = {
        "wan1": {
            "staticIp": ip,
            "vlan": vlan
        },
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('PUT', url, headers=headers, data=json.dumps(payload))
    return response.json()


if __name__ == '__main__':
    # Use the functions above to make config changes on the Meraki network

    devices = get_devices(network_id)
    print(devices)

    """
    # Sample code to create vlan:
    
    vlan = "1002"
    vlan_name = "Test from python"
    subnet = "192.168.1.0/24"
    device_id = "192.168.1.2"
    add_vlan = create_vlan(network_id, vlan, vlan_name,subnet,device_id)


    # Sample code to pass list of device serial id's and get the sw network settings for them
    
    serial_numbers = ["xxx", "yyy", "zzz"] # set array with serial ids
    
    for device in serial_numbers: # loop through serial ids and get the network switch settings
        settings = get_network_switch_settings(device)
        print(settings)
        
        
    # Sample code to get the static routes of all the devices: 

    devices = get_devices(network_id)
    for device in devices:
        serial = device["serial"]
        static_routes = get_network_switch_static_routes(serial)
        msg = f"Device: {serial} the static routes are:"
        print(msg)
        for route in static_routes:
            route_id = route["staticRouteId"]
            print(route_id)
            

    # Sample code to update network switch static route:

    serial = ' '
    static_routes = get_network_switch_static_routes(serial)
    print(static_routes)
    static_route_id = " "
    subnet = "0.0.0.0/0"
    next_hop = "192.168.128.1"
    new_static_route = update_network_switch_static_routes(serial, static_route_id, "python test", subnet, next_hop)
    print(new_static_route)
    """
