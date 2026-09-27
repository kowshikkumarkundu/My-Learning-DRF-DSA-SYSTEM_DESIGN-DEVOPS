#include <iostream>
#include <string>

using namespace std;

class Car{
public:
    virtual void startEngine()=0;
    virtual void shiftGear(int gear)=0;
    virtual void accelarate()=0;
    virtual void brake()=0;
    virtual void stopEngine()=0;
    virtual ~car() {}
};