#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main() {
    string input;
    regex regexDigit("([0-9])+");
    regex regexPunc("\\*|\\+|\\(|\\)");

    cout << "Input number: \n";
    cin >> input;
    if(regex_match(input, regexDigit)){
        cout << "Number";
    }else if(regex_match(input, regexPunc)){
        cout << "Punctuation";
    }
    
    cout << "\n";
};

