cmake_minimum_required(VERSION 3.26)

# set vars
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 17)

# set exec names
set(AppExec fdWindow)
set(TestExec tests)

set(CMAKE_AUTORCC ON)

# setup project
project(force_directed_graph_qt)

set(ENZO_DEV_LIB_DIR "${CMAKE_SOURCE_DIR}/build/src/OpDefs/")

set(SOURCES
    src/force_directed_graph_qt/GraphWindow.cpp
    src/force_directed_graph_qt/ForceDirectedGraph.cpp
    src/force_directed_graph_qt/GraphicsView.cpp
    src/force_directed_graph_qt/GraphicsScene.cpp
    src/force_directed_graph_qt/Node.cpp
    src/force_directed_graph_qt/Edge.cpp
)

set(ENGINE_INCLUDE_DIRECTORIES
    src
    extern/icecream-cpp/include
)


# qt
find_package(Qt6 REQUIRED COMPONENTS Core Widgets SvgWidgets OpenGLWidgets)
qt_standard_project_setup()
ADD_DEFINITIONS(-DQT_NO_KEYWORDS)

# tbb
find_package(TBB REQUIRED COMPONENTS tbb)


qt_add_executable(${AppExec}
    ${SOURCES}
)

target_compile_definitions(${AppExec} PRIVATE ENZO_DEV_LIB_DIR="${ENZO_DEV_LIB_DIR}")


target_link_libraries(${AppExec} PRIVATE Qt6::Core Qt6::Widgets Qt6::SvgWidgets Qt6::OpenGLWidgets TBB::tbb)
target_include_directories(${AppExec} PUBLIC
    ${ENGINE_INCLUDE_DIRECTORIES}
)
