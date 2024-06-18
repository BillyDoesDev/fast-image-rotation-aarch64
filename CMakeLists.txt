cmake_minimum_required(VERSION 3.5)
project(nuts VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SOURCE_FILES
    utils/dlr_neon.cpp
)

set(CMAKE_PREFIX_PATH ${PROJECT_SOURCE_DIR}/opencv/bleh/install)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
SET(CMAKE_CXX_FLAGS "-static")
