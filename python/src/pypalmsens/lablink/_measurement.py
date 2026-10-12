"""Submodule for measurement references and data.

[MeasurementRef][] references a stored measurement, [MeasurementJob][]
represents an ongoing measurement, and [Measurement][] holds the complete
data of a finished measurement.

"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

import xarray as xr

if TYPE_CHECKING:
    from ._instrument import InstrumentClaim
    from ._session import Session


class MeasurementRef:
    """
    A reference to a measurement.
    """

    __slots__: ClassVar[tuple[str, ...]] = ('_guid', '_metadata', '_session')

    def __init__(self, guid: str, *, session: Session | None = None):
        self._guid: str = guid
        self._session: Session | None = session

    def __repr__(self) -> str:
        return f'{type(self).__name__}(guid={self.guid!r})'

    @property
    def guid(self) -> str:
        """The unique identifier of the measurement."""
        return self._guid

    async def get_info(self) -> None:
        if self._session is None:
            raise RuntimeError(
                f'This {type(self).__name__} is detached. Reattach it via '
                'ref = session.get_measurement(ref) before fetching data.'
            )
        raise NotImplementedError

    async def get_data(self) -> xr.Dataset | xr.DataTree:
        """
        Get recorded data for this measurement.

        Resolves this reference against the session it is bound to and
        returns the measurement's dataset. The returned object is a
        snapshot of the data as stored on the lablink. It is not live-updated
        if the measurement is still running.

        Returns
        -------
        xarray.Dataset or xarray.DataTree
            The measurement data. A `Dataset` is returned for a single
            measurement, and a `DataTree` when the measurement contains
            repeated/stacked runs.
        """

        if self._session is None:
            raise RuntimeError(
                f'This {type(self).__name__} is detached. Reattach it via '
                'ref = session.get_measurement(ref) before fetching data.'
            )
        return await self._session.get_measurement(self)


class MeasurementJob:
    """
    A job representing an ongoing measurement.
    """

    def __init__(self, guid: str, *, claim: InstrumentClaim):
        self._guid: str = guid
        self._claim: InstrumentClaim = claim

    def __repr__(self):
        return f'{type(self).__name__}(guid={self.guid!r}, serial={self.serial_number!r})'

    @property
    def guid(self):
        """The unique identifier of the measurement being performed."""
        return self._guid

    @property
    def claim(self):
        """The instrument claim associated with the measurement job."""
        return self._guid

    @property
    def serial_number(self):
        """Serial number of the instrument carrying out the measurement."""
        return self._claim._serial

    @property
    def is_finished(self) -> bool:
        """True if the measurement is finished."""
        raise NotImplementedError

    async def result(self) -> MeasurementRef:
        """Wait for the measurement to finish and return measurement reference.

        Returns
        -------
        MeasurementRef
            Reference to the measurement data.
        """
        return MeasurementRef(self.guid, session=self._claim._session)

    def __await__(self):
        return self.result().__await__()

    async def abort(self) -> None:
        """Abort measurement."""
        return await self._claim.abort_measurement()

    async def pause(self) -> None:
        """Pause measurement."""
        return await self._claim.pause_measurement()

    async def resume(self) -> None:
        """Resume measurement."""
        return await self._claim.resume_measurement()
