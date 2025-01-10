#ifndef INV_H
#define INV_H
class Inventory{
    public:
        Inventory() = default;
        int money = {0};
        int oxen = {0};
        int medical = {0};
        int wagonparts = {0};
        int food = {0};
        int ammo = {0};
        int textiles = {0};
        int tools = {0};
        int clothing = {0};
        int guns = {0};
        void ChangeInventory(int item, int amount);
};
#endif