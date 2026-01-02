#include <iostream>

int main()
{
    // Array of size 10. Numbers 1 to 9 appear once, but 9 is repeated
    int a[10] = {1,2,3,4,5,6,7,8,9,9};
    int n = 10;  // Total number of elements in the array

    // Calculate the expected sum if numbers were 1 to n
    // Formula: sum of first n natural numbers = n * (n + 1) / 2
    int expectedSum = n * (n + 1) / 2;

    int actualSum = 0;  // Variable to store sum of elements in the array

    // Calculate the sum of elements in the array
    for(int i = 0; i < n; i++)
    {
        actualSum += a[i];
    }

    // Find the duplicate number
    // Explanation:
    // 1. (expectedSum - actualSum) gives the difference between what sum should be and what it actually is
    // 2. Subtracting this from n gives the repeated number
    int duplicate = n - (expectedSum - actualSum);

    // Print the repeated number
    std::cout << "Repeated Number: " << duplicate << std::endl;

    return 0;
}
