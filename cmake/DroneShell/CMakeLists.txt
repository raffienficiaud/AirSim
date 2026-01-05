cmake_minimum_required(VERSION 3.5.0)
project(DroneShell)

# LIST(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../cmake-modules") 
# INCLUDE("${CMAKE_CURRENT_LIST_DIR}/../cmake-modules/CommonSetup.cmake")
# CommonSetup()
# 
# IncludeEigen()
# 
# SetupConsoleBuild()
#
#include_directories(
#  ${AIRSIM_ROOT}/DroneShell
#  ${RPC_LIB_INCLUDES}
#  ${AIRSIM_ROOT}/DroneShell/include;
#  ${AIRSIM_ROOT}/AirLib/include
#  ${AIRSIM_ROOT}/MavLinkCom/include
#)
#
#AddExecutableSource()
#			
#CommonTargetLink()
#
add_executable(
  ${PROJECT_NAME} 

  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/linenoise.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/SimpleShell.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/main.cpp
)

target_include_directories(
  ${PROJECT_NAME} 
  PUBLIC
    ${AIRSIM_ROOT}/${PROJECT_NAME}/include
)


target_link_libraries(${PROJECT_NAME} AirLib)
# target_link_libraries(${PROJECT_NAME} ${RPC_LIB})
