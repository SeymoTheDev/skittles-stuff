#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
    char name[50];
    cout << "Naming System With C++" << endl;
    cin.getline(name, 50);

    char lib[100];
    cout << name << ", Whats up dude :D" << endl;
    cin.getline(lib, 100);
    return 0;
}