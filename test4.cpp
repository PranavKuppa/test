#include <conio.h>
#include <iomanip.h>
#include <iostream>
#include <math.h>

using namespace std;

int main() {

  int count = 10;
  for (int i = 0; i < count; i++) {
    cout << "Iteration: " << i << endl;
    if (i == 5) {
      cout << "Halfway there!" << endl;
    }
  }
  return 0;
}
