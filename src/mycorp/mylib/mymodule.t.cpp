#include <catch2/catch.hpp>
#include "mymodule.hpp"

TEST_CASE("module test") {
  REQUIRE(mycorp::is_this_working() == false);
}
