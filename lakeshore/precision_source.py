"""Implements functionality unique to the Lake Shore 155 Precision Source"""

from collections import namedtuple
from .xip_instrument import XIPInstrument

operation_register = [
    "",
    "",
    "",
    "",
    "",
    "waiting_for_trigger_event",
    "waiting_for_ARM_event",
    "",
    "",
    "",
    "trigger_model_is_idle",
    "",
    "interlock_is_open"
]

questionable_register = [
    "voltage_source_in_current_limit",
    "current_source_in_voltage_compliance",
    "",
    "",
    "",
    "",
    "",
    "",
    "calibration_error",
    "inter_processor_communication_error"
]

OperationRegister = namedtuple('OperationRegister',
                               [bit_name for bit_name in operation_register if bit_name != ""])

QuestionableRegister = namedtuple('QuestionableRegister',
                                  [bit_name for bit_name in questionable_register if bit_name != ""])


class PrecisionSource(XIPInstrument):
    """A class object representing a Lake Shore 155 precision I/V source"""

    vid_pid = [(0x1FB9, 0x0103)]

    def __init__(self, serial_number=None,
                 com_port=None, baud_rate=115200, flow_control=True,
                 timeout=2.0,
                 ip_address=None):
        # Call the parent init, then fill in values specific to the 155
        XIPInstrument.__init__(self, serial_number, com_port, baud_rate, flow_control, timeout, ip_address)
