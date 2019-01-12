
add_library(mylib
    mymodule.cpp
    mymodule.hpp
)

add_library(mylib::mylib ALIAS mylib)

target_compile_features(mylib PRIVATE cxx_std_14)
target_compile_options(mylib PRIVATE -Wall -Wextra -pedantic -Werror)

target_include_directories(
  mylib 
 PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}>      # for headers when building
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>    # for generated files in build mode
  $<INSTALL_INTERFACE:include/mycorp/myproject>     # for clients in install mode
)

if(BUILD_TESTING)
  find_package(Catch2 REQUIRED)

  add_executable(tests 
      tests.cpp 
      mymodule.t.cpp
  )

  target_link_libraries(
   tests 
    PUBLIC 
   Catch2::Catch2 
   mymodule::mymodule
  )

  target_compile_features(tests PRIVATE cxx_std_14)
endif()