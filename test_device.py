import sqlite3,pytest
from device import Device
@pytest.fixture
def device():
 d=Device();yield d;d.close()
@pytest.mark.parametrize("address",[0,7,15])
def test_roundtrip(device,address):
 device.write(address,0xffffffff);device.wait();assert device.read(address)==0xffffffff
def test_bounds(device):
 with pytest.raises(ValueError):device.write(16,0)
def test_faults(device):
 device.lib.device_fault(1)
 with pytest.raises(ValueError):device.write(0,4)
 device.lib.device_fault(3);device.lib.device_reset();device.lib.device_fault(0);device.write(0,4);device.lib.device_fault(3)
 with pytest.raises(TimeoutError):device.wait()
 device.lib.device_fault(0);device.wait()
