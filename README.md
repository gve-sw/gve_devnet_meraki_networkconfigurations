# Meraki Network Configuration Script 

The Meraki Network Configuration Script provides an programmable way to make network configuration changes on the meraki network by using the Meraki API. 

## Contacts
* Eda Akturk 
* Simon Fang (sifang@cisco.com)

## Solution Components
* Meraki Dashboard API
* Meraki MS  
* Meraki MX
* Python 

## Installation:

#### Clone the repo
```
$ git clone https://github.com/gve-sw/gve_devnet_meraki_networkconfigurations.git
```

#### Set up a Python venv
First make sure that you have Python 3 installed on your machine. We will then be using venv to create 
an isolated environment with only the necessary packages.

##### Install virtualenv via pip
```
$ pip install virtualenv
```

##### Create a new venv
```
Change to your project folder
$ cd gve_devnet_meraki_networkconfigurations

Create the venv
$ virtualenv venv

Activate your venv
$ source venv/bin/activate
```

#### Install dependencies
```
$ pip install -r requirements.txt
```

## Setup:

1. Add your meraki api key to main.py. 
```
api_key = " "
```

2. You can add your network_id if you would like to perform changes to a single network. (You could also get all the networks if you would like to loop through them)
```
network_id = " "
```

## Usage

Edit the main function with the network calls you would like to test and run the script by the following command:


    $ python main.py


You can check the results from the meraki dashboard. 

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
