#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double fl;
typedef vector<ll> vll;
#define re(i, n) for (int i = 0; i < n; i++)
#define endl "\n"
#define rep(i, a, n) for (int i = a; i < n; i++)
#define in(a, n) \
    vll a(n);    \
    re(i, n) cin >> a[i];
#define printV(a)         \
    for (int i : a)       \
        cout << i << " "; \
    cout << "\n";

ll Fibo_Rec(ll n, ll i)
{
    if (n < 2)
    {
        return n;
    }
    // cout << n << ' ' << i << endl;
    return Fibo_Rec(n - 1, i + 1) + Fibo_Rec(n - 2, i + 1);
}
ll Fibo_Loop(ll t)
{
    vll i(t, 0);
    i[0] = 0;
    i[1] = 1;
    for (ll z = 2; z <= t; z++)
    {
        i[z] = i[z - 1] + i[z - 2];
        // cout << i[z]   << ' ';
    }
    // printV(i);
    return i[t];
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    // cout << Fibo_Loop(t);
    if ((3736710778780434371 == 354224848179261915075 )== true)
    {
        cout << 'T';
    }
    else
    {
        cout << 'F';
    }
    
    return 0;
}
