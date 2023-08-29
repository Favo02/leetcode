#include <string>
#include <iostream>
using namespace std;

class Solution {
public:

  int bestClosingTime(string customers) {
    // cout << '\n' << customers << '\n';

    uint N = customers.length();

    uint clients[N];
    uint empty[N];

    uint ccount = 0;
    uint ecount = 0;
    
    for (uint i = 0, j = N-1; i < N; i++, j--) {
      empty[i] = ecount;
      ccount += customers[j] == 'Y' ? 1 : 0;
      ecount += customers[i] == 'N' ? 1 : 0;
      clients[j] = ccount;
    }

    uint min = empty[0] + clients[0];
    uint minI = 0;
    for (uint i = 0; i < N; i++) {
      uint pen = empty[i] + clients[i];
      if (pen < min) {
        min = pen;
        minI = i;
      }
    }

    // edge case best time greather than array length
    if (calculatePenalty(customers, N) < min) {
      minI = N;
    }

    cout << minI << '\n';

    return minI;
  }

  int calculatePenalty(string customers, int closing) {
    int penalty = 0;

    for (uint i = 0; i < customers.length(); i++) {
      if (i < closing) {
        penalty += customers[i] == 'N' ? 1 : 0;
      }
      else {
        penalty += customers[i] == 'Y' ? 1 : 0;
      }
    }

    return penalty;
  }

};

int main() {
  Solution* s = new Solution();

  s->bestClosingTime("YNYY"); // 4
  s->bestClosingTime("YYNY"); // 2
  s->bestClosingTime("NYYYYNYN"); // 5
  s->bestClosingTime("YYYY"); // 4
  s->bestClosingTime("NNNNN"); // 0

}
