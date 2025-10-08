cmake_minimum_required(VERSION 3.26)

# set vars
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 17)

set(CMAKE_AUTORCC ON)

# set exec names
set(AppExec fdWindow)

# setup project
project(force_directed_graph_qt)

set(SOURCES
    standardWindow.cpp
)

set(INCLUDE_DIRECTIONS
    ../../include/
)

# qt
find_package(Qt6 REQUIRED COMPONENTS Core Widgets)
qt_standard_project_setup()
ADD_DEFINITIONS(-DQT_NO_KEYWORDS)

qt_add_executable(${AppExec}
    ${SOURCES}
)

target_link_libraries(${AppExec} PRIVATE "${CMAKE_CURRENT_LIST_DIR}/../../build/libForceDirectedGraphQt.so" Qt6::Core Qt6::Widgets)
target_include_directories(${AppExec} PUBLIC ${INCLUDE_DIRECTIONS})
