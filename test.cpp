// C) 2020 Nathaniel D'Rozario
// See LICENSE file for license details

#include <fstream>
using namespace std;

int main () { // multiplies by 2
    ifstream fin ("test.in");
    ofstream fout ("test.out");
    int n;
    fin >> n;
    fout << n * 2;
    return 0;
}