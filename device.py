import ctypes,os
class Device:
 def __init__(self,path=None):
  self.lib=ctypes.CDLL(path or os.getenv("DEVICE_LIBRARY","./libdevice.so"))
  self.lib.device_write.argtypes=[ctypes.c_int,ctypes.c_uint32]
  self.lib.device_read.argtypes=[ctypes.c_int,ctypes.POINTER(ctypes.c_uint32)]
  self.lib.device_fault.argtypes=[ctypes.c_int]
  self.lib.device_open()
 def write(self,address,value):
  result=self.lib.device_write(address,value)
  if result:raise ValueError(f"device error {result}")
 def read(self,address):
  value=ctypes.c_uint32();result=self.lib.device_read(address,ctypes.byref(value))
  if result:raise ValueError(f"device error {result}")
  return value.value
 def wait(self,limit=10):
  for _ in range(limit):
   if self.lib.device_tick()==0:return
  raise TimeoutError("device remained busy")
 def close(self):self.lib.device_close()
