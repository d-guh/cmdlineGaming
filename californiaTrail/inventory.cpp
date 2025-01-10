#include "inventory.h"
void Inventory::ChangeInventory(int item, int amount)
{
    switch(item)
    {
        case 1:
            oxen += amount;
            break;
        case 2:
            medical += amount;
            break;
        case 3:
            wagonparts += amount;
            break;
        case 4:
            food += amount * 30;
            break;
        case 5:
            ammo += amount;
            break;
        case 6:
            textiles += amount;
            break;
        case 7:
            tools += amount;
            break;
        case 8:
            clothing += amount;
            break;
        case 9:
            guns += amount;
            break;
    }
}