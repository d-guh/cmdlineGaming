#ifndef INPUTS_H
#define INPUTS_H
#include <string>
#include <vector>
class Inputs
{
    public:
        std::vector<std::string> multi2 = {"Y", "N", "y", "n"};
        std::vector<std::string> multi3 = {"1", "2", "3"};
        std::vector<std::string> multi4 = {"1", "2", "3", "4"};
        std::vector<std::string> multi5 = {"1", "2", "3", "4", "5"};
        std::vector<std::string> inventorymulti = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"};
        Inputs() = default;
        bool ValidateInput(std::string, std::vector<std::string>);
        std::string PromptUser(std::string, std::vector<std::string>, std::string&);
};

#endif