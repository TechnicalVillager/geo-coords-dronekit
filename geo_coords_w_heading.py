#!/usr/bin/env python

#..................................................................................
# Author  :  Saiffullah Sabir Mohamed
# Github  :  https://github.com/TechnicalVillager
# Website :  http://technicalvillager.github.io/
# Source  :  https://github.com/TechnicalVillager/geo-coords-dronekit/
#..................................................................................

# Import Necessary Packages
from dronekit import connect

# Connecting the Vehicle
vehicle = connect('udpin:127.0.0.1:14551', baud=115200)

# Printing Vehicle's Latitude
print("Vehicle's Latitude              =  ", vehicle.location.global_relative_frame.lat)

# Printing Vehicle's Longitude
print("Vehicle's Longitude             =  ", vehicle.location.global_relative_frame.lon)

# Printing Vehicle's Altitude
print("Vehicle's Altitude (in meters)  =  ", vehicle.location.global_relative_frame.alt)

# Printing Vehicle's Heading Angle
print("Vehicle's Heading               =  ", vehicle.heading)