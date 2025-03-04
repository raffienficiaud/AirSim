cmake_minimum_required(VERSION 3.5.0)
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

file(GLOB_RECURSE 
  ${PROJECT_NAME}_sources
  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/api/*.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/api/*.cpp
  
  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/common/*.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/common/*.cpp
  
  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/common/common_utils/*.cpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/common/common_utils/*.cpp
  
  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/safety/*.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/safety/*.cpp

  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/vehicles/car/api/*.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/vehicles/car/api/*.cpp

  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/vehicles/multirotor/*.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/vehicles/multirotor/*.cpp

  ${AIRSIM_ROOT}/${PROJECT_NAME}/include/vehicles/multirotor/api/*.hpp
  ${AIRSIM_ROOT}/${PROJECT_NAME}/src/vehicles/multirotor/api/*.cpp
)

add_library(${PROJECT_NAME} STATIC ${${PROJECT_NAME}_sources})

# CommonTargetLink()
target_link_libraries(${PROJECT_NAME} 
  #${RPC_LIB}
  
  PUBLIC
    MavLinkCom
    Threads::Threads
    Eigen3::Eigen
    rpclib::rpc
  )
#target_link_libraries(${PROJECT_NAME} MavLinkCom)
#target_link_libraries(${PROJECT_NAME} ${CMAKE_THREAD_LIBS_INIT})

#string(SUBSTRING ${CMAKE_STATIC_LINKER_FLAGS} 9 -1 "BUILD_PLATFORM")
#find_package(Threads REQUIRED)
#target_link_libraries(${PROJECT_NAME} ${CMAKE_THREAD_LIBS_INIT})
#target_link_libraries(${PROJECT_NAME} AirLib)
#target_link_libraries(${PROJECT_NAME} MavLinkCom)
#target_link_libraries(${PROJECT_NAME} ../AirLib/deps/rpclib/lib/${BUILD_PLATFORM}/$(Configuration)/rpc)
