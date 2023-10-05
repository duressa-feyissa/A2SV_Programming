#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array
const long long mxN = 1e5;

vector<ar<long long, 3>> g;

long long n, m, u, v, w;
void solve()
{
    cin >> n >> m;
    for (int i = 0; i < m; ++i)
    {
        cin >> u >> v >> w;
        g.push_back({u, v, w});
    }
    vector<long long> dist(n + 1, 1e9);
    vector<long long> par(n + 1, -1);
    dist[1] = 0;
    for (int i = 0; i < n; ++i)
    {
        for (auto e : g)
        {
            if (dist[e[0]] + e[2] < dist[e[1]])
            {
                dist[e[1]] = dist[e[0]] + e[2];
                par[e[1]] = e[0];
            }
        }
    }
    int x = -1;
    for (auto e : g)
    {
        if (dist[e[0]] + e[2] < dist[e[1]])
        {
            x = e[1];
            break;
        }
    }
    if (x == -1)
    {
        cout << "NO" << endl;
    }
    else
    {
        cout << "YES" << endl;
        for (int i = 0; i < n; ++i)
        {
            x = par[x];
        }
        vector<long long> cycle;
        for (int v = x;; v = par[v])
        {
            cycle.push_back(v);
            if (v == x && cycle.size() > 1)
            {
                break;
            }
        }
        reverse(cycle.begin(), cycle.end());
        for (auto v : cycle)
        {
            cout << v << " ";
        }
        cout << endl;
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}