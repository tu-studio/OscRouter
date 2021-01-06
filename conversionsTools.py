# Comment on Conversions: In General x and y axis were swapped because 0° should be at the front which can easily achieved throu that

import numpy as np
# import str_keys_conventions as skc

# change to f32 ?
def f32(val) -> np.float32:
    return np.float32(val)


deg90_rad = f32(np.deg2rad(90))


def mag_xyz(x, y, z) -> np.float32:
    return np.sqrt(np.square(x) + np.square(y) + np.square(z))

def convert_deg_angleToRad(azimuth, elevation) -> [np.float32]:

    if azimuth < 0:
        azimuth += f32(360)

    azim_rad = np.deg2rad(azimuth)

    # if elevation < 0:
    #     elevation = f16(90) - elevation
    elev_rad = np.deg2rad(elevation)

    return [azim_rad, elev_rad]

    # self._positionIsSet[dk.polar_rad] = True

def conv_pol2cart(azim, elev, dist) -> [np.float32]:


    azim_rad, elev_rad = convert_deg_angleToRad(azim, elev)

    y = np.sin(deg90_rad - elev_rad) * np.cos(azim_rad) * dist
    x = np.sin(deg90_rad - elev_rad) * np.sin(azim_rad) * dist
    z = np.cos(deg90_rad - elev_rad) * dist

    return [x, y, z]

    # self._positionIsSet[dk.cartesian] = True



def conv_pol2ncart(azim, elev, dist) -> [np.float32]:

    azim_rad, elev_rad = convert_deg_angleToRad(azim, elev)

    ny = np.sin(deg90_rad - elev_rad) * np.cos(azim_rad)
    nx = np.sin(deg90_rad - elev_rad) * np.sin(azim_rad)
    nz = np.cos(deg90_rad - elev_rad)

    return [nx, ny, nz, dist]

    # self._positionIsSet[skc.normcartesian] = True


def conv_cart2pol(x, y, z) -> [np.float32]:
    dist = mag_xyz(x, y, z )
    azim_rad = np.arctan(x / y)
    azim = np.rad2deg(azim_rad)
    if azim > 180.:
        azim -= f32(360)

    elev_rad = np.arctan(np.sqrt(np.square(x) + np.square(y) / z))
    elev = np.rad2deg(elev_rad)
    if elev > 90.:
        elev = 90. - elev

    return [azim, elev, dist]


def conv_cart2ncart(x, y, z) -> [np.float32]:
    nd = mag_xyz(x, y, z)
    inv_mag = 1 / nd
    nx = f32(x * inv_mag)
    ny = f32(y * inv_mag)
    nz = f32(z * inv_mag)
    return [nx, ny, nz, nd]

def conv_ncart2pol(nx, ny, nz, nd):
    azim_rad = np.arctan(nx / ny)
    azim = np.rad2deg(azim_rad)
    azim = wrapAzimuth180(azim)

    elev_rad = np.arctan(np.sqrt(np.square(nx) + np.square(ny) / nz))
    elev = np.rad2deg(elev_rad)
    elev = wrapElevation90(elev)

    return [azim, elev, nd]


def conv_ncart2cart(nx, ny, nz, nd) -> [np.float32]:
    x = nx * nd
    y = ny * nd
    z = nz * nd
    return [x, y, z]


def wrapAzimuth180(azim) -> np.float32:
    if azim > 180.:
        azim -= f32(360)
        return azim
    else:
        return azim


def wrapElevation90(elev) -> np.float32:
    if elev > 90.:
        elev = f32(90.) - elev
        return elev
    else:
        return elev

#TODO: right conversions
def apply_factor_addition(values, factors, additions):
    # values
    return values

#TODO: implement this
def azi_to_wonderangle(azim) -> np.float32:
    return azim

def dist_to_gain(dist) -> np.float32:
    return dist