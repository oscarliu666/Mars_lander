#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    // declare variables
    int counter = 1;
    double m, k, x, v, t_max, dt, t, a;
    vector<double> t_list, x_list, v_list;
    // mass, spring constant, initial position and velocity
    m = 1;
    k = 1;
    x = 0;
    v = 1;
    // simulation time and timestep
    t_max = 0.2;
    dt = 0.1;

    // Euler integration
    for (t = 0; t < t_max; t += dt) {

        // append current state to trajectories
        t_list.push_back(t);
        x_list.push_back(x);
        v_list.push_back(v);

        // calculate new position and velocity
        a = -k * x / m;
        x = x + dt * v;
        v = v + dt * a;
    }

    t_max = 100;
    for (t = 0.2; t <= t_max; t += dt) {

        // calculate new position and velocity
        a = -k * x / m;
        x = 2*x_list[counter]-x_list[counter-1]+(pow(dt,2))*a;
        v = (1/dt)*(x-x_list[counter]);

        // append current state to trajectories
        t_list.push_back(t);
        x_list.push_back(x);
        v_list.push_back(v);
        counter+=1;


    }

    // Write the trajectories to file
    ofstream fout;
    fout.open("trajectories.txt");
    if (fout) { // file opened successfully
        for (int i = 0; i < t_list.size(); i = i + 1) {
            fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
        }
    }
    else { // file did not open successfully
        cout << "Could not open trajectory file for writing" << endl;
    }


}