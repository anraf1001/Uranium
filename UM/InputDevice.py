# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from UM.Signal import Signal, SignalEmitter
from UM.PluginObject import PluginObject


##  Abstract base class for all input devices (HMI devices)
#   Examples of this are mouse & keyboard
class InputDevice(PluginObject, SignalEmitter):
    def __init__(self):
        super().__init__()

    ##  Emitted whenever the device produces an event.
    #   All actions performed with the device should be seen as an event.
    #   \param event The event that is emitted.
    event = Signal()
