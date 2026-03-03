//Performs binary search on a sorted array and counts all occurrences of a given element.
#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;

int binsearch(int a[],int low,int high, int x)
{
	int mid,count=0;
	while(low<high)
	{
		mid = (low+high)/2;
		if(x == a[mid])
		{
			count++;
			int l = mid-1; // Count to the left of the number found and keep decrementing the left counter
			while(x==a[l])
			{
				l--;
				count++;
			}
			int r = mid + 1; //Count to the right of the number found and keep incrementing the right counter
			while(x==a[r])
			{
				r++;
				count++;
			}
			return count; //Return the count
		}
		else if(x<a[mid]) //Normal condition
			high = mid - 1;
		else if(x>a[mid])
			low = mid + 1;
	}

	return 0;
}


int main()
{
	int a[] = {1,2,3,4,5,6,6,6,6,6,6,6,7,7,8,9,9,10,10};


	char c[] = {'a','b','c','d'};
	int len = sizeof(c)/sizeof(char);
	cout<<len<<endl;
	int i=0;

	while(i<len)
	{
		cout<<c[i];


	}
	getch();
	return 0;
}
