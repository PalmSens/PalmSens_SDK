from __future__ import annotations

import pypalmsens as ps

man = ps.connect()

comm = man._comm
cap = man._comm.Capabilities


if __name__ == '__main__':
    c = man.capabilities
    breakpoint()
