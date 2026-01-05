# Welcome to Colosseum, a successor of [AirSim](https://github.com/microsoft/AirSim)

## Build Status
[![Ubuntu Build](https://github.com/CodexLabsLLC/Colosseum/actions/workflows/test_ubuntu.yml/badge.svg)](https://github.com/CodexLabsLLC/Colosseum/actions/workflows/test_ubuntu.yml)
[![MacOS Build](https://github.com/CodexLabsLLC/Colosseum/actions/workflows/test_macos.yml/badge.svg)](https://github.com/CodexLabsLLC/Colosseum/actions/workflows/test_macos.yml)
[![Windows Build](https://github.com/CodexLabsLLC/Colosseum/actions/workflows/test_windows.yml/badge.svg)](https://github.com/CodexLabsLLC/Colosseum/actions/workflows/test_windows.yml)

[![](https://dcbadge.vercel.app/api/server/y9ZJKKKn8J)](https://discord.gg/y9ZJKKKn8J)

# Airsim simplified
The original build/installation instructions of Airsim are way too complicated. This fork
aims at simplifying the build of Airsim and the injection of the plugin into your Unreal environment.


## Build steps
The steps are as follows:

1. install the tools needed for generating the dependencies. This is simple: a python package called `conan` will
   be used for this
1. checkout the `conan` recipes repository that contain the "recipes": the `conan` recipes are small scripts
   that define rules for building C/C++ packages. The `conan` community has already done an incredible work
   for providing the packages we need in Airim as simple recipes.
1. configure the dependencies of Airsim and build those with `conan`
1. configure Airsim `cmake` environment to use the conan built packages and build Airsim.

This sounds a bit involved, but this is actually very simple.

### Configure `conan`

```bash
# create a python virtual environment and install conan: this does not need to be shared with anything else
# as it will be used only for conan
python3 -m venv .venv_build
. .venv_build/bin/activate

# install conan
pip install -U pip wheel
pip install conan

# convenience variable
export BASE_FOLDER=`pwd`

# this folder will contain the conan-center-index: a repository that contains all the "recipes"
# we need for building our dependencies
export CONAN_CENTER_INDEX_SRC=$BASE_FOLDER/../conan-center-index

# this variable indicates the location where conan will be storing the build profiles, recipes
# and built dependencies
export CONAN_HOME=$BASE_FOLDER/.conan

# checkout the conan repository containing the "recipes"
git clone git@github.com:conan-io/conan-center-index.git $CONAN_CENTER_INDEX_SRC

# initialize conan profile, requires $CONAN_HOME to be defined **first**
conan profile detect
```

### Configure and build Airsim

```bash
# this will be our build folder
mkdir $BASE_FOLDER/build

# this little script declares the conan packages we need for building Airsim
./external_libraries/prepare_conan_clang.sh

# TODO --profile=${profile_name} \
cd $BASE_FOLDER/build

#
# build the conan dependencies:
#

# for Linux:
conan install \
  --output-folder . \
  --build=missing \
  -s build_type=Release ..

# for macOS/Xcode, multiconfiguration build makes it easier
conan install \
  --output-folder . \
  --build=missing \
  -s build_type=Release \
  -s "&:build_type=Debug" \
  -c tools.cmake.cmaketoolchain:generator=Xcode \
  ..

#
# Configure and build Airsim
#

# for linux:
cmake \
  -DCMAKE_TOOLCHAIN_FILE=./conan_toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Release \
  --fresh \
  ../cmake
make -j

# for macOS/Xcode:
cmake -G Xcode \
  -DCMAKE_TOOLCHAIN_FILE=./conan_toolchain.cmake \
  --fresh \
  ../cmake
# then open and build the project using your IDE
open Airsim.project
```

### Install the plugin into your Unreal environment

Little cherry on top of the previous steps: the following installs the generated binaries into
your Unreal environment. It modifies accordingly your Unreal project and performs the necessary copies.

```bash
# after the build: this will create the AirSim
# plugin folder inside the Unreal project folder
# pointed by $BASE_FOLDER/Unreal/Environments/BlocksV2
# This can be any path containing a .uproject
cmake \
  --install . \
  --config Debug \
  --prefix $BASE_FOLDER/Unreal/Environments/BlocksV2
```

# Running the RL stuff

```bash
cd PythonClient
pip install -e .

# needed by airsim
pip install msgpack-rpc-python 

# optional
# opencv-contrib-python 
pip install torch torchrl torchvision "gymnasium[classic_control]"

# to fix: installation of "gymnasium[box2d]"

cd ./reinforcement_learning
PYTHONPATH=`pwd`/..:$PYTHONPATH python dqn_drone_raffi.py
```


## Looking for more performance?
The company managing this repo created the SWARM Developer System to help build, simulate and deploy single and
multi-agent autonomous systems. Check it out here: [SWARM Developer System](https://www.swarmsim.io/overview/developer)

## IMPORTANT ANNOUNCEMENT
Moving forward, we are now using Unreal Engine 5 version 5.03 or greater! If you
want to use UE4.27, you can use the branch `ue4.27`.

## Unreal Engine Version for Main Branch
The main branch of this repository **only** supports Unreal Engine 5.2! Please see our other branches
for other versions that we support.

## Currently Supported Operating Systems
Below are the list of officially supported Operating Systems, with full Unreal Engine support:
### Windows
- Windows 10 (Latest)

### Linux
- ~~Ubuntu 18.04~~ (NO LONGER SUPPORTED. 18.04 is EOL so we will not be checking this anymore and GitHub doesn't support CI builds)
- Ubuntu 20.04

**NOTE** Ubuntu 22.04 is not currently supported due to Vulkan support. If this changes, we will notify you here. If you want to use Colosseum on 22.04, we highly recommend that you use Docker.

### MacOS (Non-M1 Macs only)
- MacOS Monterey (12)
- MacOS (11)

**NOTE** MacOS support is highly experimental and may be dropped in future releases. This is because Apple continually changes their build tools and doesn't like 3rd party developers in general. There are ongoing discussions to remove this support.

## Sponsors
1. Codex Laboratories LLC [Website](https://www.codex-labs-llc.com)

## Introduction

Colosseum is a simulator for robotic, autonomous systems, built on [Unreal Engine](https://www.unrealengine.com/) (we now also have an experimental [Unity](https://unity3d.com/) release). It is open-source, cross platform, and supports software-in-the-loop simulation with popular flight controllers such as PX4 & ArduPilot and hardware-in-loop with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. Similarly, we have an experimental release for a Unity plugin.

This is a fork of the AirSim repository, which Microsoft decided to shutdown in July of 2022. This fork serves as a waypoint to building a new and better simulation platform. The creater and maintainer of this fork is Codex Laboratories LLC (our website is [here](https://www.codex-labs-llc.com)). Colosseum is one of the underlying simulation systems that we use in our product, the [SWARM Simulation Platform](https://www.swarmsim.io). This platform exists to provide pre-built tools and low-code/no-code autonomy solutions. Please feel free to check this platform out and reach out if interested.

## Join the Community
We have decided to create a Discord channel to better allow for community engagement. Join here: [Colosseum Robotics Discord](https://discord.gg/y9ZJKKKn8J).


## Goals and Project Development
This section will contain a list of the current features that the community and Codex Labs are working on to support and build.

Click [here](https://docs.google.com/document/d/1doohQTos4v1tg4Wv6SliQFnKNK1MouKX2efg2mapXFU/edit?usp=sharing) to view our current development goals!

If you want to be apart of the official development team, attend meetings, etc., please utilize the Slack channel (link above) and
let Tyler Fedrizzi know!

## License

This project is released under the MIT License. Please review the [License file](LICENSE) for more details.


