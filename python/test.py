from __future__ import annotations

import pypalmsens as ps
from pypalmsens._instruments import capabilities2

man = ps.connect()

comm = man._comm
cap = man._comm.Capabilities


c = capabilities2.Capabilities._init(comm=comm)

if __name__ == '__main__':
    breakpoint()
    # c = man.capabilities
