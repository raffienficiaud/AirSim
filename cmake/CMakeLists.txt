cmake_minimum_required(VERSION 3.21.0)
project(AirSim)

enable_testing()

set(AIRSIM_ROOT "${CMAKE_CURRENT_LIST_DIR}/..")
file(REAL_PATH "${AIRSIM_ROOT}" AIRSIM_ROOT)

if(NOT EXISTS "${AIRSIM_ROOT}")
    message(FATAL_ERROR "Cannot find AIRSIM_ROOT at location '${AIRSIM_ROOT}'")
endif()

set(PLUGIN_INSTALL_FOLDER "Plugins/AirSim")

add_subdirectory("rpclib_wrapper")
add_subdirectory("AirLib")
add_subdirectory("MavLinkCom")
add_subdirectory("AirLibUnitTests")
add_subdirectory("HelloDrone")
add_subdirectory("HelloSpawnedDrones")
add_subdirectory("HelloCar")
add_subdirectory("DroneShell")
add_subdirectory("DroneServer")
