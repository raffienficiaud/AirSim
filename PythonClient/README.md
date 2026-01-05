# Python API for AirSim

This package contains Python APIs for [AirSim](https://github.com/microsoft/airsim).

## How to Use
See examples at [car/hello_car.py](https://github.com/Microsoft/AirSim/blob/main/PythonClient/car/hello_car.py) or [multirotor/hello_drone.py](https://github.com/microsoft/AirSim/blob/main/PythonClient/multirotor/hello_drone.py).

## Dependencies
This package depends on `msgpack` and would automatically install `msgpack-rpc-python` (this may need administrator/sudo prompt):
```
pip install msgpack-rpc-python
```

Some examples also requires opencv.

## More Info

More information on AirSim Python APIs can be found at:
https://github.com/Microsoft/AirSim/blob/main/docs/python.md


# Install local development version

```bash
SETUPTOOLS_SCM_PRETEND_VERSION=0.1-dev pip install -e .
```

Install the necessary for reinforcement learning
```bash
pip install --group rl
```


# Run the environment

1. The binary is inside the packaged .app file
1. the following command line runs unattended and offscreen
1. additional settings can be passed from command line, such as the API port and the multirotor setting.
   That way several instances can be run in parallel.

```bash
/Volumes/user-data/code/perso/AirSim/Unreal/Environments/BlocksV2/Binaries/Mac/BlocksV2.app/Contents/MacOS/BlocksV2 \
    -RenderOffscreen \
    -unattended \
    -settings='{"SimMode":"Multirotor","ApiServerPort":41452}'
```


