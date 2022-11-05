#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>


using namespace std;

float posNum(string token)
{
    cout << "entering posNum" << endl;
    if (token == "WR")
    {
        return 1;
    }
    if (token == "RB")
    {
        return 2;
    }
    if (token == "QB")
    {
        return 3;
    }
    if (token == "TE")
    {
        return 4;
    }
    if (token == "DST")
    {
        return 4;
    }
    return -1;
}

float* allPlayers()
{
    cout << "entering function" << endl;
    float* ptr = (float*) malloc(8976); 
    float arr[561][4];
    cout << "malloced" << endl;


    int i = 0;
  
    // File pointer
    fstream fin;
  
    // Open an existing file
    fin.open("DKSalaries.csv", ios::in);
    cout << "opened fiile DKSalaries.csv" << endl;
    
  
    // Read the Data from the file
    // as String Vector
    vector<string> row;
    string word, temp;
    char* line;

    cout << "initialized variables for parsing file" << endl;

    while (fin >> temp) 
    {
        
        cout << "top of loop" << endl;
        int m = 0;
        float a, b, c, d;
        row.clear();
        cout << "reseting row data" << endl;
        string str;
        // read an entire row and
        // store it in a string variable 'str'
        getline(fin, str);
        line = &str[0];

        cout << "line:" << str << endl;

        char *token = strtok(line, ",");
 
        // Keep printing tokens while one of the
        // delimiters present in str[].
        if (i!=0)
        {
            while (token != NULL)
            {
    
                cout << m << ":" << token << endl;
                if (m==3)
                {
                    a = stof (token);
                }
                if (m==5)
                {
                    b = stof (token);
                }
                if (m==8)
                {
                    c = stof (token);
                }
                if (m==0)
                {
                    d = posNum(token);
                }
                token = strtok(NULL, ",");
                m++;
            }
            cout << a << "," << b <<  "," << c << "," <<  d << endl;
            arr[i-1][0] = a; //ID
            arr[i-1][1] = b; //SALARY
            arr[i-1][2] = c; //PROJ
            arr[i-1][3] = d; //POS
            cout <<  "assigned to arr[" << i-1 << "]" << endl;
        }
        


        cout << arr[i-1] << endl;
        i++;
    }
    cout << arr << endl;
    return *arr; 
}

int main(int argc, char** argv)
{
    allPlayers();
    return 0;
}