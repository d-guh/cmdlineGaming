#ifndef INTRO_H
#define INTRO_H
#include <string>
#include <iostream>
#include <iomanip>
#include <vector>
#include "inventory.h"
class Introduction
{
    public:
        Introduction() = default;
        int* Wage;
        std::vector<std::string> rules;
        std::vector<int> inventory;
        std::string invnames[9] = {"Oxen", "Medical Supplies", "Wagon Parts", "Food", "Ammo", "Textiles", "Tools", "Clothing", "Guns"};
        void ReadGameRules();
        void PrintLine(std::string line)
        {
            std::cout << line << std::endl;
        }
        void PrintLinePrice(std::string line, int prices, int width, int owned)
        {
            std::cout << std::setw(width) << std::left << line << std::left << "$" << std::setw(15) << prices << std::setw(10) << owned << std::endl;
        }
        int ConvertItemStrToPriceInt(std::vector<std::string>& rules)
        {
            int price = std::stoi(rules[0]);
            rules.erase(rules.begin());
            return price;
        }
        void PrintDialogueOptions()
        {
            PrintLine("Choose how to start your adventure: ");
            PrintLine("--------------------------------------------------------");
            PrintLine("1. Factory worker from the north");
            PrintLine("2. Blacksmith working for the rail company");
            PrintLine("3. Freedman from the south looking for a new future");
            PrintLine("4. Immigrant from Europe starting a new life");
            PrintLine("5. Orphan finding their own way");
            PrintLine("--------------------------------------------------------");
        }
        void LoadShopOptions()
        {
            for (int i = 0; i < 9; i++)
            {
                inventory.push_back(ConvertItemStrToPriceInt(rules));
            }
        }
        void PrintShopOptions(std::vector<std::string>& rules, int money, Inventory& inv)
        {
            int width = 30;
            // Buy: oxen $100 (1) medical $50 (2) wagon parts $50 (3) food $70 (4) ammo (5) textiles (6) tools (7) clothing (8) guns (9) 
            std::cout << "\n";
            PrintLine("Purchase Items from your hometown shop: ");
            std::cout << "\n";
            std::cout << std::setw(width) << std::left << "You have" << std::right << "$" << money << " to spend."<< "  Owned" << std::endl;
            PrintLine("--------------------------------------------------------");
            PrintLinePrice("1. Oxen", inventory[0], width, inv.oxen);
            PrintLinePrice("2. Medical Supplies", inventory[1], width, inv.medical);
            PrintLinePrice("3. Wagon Parts", inventory[2], width, inv.wagonparts);
            PrintLinePrice("4. Food [lbs]", inventory[3], width, inv.food);
            PrintLinePrice("5. Ammo", inventory[4], width, inv.ammo);
            PrintLinePrice("6. Textiles", inventory[5], width, inv.textiles);
            PrintLinePrice("7. Tools", inventory[6], width, inv.tools);
            PrintLinePrice("8. Clothing", inventory[7], width, inv.clothing);
            PrintLinePrice("9. Guns", inventory[8], width, inv.guns);
            PrintLine("--------------------------------------------------------");
            PrintLine("10. Leave the shop");
        }
        int GetWage(int i)
        {
            return Wage[i];
        }
        bool RequestPurchase(int&, int,Inventory&);
        void Startup();
        void GetWages(std::vector<std::string>&, int);
};
#endif