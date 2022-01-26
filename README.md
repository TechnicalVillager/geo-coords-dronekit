# Get Geographical Coordinates of a drone using DroneKit

This repository consists of the following three scripts:
- `geo_coords.py`
- `geo_coords_alt.py`
- `geo_coords_w_heading.py`

## Requirements
- [python](https://www.python.org/)
- [dronekit-python](https://github.com/dronekit/dronekit-python)

## Usage
- On execution, the `geo_coords.py` script will print the `latitude` and `longitude` of the drone's current location.

```terminal
$ python geo_coords.py
```

- On execution, the `geo_coords_alt.py` script will print the current `altitude` in meters along with the `latitude` and `longitude` of the drone's current location.

```terminal
$ python geo_coords_alt.py
```

- On execution, the `geo_coords_w_heading.py` script will print the vehicle's current `heading` angle in degrees along with the `altitude`, `latitude`, and `longitude` of the drone's current location.

```terminal
$ python geo_coords_w_heading.py
```
