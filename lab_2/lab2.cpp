#include <ctime>
#include <fstream>
#include <iostream>

using namespace std;

string RandomSequence() {
	srand(time(NULL));
	string seq;

	for (int i = 0; i < 128; i++) {
		if (rand() % 2 == 1) seq += "1";
		else seq += "0";
	}

	return seq;
}

int main() {
	string sequence = RandomSequence();
	cout << sequence;

	return 0;
}