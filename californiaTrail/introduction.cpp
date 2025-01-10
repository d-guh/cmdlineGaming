#include "introduction.h"
#include <vector>
#include <fstream>
// A function that reads from the gamerules.txt file, and using ~ as a comment character, read the file line by line and insert the lines into a vector of strings
void Introduction::ReadGameRules()
{
    std::ifstream file("gamerules.txt");
    std::string line;
    if (file.is_open())
    {
        while (std::getline(file, line))
        {
            if (line[0] != '~')
            {
                rules.push_back(line);
            }
        }
        file.close();
    }
}
// Write a function that takes a vector of strings and inserts the first n elements into an array of ints, removes those elements from the vector, and returns the array
void Introduction::GetWages(std::vector<std::string>& rules, int n)
{
    int *wages = new int[n];
    rules.erase(rules.begin());
    for (int i = 0; i < n; i++)
    {
        wages[i] = std::stoi(rules[i]);
    }
    rules.erase(rules.begin() + 1, rules.begin() + n + 1);
    
    if (stoi(rules[0]))
    {
        rules.erase(rules.begin());
        for (int i = 0; i < n; i++)
        {
            int random = rand() % stoi(rules[0]) - stoi(rules[0])/2;
            wages[i] += random;
        }
        rules.erase(rules.begin());
    }

    this->Wage = wages;
}
void Introduction::Startup()
{
    srand(time(0));
    ReadGameRules();
    GetWages(rules, std::stoi(rules[0]));
    LoadShopOptions();
}
bool Introduction::RequestPurchase(int& usermoney, int itemrequested, Inventory& inv)
{
    if (usermoney >= inventory[itemrequested])
    {
        usermoney -= inventory[itemrequested];
        std::cout << "You have purchased (" << invnames[itemrequested] << ") for $" << inventory[itemrequested] << std::endl;
        inv.ChangeInventory(itemrequested + 1, 1);
        return true;
    }
    else
    {
        std::cout << "You do not have enough money to purchase this item." << std::endl;
        return false;
    }
}