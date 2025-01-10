#include "inputs.h"
#include <string>
#include <iostream>
#include <vector>
// Process a user input, use an arrary of strings to check if the input is valid against any of those options, if valid return true as a bool
bool Inputs::ValidateInput(std::string userinput, std::vector<std::string> options)
{
    for (std::string i : options)
    {
        if (userinput == i)
        {
            return true;
        }
    }
    return false;
}
// Prompt the user for input, return the input as a string
std::string Inputs::PromptUser(std::string question, std::vector<std::string> validOptions, std::string& userinput)
{
    std::cout << question;
    std::getline(std::cin, userinput);
    if (!this->ValidateInput(userinput, validOptions))
    {
        std::cout << "Invalid input, please try again." << std::endl;
        this->PromptUser(question, validOptions, userinput);
    }
    return userinput;
}