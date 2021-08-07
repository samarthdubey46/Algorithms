#include <bits/stdc++.h>
using namespace std;

class Graph
{
    int V;
    vector<int> *adj;

public:
    Graph(int V)
    {
        this->V = V;
        adj = new vector<int>(V);
    }
    void DFSUtil(int v, bool visited[])
    {
        visited[v] = true;
        cout << v;
        vector<int>::iterator i;
        for (i = adj[v].begin(); i != adj[v].end(); ++i)
        {
            if (!visited[*i])
            {
                DFSUtil(*i, visited);
            }
        }
    };

public:
    void addEdge(int v, int w)
    {
        adj[v].push_back(w);
    };
    void DFS()
    {
        bool *visited = new bool[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;
        for (int i = 0; i < V; i++)
            if (visited[i] == false)
                DFSUtil(i, visited);
    };
};
int main()
{
    Graph g = Graph(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    g.DFS();

    return 0;
}