from struct import pack
from struct import unpack
from struct import calcsize as sizeof
from struct import error

CONNECT_TO_CAR = 1
MOVE_CAR = 2
GET_MALUS = 3
SEND_MALUS = 4

FORWARD = 10
BACKWARD = 11
LEFT = 12
RIGHT = 13


def create_packet(op_code, data):
    return pack("!I{}s".format(len(data)), op_code, data.encode())

def process_packet(packet):
    try:
        return unpack("!I{}s".format(len(packet)-sizeof("!I")), packet)

    except error as e:
        print("Packet Format Error : {}".format(packet))
        return None, None
