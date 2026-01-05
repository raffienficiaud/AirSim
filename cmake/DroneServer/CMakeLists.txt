cmake_minimum_required(VERSION 3.5.0)
project(DroneServer)

#LIST(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../cmake-modules") 
#INCLUDE("${CMAKE_CURRENT_LIST_DIR}/../cmake-modules/CommonSetup.cmake")
#CommonSetup()
#
#IncludeEigen()
#
#SetupConsoleBuild()
#
#include_directories(
#  ${AIRSIM_ROOT}/DroneServer
#  ${AIRSIM_ROOT}/MavLinkCom/include
#  ${RPC_LIB_INCLUDES}
#  ${AIRSIM_ROOT}/AirLib/include
#)
#
#AddExecutableSource()
#			
#CommonTargetLink()
#
add_executable(
  ${PROJECT_NAME} 
  ${AIRSIM_ROOT}/${PROJECT_NAME}/main.cpp
)

target_include_directories(
  ${PROJECT_NAME} 
  PUBLIC
    ${AIRSIM_ROOT}/MavLinkCom/include # needed ??
)


target_link_libraries(${PROJECT_NAME} AirLib MavLinkCom)


#target_link_libraries(${PROJECT_NAME} AirLib)
#target_link_libraries(${PROJECT_NAME} MavLinkCom)
#target_link_libraries(${PROJECT_NAME} ${RPC_LIB})
