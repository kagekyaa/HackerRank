#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

/*
Only Pass Test Case #0
https://www.hackerrank.com/challenges/attribute-parser
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int numofLines, numofQueries;
    
    cin >> numofLines >> numofQueries;
    cin.ignore();
    
    string input[20], query[20];
    
    //input:
    for(int i=0; i < numofLines;i++)
    {
        getline(cin, input[i]);
    }
     
    for(int i=0; i < numofQueries;i++)
    {
        getline(cin, query[i]);
    }
   
    //processing:
    bool status = false;
    string tempAttribute, tempTagName, tempValue;
    size_t foundSp1, foundSp2;
    for(int i=0; i < numofQueries; i++)
    {
        foundSp1 = query[i].find_last_of('.');
        tempTagName = query[i].substr(foundSp1+1);
        foundSp2 = tempTagName.find_last_of('~');
        tempAttribute = tempTagName.substr(foundSp2+1);
        tempTagName = tempTagName.substr(0,foundSp2);
        
        /*
        cout << query[i] << endl;
        cout << tempTagName << endl;
        cout << tempAttribute << endl;
        */
       
        for(int j = 0; j < numofLines; j++)
        {
            //cout << j << " " << tempTagName << " " <<  tempAttribute << endl;
            foundSp1 = input[j].find(tempTagName);
            if(foundSp1 != string::npos)
            {   
                //cout << foundSp1 << " : " << j << endl;
                
                foundSp1 = input[j].find(tempAttribute);
                tempValue = "";
                if(foundSp1 != string::npos)
                {
                    status = false;
                    for(int k = foundSp1+tempAttribute.size()+2; k < input[j].size() ; k++)
                    {
                        //start recording:
                        if(status == true)
                        {
                            if(input[j][k] == '"')
                            {
                                cout << tempValue << endl;
                                break;
                            }
                            tempValue += input[j][k];
                        }
                        if(input[j][k] == '"')
                        {
                            status = true;
                        }
                    }
                    break;
                }
                else
                {
                    //output:
                    cout << "Not Found!" << endl;
                    break;
                }
                break;
            }
        }
       
    }
   
    
    return 0;
}
