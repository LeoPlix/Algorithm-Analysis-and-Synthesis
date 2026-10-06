#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, m1, m2, K;
    if (!(cin >> N)) return 0;
    cin >> M >> m1 >> m2 >> K;

    // Graph construction (Adjacency list + Indegree for TopoSort)
    vector<vector<int>> adj(N+1);
    vector<int> indeg(N+1, 0);
    for (int i = 0; i < K; ++i) {
        int a, b; cin >> a >> b;
        adj[a].push_back(b);
        indeg[b]++;
    }

    // Topological Sort (Kahn's Algorithm)
    queue<int> q;
    for (int i = 1; i <= N; ++i) {
        if (indeg[i] == 0) q.push(i);
    }

    vector<int> topo;
    topo.reserve(N);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        topo.push_back(u);
        for (int v : adj[u]) {
            if (--indeg[v] == 0) q.push(v);
        }
    }
    
    int R = m2 - m1 + 1;
    vector<vector<pair<int,int>>> truck_routes(R);

    // DP setup: 'ts' acts as a version ID to avoid clearing vectors repeatedly
    vector<int> dp_mod(N+1);
    vector<int> visit_time(N+1, 0);
    int ts = 0;

    // Outer loop: Consider every node 's' as the start of a route
    for (int s : topo) {
        ++ts;
        visit_time[s] = ts;
        dp_mod[s] = 1; // Base case: 1 path from s to s
        
        // Inner loop: Propagate path counts following topological order
        for (int u : topo) {
            if (visit_time[u] != ts) continue; // Skip unreachable nodes
            for (int v : adj[u]) {
                if (visit_time[v] != ts) {
                    visit_time[v] = ts;
                    dp_mod[v] = 0;
                }
                // Transition: paths(s->v) += paths(s->u) % M
                dp_mod[v] = (dp_mod[v] + dp_mod[u]) % M; 
            }
        }

        // Assign route (s -> t) to the correct truck based on total paths
        for (int t = 1; t <= N; ++t) {
            if (t == s || visit_time[t] != ts) continue; 
            
            int truck_num = 1 + dp_mod[t];
            
            // Store if truck is within the required range [m1, m2]
            if (truck_num >= m1 && truck_num <= m2) {
                truck_routes[truck_num - m1].push_back({s, t}); 
            }
        }
    }

    // Output: Sort routes lexicographically and print
    for (int i = 0; i < R; ++i) { 
        auto &vec = truck_routes[i];
        sort(vec.begin(), vec.end());
        cout << "C" << (m1 + i);
        for (const auto &p : vec) {
            cout << " " << p.first << "," << p.second;
        }
        cout << "\n";
    }
    return 0;
}