from __future__ import annotations

import asyncio
import warnings
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import PalmSens
import System
from typing_extensions import override

if TYPE_CHECKING:
    from PalmSens.Devices import Device as PSDevice

import sys
from typing import TYPE_CHECKING, Any

from .shared import create_future

WINDOWS = sys.platform == 'win32'
LINUX = not WINDOWS

if WINDOWS:
    from PalmSens.Windows.Devices import (
        BLEDevice,
        BluetoothDevice,
        FTDIDevice,
        SerialPortDevice,
        USBCDCDevice,
        WinUSBDevice,
    )
else:
    from PalmSens.Core.Linux.Comm.Devices import FTDIDevice, SerialPortDevice


if TYPE_CHECKING:
    pass


warnings.simplefilter('default')


async def discover_async(
    ftdi: bool = True,
    usbcdc: bool = True,
    winusb: bool = True,
    bluetooth: bool = False,
    serial: bool = True,
    ignore_errors: bool = False,
) -> list[Instrument]:
    """Discover instruments.

    For a list of device interfaces, see:
        https://dev.palmsens.com/python/latest/_attachments/installation/index.html#compatibility

    Parameters
    ----------
    ftdi : bool
        If True, discover ftdi devices
    usbcdc : bool
        If True, discover usbcdc devices (Windows only)
    winusb : bool
        If True, discover winusb devices (Windows only)
    bluetooth : bool
        If True, discover bluetooth devices (Windows only)
    serial : bool
        If True, discover serial devices
    ignore_errors : False
        Ignores errors in device discovery

    Returns
    -------
    discovered : list[Instrument]
        List of dataclasses with discovered instruments.
    """
    interfaces: dict[str, Any] = {}

    if ftdi:
        interfaces['ftdi'] = FTDIDevice

    if WINDOWS:
        if usbcdc:
            interfaces['usbcdc'] = USBCDCDevice

        if winusb:
            interfaces['winusb'] = WinUSBDevice

        if bluetooth:
            interfaces['bluetooth'] = BluetoothDevice
            interfaces['ble'] = BLEDevice

    if LINUX:
        if serial:
            interfaces['serial'] = SerialPortDevice

    instruments: list[Instrument] = []

    for name, interface in interfaces.items():
        try:
            devices: list[PalmSens.Devices.Device] = await create_future(
                interface.DiscoverDevicesAsync()
            )
        except System.DllNotFoundException:
            if ignore_errors:
                continue

            if name == 'ftdi':
                msg = (
                    'Cannot discover FTDI devices (missing driver).'
                    '\nfor more information see: '
                    'https://dev.palmsens.com/python/latest/_attachments/installation/index.html#ftdisetup'
                    '\nSet `ftdi=False` to hide this message.'
                )
                warnings.warn(msg, stacklevel=2)
                continue
            raise

        for device in devices:
            instruments.append(
                Instrument(
                    id=device.ToString(),
                    interface=name,
                    device=device,
                )
            )

    instruments.sort(key=lambda instrument: instrument.id)

    return instruments


def discover(
    ftdi: bool = True,
    usbcdc: bool = True,
    winusb: bool = True,
    bluetooth: bool = False,
    serial: bool = True,
    ignore_errors: bool = False,
) -> list[Instrument]:
    """Discover instruments.

    For a list of device interfaces, see:
        https://dev.palmsens.com/python/latest/_attachments/installation/index.html#compatibility

    Parameters
    ----------
    ftdi : bool
        If True, discover ftdi devices
    usbcdc : bool
        If True, discover usbcdc devices (Windows only)
    winusb : bool
        If True, discover winusb devices (Windows only)
    bluetooth : bool
        If True, discover bluetooth devices (Windows only)
    serial : bool
        If True, discover serial devices
    ignore_errors : False
        Ignores errors in device discovery

    Returns
    -------
    discovered : list[Instrument]
        List of dataclasses with discovered instruments.
    """
    return asyncio.run(
        discover_async(
            ftdi=ftdi,
            usbcdc=usbcdc,
            winusb=winusb,
            bluetooth=bluetooth,
            serial=serial,
            ignore_errors=ignore_errors,
        )
    )


@dataclass
class Instrument:
    """Dataclass holding instrument info."""

    id: str = field(repr=False)
    """Device ID of the instrument."""
    name: str = field(init=False)
    """Name of the instrument."""
    channel: int = field(init=False, default=-1)
    """Channel index if part of a multichannel device.

    Returns -1 if instrument is not part of a multi-channel device."""
    interface: str
    """Type of the connection."""
    device: PSDevice = field(repr=False)
    """Device connection class."""

    def __post_init__(self):
        try:
            idx = self.id.index('CH')
        except ValueError:
            self.name = self.id
        else:
            ch_str = self.id[idx : idx + 5]
            self.channel = int(ch_str[2:])
            self.name = self.id[:idx]

    @classmethod
    def from_port(cls, port: str, *, baudrate: int | None = None) -> Instrument:
        """Create serial port instrument class.

        Parameters
        ----------
        port : str
            Name of the port to connect to
        baudrate : int, optional
            Set the baudrate. If None, use the default baudrate.

        Returns
        -------
        instrument : Instrument
            Instrument dataclass
        """

        if baudrate is None:
            device = SerialPortDevice(port)
        else:
            device = SerialPortDevice(port, baudrate=baudrate)

        instrument = cls(
            id=device.ToString(),
            interface='serial',
            device=device,
        )
        return instrument

    @override
    def __repr__(self):
        args = ''.join(
            (
                f'name={self.name!r}, ',
                f'channel={self.channel}, ' if self.channel > 0 else '',
                f'interface={self.interface!r}',
            )
        )

        return f'{self.__class__.__name__}({args})'

    @property
    def baudrate(self) -> int:
        """Baud rate."""
        return self.device.baudrate
