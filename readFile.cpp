/**********************************************
Last Name:  <your last name>
First Name:  <your first name>
Student ID: <your student ID number>
Course: CPSC 457
Tutorial Section: <your tutorial sction>
Assignment: 1
Question: 2

File name: readFile.cpp
**********************************************/

#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char * const argv[])
{
    // Get the file name
    string filename;

    if (argc != 2)
    {
        cout << "Usage: readFile <input file> " << endl;
        return -1;
    }
    else
    {
        filename = argv[1];
    

    // Open the file
    ifstream infile;
    infile.open(filename.c_str());
    
    
    string line;        // each line of the file
    getline(infile, line);
    while (!infile.eof())
    {
        cout << line << endl;
        getline(infile, line);
    }
    
    infile.close();
        
    }
    
    return 0;
}
