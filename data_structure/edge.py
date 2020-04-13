from __future__ import annotations
from dataclasses import dataclass


@dataclass # constructor defined by attributes
class Edge(object):
    u: int # the 'from' vertex
    v: int # the 'to' vertex

    def reversed(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return "{} -> {}".format(self.u, self.v)
