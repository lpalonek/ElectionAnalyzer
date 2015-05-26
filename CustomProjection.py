__author__ = 'lpalonek'

from cartopy.crs import TransverseMercator
import shapely.geometry as sgeom
import cartopy

__document_these__ = ['Globe']

class CP(TransverseMercator):
    def __init__(self):
        super(CP, self).__init__(central_longitude=-80, central_latitude=55,
                                   scale_factor=0.9996012717,
                                   false_easting=400000,
                                   false_northing=400000)

    @property
    def boundary(self):
        w = self.x_limits[1] - self.x_limits[0]
        h = self.y_limits[1] - self.y_limits[0]
        return sgeom.LineString([(0, 0), (0, h), (w, h), (w, 0), (0, 0)])

    @property
    def x_limits(self):
        return (0, 10e5)

    @property
    def y_limits(self):
        return (0, 10e5)