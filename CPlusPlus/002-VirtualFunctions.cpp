#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/virtual-functions
*/

class Person
{
    public: 
        char name[100]; 
        int age;
    
        virtual void getdata()=0;
        virtual void putdata()=0;

};

class Professor : public Person 
{ 
    private : 
        int publications; 
        static int cur_id;

    public :
        Professor()
        {

        }

        void getdata()
        {
            cin >> name >> age >> publications;
        }

        void putdata()
        {
            cur_id++;
            cout<< name << " " << age << " " << publications << " " << cur_id << endl;
        }

};
int Professor::cur_id=0;

class Student : public Person 
{ 
    private : 
        int mark[6]; 
        static int cur_id;

    public :
        Student()
        {

        }
    
        void getdata()
        {
            cin>>name>>age;

             for(int i=0;i<6;i++)
                 cin>>mark[i];
        }

        void putdata()
        {
            int sum=0;
            cur_id++;
            
            for(int i=0; i < 6; i++)
                sum += mark[i];
            cout<< name << " " << age << " " << sum << " " << cur_id << endl;
            
        }
};
int Student::cur_id=0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
