#include <iostream>
#include <vector>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    vector<vector<int>> graph(b, vector<int>(3, 0));
    for (int i = 0; i < b; i++) {
        cin >> graph[i][0] >> graph[i][1] >> graph[i][2];
    }

    vector<int> dist(a, 30000);

    dist[0] = 0;
    for (int i = 0; i < a - 1; i++) {
        for (int j = 0; j < b; j++) {
            if (dist[graph[j][0] - 1] != 30000 && dist[graph[j][1] - 1] > dist[graph[j][0] - 1] + graph[j][2]) {
                dist[graph[j][1] - 1] = dist[graph[j][0] - 1] + graph[j][2];
            }
        }
    }

    for (int i = 0; i < a; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;
}