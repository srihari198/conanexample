#include <iostream>
#include "a.h"

void a(){
    #ifdef _WIN64
      std::cout << "LibA 64 bits\n";
    #else
      std::cout << "LibA 32 bits\n";
    #endif
}