#include <iostream>
#include "obr.cpp"

int main(int argc, char *argv[]) {
    int inp;
    std::cout << "Введите число: ";
    std::cin >> inp;
    std::cout << obr(inp) << std::endl;
}