project(MyHello CXX)

include($(CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(b b.cpp)
target_link_libraries(b CONAN_PKG::LibA)
