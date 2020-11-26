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

int main()
{
// #ifndef ONLINE_JUDGE
//     freopen("input.txt", "r", stdin);
//     freopen("output.txt", "w", stdout);
// #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t,n_1 = 0,n_2 = 0;
    cin >> t;
    vll l;
    in(a,t);
    sort(a.begin(),a.end(),greater<ll>());
    // a.reserve();
    cout << a[0] * a[1];
    // printV(a);
    // cout << n_1 << " " << n_2;
    
    return 0;
}
