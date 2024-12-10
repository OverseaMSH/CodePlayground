#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Compound {
    int cost; 
    int weight;  
    double ratio;  

    Compound(int c, int w) : cost(c), weight(w) {
        ratio = (double)cost / weight;
    }
};

bool compare(Compound a, Compound b) {
    return a.ratio > b.ratio;
}

int main() {
    int n, W;
    cin >> n >> W;  
    vector<Compound> compounds;

    for (int i = 0; i < n; ++i) {
        int cost, weight;
        cin >> cost >> weight;
        compounds.push_back(Compound(cost, weight));
    }

    sort(compounds.begin(), compounds.end(), compare);

    double totalValue = 0.0; 
    int remainingCapacity = W;

    for (int i = 0; i < n; ++i) {
        if (remainingCapacity == 0) {
            break;  
        }

        int weightTaken = min(compounds[i].weight, remainingCapacity);
        totalValue += (weightTaken * compounds[i].ratio);
        remainingCapacity -= weightTaken;  
    }

    cout << fixed << setprecision(4) << totalValue << endl;

    return 0;
}
