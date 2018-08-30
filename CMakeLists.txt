cmake_minimum_required(VERSION 2.8)
project(greet)

### 此处的动态库名必须和BOOST_PYTHON_MODULE()中定义的保持一致，即最后生成的库必须名为hello_ext.so
set(greetSRC cppDemo/greet_wrapper.cpp)
add_library(hello_ext SHARED ${greetSRC})
set_target_properties(hello_ext PROPERTIES PREFIX "")

#dependencies
INCLUDE(FindPkgConfig)
pkg_check_modules(PYTHON REQUIRED python)
include_directories(/usr/include ${PYTHON_INCLUDE_DIRS})
target_link_libraries(hello_ext boost_python)