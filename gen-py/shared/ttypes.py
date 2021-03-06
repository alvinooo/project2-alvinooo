#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class responseType(object):
    OK = 1
    ERROR = 2

    _VALUES_TO_NAMES = {
        1: "OK",
        2: "ERROR",
    }

    _NAMES_TO_VALUES = {
        "OK": 1,
        "ERROR": 2,
    }


class uploadResponseType(object):
    OK = 1
    MISSING_BLOCKS = 2
    FILE_ALREADY_PRESENT = 3
    ERROR = 4

    _VALUES_TO_NAMES = {
        1: "OK",
        2: "MISSING_BLOCKS",
        3: "FILE_ALREADY_PRESENT",
        4: "ERROR",
    }

    _NAMES_TO_VALUES = {
        "OK": 1,
        "MISSING_BLOCKS": 2,
        "FILE_ALREADY_PRESENT": 3,
        "ERROR": 4,
    }


class response(object):
    """
    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'message', None, None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.message = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('response')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.I32, 1)
            oprot.writeI32(self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class uploadResponse(object):
    """
    Attributes:
     - status
     - hashList
     - blockServerList
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'status', None, None, ),  # 1
        (2, TType.LIST, 'hashList', (TType.STRING, 'UTF8', False), None, ),  # 2
        (3, TType.LIST, 'blockServerList', (TType.LIST, (TType.STRING, 'UTF8', False), False), None, ),  # 3
    )

    def __init__(self, status=None, hashList=None, blockServerList=None,):
        self.status = status
        self.hashList = hashList
        self.blockServerList = blockServerList

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.hashList = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.hashList.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.blockServerList = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = []
                        (_etype15, _size12) = iprot.readListBegin()
                        for _i16 in range(_size12):
                            _elem17 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                            _elem11.append(_elem17)
                        iprot.readListEnd()
                        self.blockServerList.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('uploadResponse')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.hashList is not None:
            oprot.writeFieldBegin('hashList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.hashList))
            for iter18 in self.hashList:
                oprot.writeString(iter18.encode('utf-8') if sys.version_info[0] == 2 else iter18)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.blockServerList is not None:
            oprot.writeFieldBegin('blockServerList', TType.LIST, 3)
            oprot.writeListBegin(TType.LIST, len(self.blockServerList))
            for iter19 in self.blockServerList:
                oprot.writeListBegin(TType.STRING, len(iter19))
                for iter20 in iter19:
                    oprot.writeString(iter20.encode('utf-8') if sys.version_info[0] == 2 else iter20)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class file(object):
    """
    Attributes:
     - filename
     - version
     - hashList
     - status
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'filename', 'UTF8', None, ),  # 1
        (2, TType.I32, 'version', None, None, ),  # 2
        (3, TType.LIST, 'hashList', (TType.STRING, 'UTF8', False), None, ),  # 3
        None,  # 4
        (5, TType.I32, 'status', None, None, ),  # 5
    )

    def __init__(self, filename=None, version=None, hashList=None, status=None,):
        self.filename = filename
        self.version = version
        self.hashList = hashList
        self.status = status

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.filename = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.hashList = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.hashList.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('file')
        if self.filename is not None:
            oprot.writeFieldBegin('filename', TType.STRING, 1)
            oprot.writeString(self.filename.encode('utf-8') if sys.version_info[0] == 2 else self.filename)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I32, 2)
            oprot.writeI32(self.version)
            oprot.writeFieldEnd()
        if self.hashList is not None:
            oprot.writeFieldBegin('hashList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.hashList))
            for iter27 in self.hashList:
                oprot.writeString(iter27.encode('utf-8') if sys.version_info[0] == 2 else iter27)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 5)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
