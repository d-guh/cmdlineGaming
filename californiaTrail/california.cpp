#include <iostream>
#include <iomanip>
#include <cctype>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <limits>
#include "california.h"
#include "inputs.h"
#include "introduction.h"
#include "inventory.h"
#include "encounters.h"
#include <unistd.h>
#include <chrono>
#include <thread>
using namespace std;



void PrintLine(string line)
{
    cout << line << endl;
}
void PrintLine(string line, int width)
{
    cout << setw(width) << left << line << endl;
}
void Pausing()
{
    std::chrono::milliseconds duration(500);
    std::this_thread::sleep_for(duration);
}

int main()
{
    Inputs input;
    Introduction intro;
    Inventory inventory;
    string q;
    string userinput;
    bool finished_purchasing = false;
    // type cls for windows build
    system("clear");
    intro.PrintDialogueOptions();
    Pausing();
    input.PromptUser("\nWhat is your choice?: ", input.multi5, userinput);
    intro.Startup();
    inventory.money = intro.GetWage(stoi(userinput) - 1);
    Pausing();
    cout << "Your starting money has been chosen as: $" << inventory.money << endl;
    Pausing();
    PrintLine("You have been given a gift of an oxen and a wagon from a friend to get you started on your journey.");
    inventory.oxen = 1;
    Pausing();
    do
    {
        intro.PrintShopOptions(intro.rules, inventory.money, inventory);
        input.PromptUser("\nWhat would you like to purchase?: ", input.inventorymulti, userinput);
        if (stoi(userinput) != 10)
        {
            intro.RequestPurchase(inventory.money, stoi(userinput) - 1,inventory);
        }
        else
        {
            finished_purchasing = true;
        }
        Pausing();
        Pausing();
        system("clear");
    } while (finished_purchasing == false);
    system("clear");
    PrintLine("Leaving the shop and starting your journey...");
    Pausing();

    Encounters encounters;
    encounters.GuessTime("You prepare to take the shot...", 1, 400);
    encounters.GuessTime("You prepare to take the shot...", 1, 400);
    encounters.GuessTime("You prepare to take the shot...", 1, 400);
    encounters.GuessTime("You prepare to take the shot...", 1, 400);
    encounters.GuessTime("You prepare to take the shot...", 1, 400);
    encounters.GuessTime("You prepare to take the shot...", 1, 400);
    encounters.GuessTime("You prepare to take the shot...", 1, 400);

    return 0;
}