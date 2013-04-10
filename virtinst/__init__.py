#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free  Software Foundation; either version 2 of the License, or
# (at your option)  any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA.

from virtcli import cliconfig, cliutils
enable_rhel6_defaults = not cliconfig.rhel_enable_unsupported_opts
cliutils.setup_i18n()


# Public imports

import Storage
import Interface
from Guest import Guest
from VirtualDevice import VirtualDevice
from VirtualNetworkInterface import VirtualNetworkInterface
from VirtualGraphics import VirtualGraphics
from VirtualAudio import VirtualAudio
from VirtualInputDevice import VirtualInputDevice
from VirtualDisk import VirtualDisk
from VirtualHostDevice import (VirtualHostDevice, VirtualHostDeviceUSB,
                               VirtualHostDevicePCI)
from VirtualCharDevice import VirtualCharDevice
from VirtualVideoDevice import VirtualVideoDevice
from VirtualController import VirtualController
from VirtualWatchdog import VirtualWatchdog
from VirtualFilesystem import VirtualFilesystem
from VirtualSmartCardDevice import VirtualSmartCardDevice
from VirtualRedirDevice import VirtualRedirDevice
from VirtualMemballoon import VirtualMemballoon
from FullVirtGuest import FullVirtGuest
from ParaVirtGuest import ParaVirtGuest
from DistroInstaller import DistroInstaller
from PXEInstaller import PXEInstaller
from LiveCDInstaller import LiveCDInstaller
from ImportInstaller import ImportInstaller
from ImageInstaller import ImageInstaller
from Installer import ContainerInstaller
from CloneManager import CloneDesign
from User import User
from Clock import Clock
from CPU import CPU, CPUFeature
from Seclabel import Seclabel
from XMLBuilderDomain import XMLBuilderDomain
import util
import support