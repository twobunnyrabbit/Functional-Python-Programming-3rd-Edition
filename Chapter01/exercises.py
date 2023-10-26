"""
inputs:
    - lat1
    - lat2
    - lon1
    - lon2
    - dlat = rad(lat1) - rad(lat2)
    - dlon = rad(lon1) - rad(lon2)
    - latm = (rad(lat1) + rad(lat2))/2
    - c = cos(latm)
    - x = c x R x (rad(lon1) - rad(lon2))
    - y = R x (rad(lat1) - rad(lat2))
outputs:
    - d = sqrt(x^2 + y^2)

rlon1 = rad(lon1)

x = R x (rlon1 - rlon2)
"""

import math


def rads(d: float) -> float:
    """
    Converts degrees to radians.
    """
    return math.pi * d / 180


def getX(
    c: float, R: float, lat1: float, lat2: float, lon1: float, lon2: float
) -> float:
    """
    Obtain the x coordinate for whatever this is.
    """
    rlon1 = rads(lon1)
    rlon2 = rads(lon2)
    latm = (rads(lat1) + rads(lat2)) / 2
    c = math.cos(latm)
    return c * R * (rlon1 - rlon2)


def getY(R: float, lat1: float, lat2: float) -> float:
    return R * (rads(lat1) - rads(lat2))


c = 2
R = 5
lat1 = 32.82950
lon1 = -79.93021
lat2 = 32.74412
lon2 = -79.85226

d = math.hypot(getX(c, R, lat1, lat2, lon1, lon2), getY(R, lat1, lat2))
print(d)
