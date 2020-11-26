const Bfs = (graph, start, end,blocked) => {
    let queue = [[start]]
    let explored = []
    if (start === end) {
        console.log("No Path Available")
        return
    }
    while (queue.length > 0) {
        let path = queue.pop()
        let node = path[path.length - 1]
        if (!explored.includes(node) && !blocked.includes(node) ) {
            let neighbours = graph[node];
            for (let i = 0; i < neighbours.length; i++) {
                let new_path = [...path]
                new_path.push(neighbours[i])
                queue.push(new_path);
                if (neighbours[i] == end) {
                    console.log(...new_path)
                    return
                }
            }
        }
    }
    console.log("No Path")
    return
    // let queue = [start]
    // let n = Object.keys(graph).length
    // let parent = new Array(n).fill(-1)
    // parent[start] = start
    // let dist = new Array(n).fill(0)
    // let vis = new Array(n).fill(false)
    // while(queue.length > 0) {
    //     let v = queue[0]
    //     queue.shift()
    //     vis[v] = true
    //     for(let i = 0; i < graph[v].length; i++) {
    //         let u = graph[v][i]
    //         if(!blocked.includes(u) && !vis[u]) {
    //             queue.push(u)
    //             dist[u] = dist[v] + 1
    //             parent[u] = v
    //         }
    //     }
    // }
    // let path = []
    // let v = end
    // while(v != start) {
    //     path.push(v)
    //     v = parent[v]
    // }
    // path.push(start)


    // console.log(...path)
    // return dist[end]
}




const Array_To_Graph = (array) => {
    let graph = {}
    let hascal = 0;
    let offset = 0;
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array[0].length; j++) {
            let ss_ = ((i * (array[0].length - 1)) + j) + offset
            let neighbours = []
            if (j != 0) {
                neighbours.push(ss_ - 1)
            }
            if (j != array[0].length - 1) {
                neighbours.push(ss_ + 1)
            }
            if (i != 0) {
                neighbours.push(ss_ - array[0].length)
            }
            if (i != (array.length - 1)) {
                neighbours.push(ss_ + array[0].length)
            }
            graph[parseInt(hascal)] = neighbours;
            hascal++;
        }
        offset++;
    }
    // let ks = Object.keys(graph);
    return graph
}

// let array__ = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]];
// let graph_ = Array_To_Graph(array__);
// console.log(graph_)
// Bfs(graph_, 0, 8, [])
let graph = {
    'A': ['B', 'E', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E','F'],
    'E': ['A', 'B', 'D'],
    'F': ['C','G','D'],
    'G': ['C','F']
}
Bfs(graph, 'A', 'G',['C'])