#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

// An arbitrary number that's large compared to the ones in the problem.
const int LARGE = 1e9;

int main() {
	int num_miles;
	std::cin >> num_miles;

	vector<std::string> segment_type(num_miles);
	vector<int> start(num_miles);
	vector<int> end(num_miles);
	for (int m = 0; m < num_miles; m++) {
		std::cin >> segment_type[m] >> start[m] >> end[m];
	}

	// Set a large range that might as well be (-infinity, infinity)
	int low = -LARGE;
	int high = LARGE;
	for (int m = num_miles - 1; m >= 0; m--) {
		if (segment_type[m] == "none") {
			// Set a new range based on sensor reading.
			low = std::max(low, start[m]);
			high = std::min(high, end[m]);
		} else if (segment_type[m] == "off") {
			// Update range of possible traffic flows
			low += start[m];
			high += end[m];
		} else if (segment_type[m] == "on") {
			low -= end[m];
			high -= start[m];
			// Set to zero if low becomes negative
			low = std::max(0, low);
		}
	}

	std::cout << low << ' ' << high << endl;

	low = -LARGE;
	high = LARGE;

	// Process again, this time scanning the other way
	for (int m = 0; m < num_miles; m++) {
		if (segment_type[m] == "none") {
			low = std::max(low, start[m]);
			high = std::min(high, end[m]);
		} else if (segment_type[m] == "on") {
			low += start[m];
			high += end[m];
		} else if (segment_type[m] == "off") {
			low -= end[m];
			high -= start[m];
			low = std::max(0, low);
		}
	}

	std:;cout << low << ' ' << high << endl;
}
