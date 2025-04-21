"""Constants for the Renogy BLE integration."""

import logging
from enum import Enum

DOMAIN = "renogy"

LOGGER = logging.getLogger(__name__)

# BLE scanning constants
DEFAULT_SCAN_INTERVAL = 60  # seconds
MIN_SCAN_INTERVAL = 10  # seconds
MAX_SCAN_INTERVAL = 600  # seconds

# Renogy BT-1 and BT-2 module identifiers - devices advertise with these prefixes
#RENOGY_BT_PREFIX = "BT-TH-"

# Renogy smart shunt identifier identify with this prefix
RENOGY_BT_PREFIX = "RTMShunt"

# Configuration parameters
CONF_SCAN_INTERVAL = "scan_interval"
CONF_DEVICE_TYPE = "device_type"  # New constant for device type

# Device info
ATTR_MANUFACTURER = "Renogy"


# Define device types as Enum
class DeviceType(Enum):
    CONTROLLER = "controller"
    BATTERY = "battery"
    INVERTER = "inverter"
    SHUNT = "shunt"

# List of supported device types
DEVICE_TYPES = [e.value for e in DeviceType]
DEFAULT_DEVICE_TYPE = DeviceType.CONTROLLER.value

# List of fully supported device types (currently only controller)
SUPPORTED_DEVICE_TYPES = [DeviceType.CONTROLLER.value, DeviceType.SHUNT.value]

# BLE Characteristics and Service UUIDs
RENOGY_READ_CHAR_UUID = (
    "0000fff1-0000-1000-8000-00805f9b34fb"  # Characteristic for reading data
)
RENOGY_WRITE_CHAR_UUID = (
    "0000ffd1-0000-1000-8000-00805f9b34fb"  # Characteristic for writing commands
)

# Time in minutes to wait before attempting to reconnect to unavailable devices
UNAVAILABLE_RETRY_INTERVAL = 10

# Maximum time to wait for a notification response (seconds)
MAX_NOTIFICATION_WAIT_TIME = 2.0

# Default device ID for Renogy devices
DEFAULT_DEVICE_ID = 0xFF

# Modbus commands for requesting data
COMMANDS = {
    DeviceType.CONTROLLER.value: {
        "device_info": (3, 12, 8),
        "device_id": (3, 26, 1),
        "battery": (3, 57348, 1),
        "pv": (3, 256, 34),
    },
        DeviceType.SHUNT.value: {
        "shunt_info": (3, 256, 110),
    },
}
