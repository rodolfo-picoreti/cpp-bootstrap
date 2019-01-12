
#include "mymodule.hpp"

namespace mycorp {

auto is_this_working() -> bool {
  // generate leak to test static analysis
  int* x = new int{1};
  return *x;
}

}  // namespace mycorp