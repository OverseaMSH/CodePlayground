#include <iostream>
#include <stdexcept>
using namespace std;

// Define a structure for a node in the linked list
struct Node {
    int data;       // Data stored in the node
    Node* next;     // Pointer to the next node
};

// Define a structure for the list
struct List {
    Node* head;     // Pointer to the first node
    int size;       // Number of elements in the list
};

// Function to create and initialize the list
void Create(List &L) {
    L.head = nullptr; // List starts empty
    L.size = 0;       // Size is initialized to 0
}

// Function to return the size of the list
int Size(const List &L) {
    return L.size;
}

// Function to return the first element of the list
int First(const List &L) {
    if (L.size != 0) {
        return L.head->data; // Return the data of the first node
    } else {
        throw runtime_error("Error: List is empty");
    }
}

// Function to check if the list is empty
bool isEmpty(const List &L) {
    return L.size == 0;
}

// Function to insert a new element at the beginning of the list
void InsertFirst(List &L, int x) {
    Node* newNode = new Node; // Allocate a new node
    newNode->data = x;        // Set the data
    newNode->next = L.head;   // Point to the current head
    L.head = newNode;         // Update the head to the new node
    L.size++;                 // Increment the size
}

// Function to insert a new element after a given node
void InsertAfter(List &L, Node* n, int x) {
    if (n == nullptr) {
        throw runtime_error("Error: Node does not exist");
    }
    Node* newNode = new Node; // Allocate a new node
    newNode->data = x;        // Set the data
    newNode->next = n->next;  // Link the new node to the next node
    n->next = newNode;        // Link the given node to the new node
    L.size++;                 // Increment the size
}

// Function to delete the first element of the list
void DeleteFirst(List &L) {
    if (isEmpty(L)) {
        throw runtime_error("Error: List is empty");
    }
    Node* temp = L.head;      // Store the current head
    L.head = L.head->next;    // Update the head to the next node
    delete temp;              // Free the old head node
    L.size--;                 // Decrement the size
}

// Function to delete the element after a given node
void DeleteAfter(List &L, Node* n) {
    if (isEmpty(L) || n == nullptr || n->next == nullptr) {
        throw runtime_error("Error: Element does not exist");
    }
    Node* temp = n->next;     // Store the node to be deleted
    n->next = temp->next;     // Update the link to skip the deleted node
    delete temp;              // Free the deleted node
    L.size--;                 // Decrement the size
}

// Helper function to display the list elements
void Display(const List &L) {
    Node* current = L.head;
    cout << "List: ";
    while (current != nullptr) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    List myList; // Create a list
    Create(myList); // Initialize the list

    // Insert elements
    InsertFirst(myList, 10);
    InsertFirst(myList, 20);
    InsertFirst(myList, 30);
    Display(myList); // Output: List: 30 20 10

    // Insert after a specific node
    Node* secondNode = myList.head->next; // Get the second node
    InsertAfter(myList, secondNode, 25);
    Display(myList); // Output: List: 30 20 25 10

    // Get the first element
    cout << "First element: " << First(myList) << endl;

    // Delete the first element
    DeleteFirst(myList);
    Display(myList); // Output: List: 20 25 10

    // Delete after a specific node
    DeleteAfter(myList, myList.head);
    Display(myList); // Output: List: 20 10

    // Check if the list is empty
    cout << "Is list empty? " << (isEmpty(myList) ? "Yes" : "No") << endl;

    return 0;
}
