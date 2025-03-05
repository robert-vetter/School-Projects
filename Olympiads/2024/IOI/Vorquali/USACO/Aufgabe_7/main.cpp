#include <bits/stdc++.h>

using namespace std;

const int MAX_TIME = 1000;

int main() {
	int n;
	cin >> n;

	vector<int> change(MAX_TIME + 1);
	for (int c = 0; c < n; c++) {
		int start, end;
		int amt;
		cin >> start >> end >> amt;

		// at the start, we'll need some additional buckets
		change[start] += amt;
		// at the end, those buckets are no longer needed
		change[end] -= amt;
	}

	int max_buckets = 0;  // the maximum number of buckets needed
	int curr_buckets =
	    0;  // # of buckets we need at the current processing time
	for (int t = 0; t < MAX_TIME; t++) {
		// update the # of buckets we're using
		curr_buckets += change[t];
		// update the maximum accordingly
		max_buckets = max(max_buckets, curr_buckets);
	}

	cout << max_buckets << endl;
}
