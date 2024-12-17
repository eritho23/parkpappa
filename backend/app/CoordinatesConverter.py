from pyproj import Proj, transform

# SWEREF 99 16 30 to WGS84
sweref99_16_30 = Proj(init='epsg:3010')  # SWEREF 99 16 30
wgs84 = Proj(init='epsg:4326')  # WGS84

def ConvertToWGS(easting, northing):
    longitude, latitude = transform(sweref99_16_30, wgs84, easting, northing)
    return longitude, latitude


