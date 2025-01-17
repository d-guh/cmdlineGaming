#include "encounters.h"
#include <time.h>
#include <chrono>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <random>
#include <thread>
void Encounters::Pausing()
{
    std::chrono::milliseconds duration(1000);
    std::this_thread::sleep_for(duration);
}
bool Encounters::GuessTime(std::string dialog, float precision, int timerange)
{
    std::string userinput;
    typedef std::chrono::high_resolution_clock Time;
    typedef std::chrono::duration<float> fsec;
    float time_to_guess = random() % timerange + timerange/10;
    time_to_guess = time_to_guess / 100;
    std::cout << dialog << std::endl;
    std::cout << "Take action as close as possible to the given time of " << time_to_guess << " seconds." << std::endl; 
    Pausing();
    std::cout << "Ready? (press enter when ready): ";
    getline(std::cin, userinput);
    std::cout << "Take action by pressing enter: ";
    auto t0 = Time::now();

    getline(std::cin, userinput);
    
    auto t1 = Time::now();

    fsec fs = t1 - t0;
    float adjustedVal = exp(-precision * pow(fs.count() - time_to_guess, 2));
    std::cout << "You did [" << round(adjustedVal * 100) << "%] damage with a time difference of [" << std::setprecision(4) << fabs(fs.count() - time_to_guess) << "] seconds\n\n" << std::endl;
    return true;
}