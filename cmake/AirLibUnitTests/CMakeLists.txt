project(AirLibUnitTests)

if(FALSE)
LIST(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../cmake-modules") 
INCLUDE("${CMAKE_CURRENT_LIST_DIR}/../cmake-modules/CommonSetup.cmake")
CommonSetup()

IncludeEigen()
endif()

find_package(Eigen3)


# SetupConsoleBuild()

include_directories(
  ${AIRSIM_ROOT}/AirLibUnitTests
  ${AIRSIM_ROOT}/AirLib/include
  ${AIRSIM_ROOT}/MavLinkCom/include
)

#AddExecutableSource()

set(PROJECT_CPP ${PROJECT_NAME}_sources)
file(GLOB_RECURSE 
  ${PROJECT_CPP} 
  "${AIRSIM_ROOT}/${PROJECT_NAME}/*.[ch]pp")
add_executable(${PROJECT_NAME} ${${PROJECT_CPP}})

#CommonTargetLink()
target_link_libraries(
  ${PROJECT_NAME} 
  PUBLIC 
    AirLib
    #MavLinkCom
    #rpclib::rpc
    #Threads::Threads
)

add_test(
  NAME 
    ${PROJECT_NAME} 
  COMMAND
    ${PROJECT_NAME}
)