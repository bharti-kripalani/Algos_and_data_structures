/**
This program implements a simple smart pointer using reference counting.
The smart pointer stores a pointer to an object and a reference counter that tracks how many smart pointers are using the same object.
When a smart pointer is copied, the reference count increases.
When a smart pointer is destroyed, the reference count decreases.
When the reference count becomes 0, the memory is automatically deleted.
This helps manage memory safely and prevents memory leaks.
  **/

#include <iostream>
using namespace std;

// Template Smart Pointer class
template <class T>
class SmartPointer
{
private:
    T* ptr;            // Pointer to the actual object
    int* ref_count;    // Reference counter

public:

    // Constructor
    SmartPointer(T* p)
    {
        ptr = p;               // Store the object pointer
        ref_count = new int(1); // Initialize reference count to 1
    }

    // Copy constructor
    SmartPointer(const SmartPointer& sp)
    {
        ptr = sp.ptr;              // Copy pointer
        ref_count = sp.ref_count;  // Share reference counter
        (*ref_count)++;            // Increase reference count
    }

    // Destructor
    ~SmartPointer()
    {
        (*ref_count)--; // Decrease reference count

        // If no pointers are using the object
        if (*ref_count == 0)
        {
            delete ptr;        // Delete the object
            delete ref_count;  // Delete the counter
            cout << "Memory deleted" << endl;
        }
    }

    // Overload * operator to access the value
    T& operator*()
    {
        return *ptr;
    }
};

int main()
{
    // Create smart pointer
    SmartPointer<int> sp1(new int(10));

    {
        // Copy smart pointer
        SmartPointer<int> sp2 = sp1;

        cout << *sp1 << endl;
        cout << *sp2 << endl;
    } // sp2 goes out of scope here

    // Memory will be deleted when sp1 also goes out of scope
    return 0;
}
