project(MavLinkCom)

find_package(Threads)

add_subdirectory("MavLinkTest")

#LIST(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/../cmake-modules") 
#INCLUDE("${CMAKE_CURRENT_LIST_DIR}/../cmake-modules/CommonSetup.cmake")
#CommonSetup()

include_directories(
  ${AIRSIM_ROOT}/MavLinkCom
  ${AIRSIM_ROOT}/MavLinkCom/common_utils
  ${AIRSIM_ROOT}/MavLinkCom/include
)

set(_mavlink_source_dir "${AIRSIM_ROOT}/MavLinkCom/")

set(_mavlink_sources
  "${_mavlink_source_dir}/common_utils/EnumFlags.hpp"
  "${_mavlink_source_dir}/common_utils/ExceptionUtils.hpp"
  "${_mavlink_source_dir}/common_utils/FileSystem.hpp"
  "${_mavlink_source_dir}/common_utils/StrictMode.hpp"
  "${_mavlink_source_dir}/common_utils/ThreadUtils.hpp"
  "${_mavlink_source_dir}/common_utils/Utils.hpp"
  "${_mavlink_source_dir}/common_utils/json.hpp"
  "${_mavlink_source_dir}/common_utils/optional.hpp"
  "${_mavlink_source_dir}/common_utils/prettyprint.hpp"
  "${_mavlink_source_dir}/common_utils/sincos.hpp"
  "${_mavlink_source_dir}/common_utils/type_utils.hpp"
  "${_mavlink_source_dir}/common_utils/FileSystem.cpp"
  "${_mavlink_source_dir}/common_utils/ThreadUtils.cpp"

  "${_mavlink_source_dir}/include/AdHocConnection.hpp"
  "${_mavlink_source_dir}/include/AsyncResult.hpp"
  "${_mavlink_source_dir}/include/MavLinkConnection.hpp"
  "${_mavlink_source_dir}/include/MavLinkDebugLog.hpp"
  "${_mavlink_source_dir}/include/MavLinkFtpClient.hpp"
  "${_mavlink_source_dir}/include/MavLinkLog.hpp"
  "${_mavlink_source_dir}/include/MavLinkMessageBase.hpp"
  "${_mavlink_source_dir}/include/MavLinkMessages.hpp"
  "${_mavlink_source_dir}/include/MavLinkNode.hpp"
  "${_mavlink_source_dir}/include/MavLinkTcpServer.hpp"
  "${_mavlink_source_dir}/include/MavLinkVehicle.hpp"
  "${_mavlink_source_dir}/include/MavLinkVideoStream.hpp"
  "${_mavlink_source_dir}/include/Semaphore.hpp"
  "${_mavlink_source_dir}/include/UdpSocket.hpp"
  "${_mavlink_source_dir}/include/VehicleState.hpp"

  "${_mavlink_source_dir}/src/AdHocConnection.cpp"
  "${_mavlink_source_dir}/src/MavLinkConnection.cpp"
  "${_mavlink_source_dir}/src/MavLinkFtpClient.cpp"
  "${_mavlink_source_dir}/src/MavLinkLog.cpp"
  "${_mavlink_source_dir}/src/MavLinkMessageBase.cpp"
  "${_mavlink_source_dir}/src/MavLinkMessages.cpp"
  "${_mavlink_source_dir}/src/MavLinkNode.cpp"
  "${_mavlink_source_dir}/src/MavLinkTcpServer.cpp"
  "${_mavlink_source_dir}/src/MavLinkVehicle.cpp"
  "${_mavlink_source_dir}/src/MavLinkVideoStream.cpp"
  "${_mavlink_source_dir}/src/Semaphore.cpp"
  "${_mavlink_source_dir}/src/UdpSocket.cpp"
  "${_mavlink_source_dir}/src/impl/AdHocConnectionImpl.cpp"
  "${_mavlink_source_dir}/src/impl/MavLinkConnectionImpl.cpp"
  "${_mavlink_source_dir}/src/impl/MavLinkFtpClientImpl.cpp"
  "${_mavlink_source_dir}/src/impl/MavLinkNodeImpl.cpp"
  "${_mavlink_source_dir}/src/impl/MavLinkTcpServerImpl.cpp"
  "${_mavlink_source_dir}/src/impl/MavLinkVehicleImpl.cpp"
  "${_mavlink_source_dir}/src/impl/MavLinkVideoStreamImpl.cpp"
  "${_mavlink_source_dir}/src/impl/UdpSocketImpl.cpp"
  "${_mavlink_source_dir}/src/serial_com/SerialPort.cpp"
  "${_mavlink_source_dir}/src/serial_com/TcpClientPort.cpp"
  "${_mavlink_source_dir}/src/serial_com/UdpClientPort.cpp"
  "${_mavlink_source_dir}/src/serial_com/SocketInit.cpp"
  "${_mavlink_source_dir}/src/serial_com/wifi.cpp"
)

if(UNIX)
    list(APPEND _mavlink_sources "${AIRSIM_ROOT}/MavLinkCom/src/impl/linux/MavLinkFindSerialPorts.cpp")
else()
    list(APPEND _mavlink_sources "${AIRSIM_ROOT}/MavLinkCom/src/impl/windows/WindowsFindSerialPorts.cpp")
endif()

add_library(MavLinkCom STATIC ${_mavlink_sources})
target_include_directories(
  MavLinkCom
  PUBLIC
    "${_mavlink_source_dir}/common_utils/"
    "${_mavlink_source_dir}/include/"
)
target_link_libraries(MavLinkCom 
  PUBLIC
  Threads::Threads
)

set(_src_code_install_location "Unreal/Plugins/AirSim")

install(
  TARGETS
    MavLinkCom
  COMPONENT
    AirSimUnreal
  DESTINATION
    "${_src_code_install_location}/Source/AirLib/deps/MavLinkCom/lib"
  #FILE_SET 
  #  HEADERS DESTINATION "coucou"    
  #PUBLIC_HEADER 
  #  DESTINATION deps# COMPONENT Development
)


foreach(_file IN LISTS _mavlink_sources)
  get_filename_component(_file_ext "${_file}" EXT)
  if("${_file_ext}" MATCHES "\\.h.*")
    get_filename_component(_current_folder "${_file}" DIRECTORY)
    file(RELATIVE_PATH _current_folder "${_mavlink_source_dir}/include/" "${_current_folder}")
    string(FIND "${_current_folder}" ".." _index_dots)
    if(_index_dots GREATER_EQUAL 0)
      continue()
    endif()
    #message(FATAL_ERROR "toto '${_current_folder}' / ${_file}")
    install(
      FILES
        "${_file}"
      COMPONENT
        AirSimUnreal
      DESTINATION
        "${_src_code_install_location}/Source/AirLib/deps/MavLinkCom/include/${_current_folder}"
    )
  endif()
endforeach()


#CommonTargetLink()

