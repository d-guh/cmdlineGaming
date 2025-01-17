#pragma once
#include <string>
class Encounters
{
    public:
        bool GuessTime(std::string dialog, float precision, int timerange);
        void Pausing();
};