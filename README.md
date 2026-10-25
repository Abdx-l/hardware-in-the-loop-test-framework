# Hardware-in-the-Loop Test Framework

C shared-library device emulator and typed ctypes wrapper with register bounds, busy ticks, deterministic faults, and SQLite-backed test outcomes.

## Run

On Linux: `cc -shared -fPIC device.c -o libdevice.so`, then install requirements.txt and run `pytest --junitxml=results.xml`. Set DEVICE_LIBRARY to a custom library path.
