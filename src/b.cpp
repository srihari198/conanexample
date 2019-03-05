#include <iostream>
#include "a.h"
#include "b.h"

void b(){
    a();
    #ifdef _WIN64
      std::cout << "LibA 64 bits\n";
    #else
      std::cout << "LibA 32 bits\n";
    #endif
}
