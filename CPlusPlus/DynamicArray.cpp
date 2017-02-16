#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int numArray, numQueries,collum,value;
    int myPointer; 
    
    cin >> numArray >> numQueries;
    
    
    
    int** myArray = new int*[numArray];
    for (int i = 0; i < numArray; i++) {
        cin >> collum;
        myArray[i] = new int[collum];
        for(int j = 0; j < collum; j++)
        {
            cin >> value;
            myArray[i][j] = value;
        }
    }
    
    int row, index;
    for (int i = 0; i < numQueries; i++) {
        cin >> row >> index; 
        cout << myArray[row][index] << endl;
    }
       
    
    
    return 0;
}
