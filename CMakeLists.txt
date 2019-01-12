cmake_minimum_required(VERSION 3.10)
project(cmake-bootstrap LANGUAGES CXX VERSION 0.0.1)

include(GNUInstallDirs)

# Set default build_type to Release
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

#
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Static analyze files
set(CMAKE_CXX_CLANG_TIDY "clang-tidy;-config=")

if (EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup()
endif()

if (EXISTS ${CMAKE_BINARY_DIR}/conan_paths.cmake)
  include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
endif()

add_subdirectory(src/mycorp/myproject)
