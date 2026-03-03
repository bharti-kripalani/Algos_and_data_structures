//Implements bitmap-based sorting of integers using a boolean array to mark presence. 
#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <bitset>

using namespace std;

int main()
{
	bitset<11> bits;

	for(int i=1;i<=10;i++)
		bits.reset(i);   //Resetting all the bits initially

	int a[10] = {10,9,8,2,6,5,3,7,1,4};
		
	for(int i=1;i<=10;i++)
	{
		bits.set(a[i-1]); //Setting the corresponding bits, where the element is present
	}

	int k = 0;

	for(int i =1;i<=10;i++)
	{
		if(bits.test(i) == 1) //If the element is present then put it in the array
		{
			a[k++] = i;
		}
	} 

	for(int i=0;i<10;i++)
		cout<<a[i]<<" ";


	getch();
	return 0;
}
