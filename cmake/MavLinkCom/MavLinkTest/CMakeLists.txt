project(MavLinkTest)

#LIST(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../cmake-modules") 
#INCLUDE("${CMAKE_CURRENT_LIST_DIR}/../../cmake-modules/CommonSetup.cmake")
#CommonSetup()

#SetupConsoleBuild()

find_package(Threads)

set(_mavlinktest_source_dir "${AIRSIM_ROOT}/MavLinkCom/MavLinkTest")

# include_directories(
#   ${AIRSIM_ROOT}/MavLinkCom/MavLinkTest
#   ${AIRSIM_ROOT}/MavLinkCom/include
#   ${AIRSIM_ROOT}/MavLinkCom/common_utils
# )

set(_mavlink_test_SRC
  ${_mavlinktest_source_dir}/Commands.cpp
  ${_mavlinktest_source_dir}/Commands.h
  ${_mavlinktest_source_dir}/ConsoleBase.h
  
  ${_mavlinktest_source_dir}/UnitTests.h
  ${_mavlinktest_source_dir}/UnitTests.cpp
  
  ${_mavlinktest_source_dir}/main.cpp
)
#file(GLOB_RECURSE PROJECT_CPP "${AIRSIM_ROOT}/MavLinkCom/${PROJECT_NAME}/*.cpp")

add_executable(
  MavLinkTest
  ${_mavlink_test_SRC}
)
target_include_directories(
  MavLinkTest
  PUBLIC
    ${AIRSIM_ROOT}/MavLinkCom/MavLinkTest/
)
  
target_link_libraries(
  MavLinkTest
  PUBLIC
    MavLinkCom
    Threads::Threads
    #${CXX_EXP_LIB}
)
