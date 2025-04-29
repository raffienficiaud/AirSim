project(AirLib)

#LIST(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../cmake-modules")
#INCLUDE("${CMAKE_CURRENT_LIST_DIR}/../cmake-modules/CommonSetup.cmake")
#CommonSetup()

find_package(Eigen3)
find_package(Threads)
find_package(rpclib)
#IncludeEigen()

include_directories(
  ${AIRSIM_ROOT}/AirLib/
  ${AIRSIM_ROOT}/AirLib/include
  ${AIRSIM_ROOT}/MavLinkCom/include
  #${RPC_LIB_INCLUDES}
)

set(_list_glob)
foreach(_subfolder "api" "common" "physics" "safety" "sensors" "vehicles")
  list(APPEND _list_glob "${AIRSIM_ROOT}/${PROJECT_NAME}/include/${_subfolder}/*.hpp")
  list(APPEND _list_glob "${AIRSIM_ROOT}/${PROJECT_NAME}/src/${_subfolder}/*.cpp")
endforeach()

file(GLOB_RECURSE
  ${PROJECT_NAME}_sources
  ${_list_glob}
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/api/*.hpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/api/*.cpp
#
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/common/*.hpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/common/*.cpp
#
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/common/common_utils/*.cpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/common/common_utils/*.cpp
#
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/safety/*.hpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/safety/*.cpp
#
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/vehicles/car/api/*.hpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/vehicles/car/api/*.cpp
#
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/vehicles/multirotor/*.hpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/vehicles/multirotor/*.cpp
#
  #${AIRSIM_ROOT}/${PROJECT_NAME}/include/vehicles/multirotor/api/*.hpp
  #${AIRSIM_ROOT}/${PROJECT_NAME}/src/vehicles/multirotor/api/*.cpp
)

add_library(
  ${PROJECT_NAME}
  STATIC
  ${${PROJECT_NAME}_sources}
)

target_link_libraries(
  ${PROJECT_NAME}
  PUBLIC
    MavLinkCom
    Threads::Threads
    Eigen3::Eigen
    rpclib::rpc
)


set(_src_code_install_location "Plugins/AirSim")
install(
  DIRECTORY
    "${AIRSIM_ROOT}/Unreal/Plugins/AirSim/"
  COMPONENT
    AirSimUnreal
  DESTINATION
    "${_src_code_install_location}"
)

foreach(_file IN LISTS ${PROJECT_NAME}_sources)
  get_filename_component(_file_ext "${_file}" EXT)
  if("${_file_ext}" MATCHES "\\.h.*")
    get_filename_component(_current_folder "${_file}" DIRECTORY)
    file(RELATIVE_PATH _current_folder "${AIRSIM_ROOT}/${PROJECT_NAME}/include/" "${_current_folder}")
    # message(STATUS "${_file} installed to ${_src_code_install_location}/Source/include/${_current_folder}")
    install(
      FILES
        "${_file}"
      COMPONENT
        AirSimUnreal
      DESTINATION
        "${_src_code_install_location}/Source/AirLib/include/${_current_folder}"
    )
  endif()
endforeach()


install(
  TARGETS
    ${PROJECT_NAME}
  COMPONENT
    AirSimUnreal
  DESTINATION
    "${_src_code_install_location}/Source/AirLib/lib/x64/"
  #FILE_SET 
  #  HEADERS DESTINATION "coucou"    
  #PUBLIC_HEADER 
  #  DESTINATION deps# COMPONENT Development
)

get_property(importTargets DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}" PROPERTY IMPORTED_TARGETS)
message(STATUS "coucou ${importTargets}")

# install(
#   IMPORTED_RUNTIME_ARTIFACTS ${importTargets}
#   LIBRARY
#     DESTINATION
#       "${_src_code_install_location}/Source/AirLib/deps"
#     COMPONENT
#       AirSimUnreal
#         
# )
# 
get_target_property(_eigen_include Eigen3::Eigen INTERFACE_INCLUDE_DIRECTORIES)
message(STATUS "Eigen3::Eigen ${_eigen_include}")

get_target_property(_rpclib_include rpclib::rpc INTERFACE_INCLUDE_DIRECTORIES)
message(STATUS "rpclib::rpc ${_rpclib_include}")

get_target_property(_rpclib_dir rpclib::rpc INTERFACE_LINK_DIRECTORIES)
message(STATUS "rpclib::rpc-dir ${_rpclib_dir}")

install(
  DIRECTORY
    ${_eigen_include}
  COMPONENT
    AirSimUnreal
  DESTINATION
    "${_src_code_install_location}/Source/AirLib/deps"
  #FILE_SET 
  #  HEADERS DESTINATION "coucou"    
  #PUBLIC_HEADER 
  #  DESTINATION deps# COMPONENT Development
)

install(
  DIRECTORY
    ${_rpclib_include}
  COMPONENT
    AirSimUnreal
  DESTINATION
    "${_src_code_install_location}/Source/AirLib/deps/rpclib"
  #FILE_SET 
  #  HEADERS DESTINATION "coucou"    
  #PUBLIC_HEADER 
  #  DESTINATION deps# COMPONENT Development
)

install(
  DIRECTORY
    ${_rpclib_dir}
  COMPONENT
    AirSimUnreal
  DESTINATION
    "${_src_code_install_location}/Source/AirLib/deps/rpclib"
  #FILE_SET 
  #  HEADERS DESTINATION "coucou"    
  #PUBLIC_HEADER 
  #  DESTINATION deps# COMPONENT Development
)

install(
  SCRIPT ./install_script.cmake
  COMPONENT
    AirSimUnreal
)

#target_link_libraries(${PROJECT_NAME} MavLinkCom)
#target_link_libraries(${PROJECT_NAME} ${CMAKE_THREAD_LIBS_INIT})

#string(SUBSTRING ${CMAKE_STATIC_LINKER_FLAGS} 9 -1 "BUILD_PLATFORM")
#find_package(Threads REQUIRED)
#target_link_libraries(${PROJECT_NAME} ${CMAKE_THREAD_LIBS_INIT})
#target_link_libraries(${PROJECT_NAME} AirLib)
#target_link_libraries(${PROJECT_NAME} MavLinkCom)
#target_link_libraries(${PROJECT_NAME} ../AirLib/deps/rpclib/lib/${BUILD_PLATFORM}/$(Configuration)/rpc)
