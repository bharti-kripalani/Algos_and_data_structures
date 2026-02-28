#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <bitset>

using namespace std;

int main()
{
	bitset<8> b; //MSB...LSB
	cin>>b;

	int i = b.all();//This will return true if all the bits are set true

	i = b.any(); //This will return true if any of the bit is set to true

	i = b.at(1); //This will return true if the bit at position 1 is set to true

	i = b.count(); //This will return the count of the bits that are set

	b.flip(4); //It will flip the bit specified at the position 4

	i = b.none(); //It will return 1 if none of the bits are set. Otherwise it will return zero

	b.reset(1); //It will reset(set to zero) the specified bit

	b.set(2); //It will set(to one) the specified bit

	i = b.size(); //It will return the no. of bits specified in the bit vector

	i = b.test(2); //It will return 0 or 1. Whatever, is the value of the bit

	string s = b.to_string(); //Convert the bitset to the string

	getch();
	return 0;
}
