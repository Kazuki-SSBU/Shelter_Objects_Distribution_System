from itertools import product
from collections import defaultdict
from distribution.models import RequestData

def get_data():
    """
    分配を計算するのに必要な情報をDBから持ってくる関数

    出力
    data: データ {"アイテム名": {"shelters": {"避難所名": 希望個数, ...}, "warehouses": {"倉庫名": 在庫数, ...}}, ...}
    """



def destribution_calculater(shelters: dict[str, int], warehouses: dict[str, int], transportable_pair: set[tuple[str, str]] = None):
    """
    入力
    shelters: 避難所 {"避難所名": 希望個数, ...}
    warehouses: 倉庫 {"倉庫名": 在庫数, ...}

    transportable_pair: 輸送可能な避難所・倉庫のペア {("避難所名", "倉庫名"), ...}


    出力
    transport_data: [{"from": "倉庫名", "to": "避難所名", "num": 出荷数}, ...]

    アルゴリズム
    二部グラフの最大フローをベースのアルゴリズム．
    →物資を最大限に利用できるが，配分に偏りが生じてしまう...?(要解決)
    →balanced flowの先行研究はあるが，時間の都合省略．
    """
    #グラフの作成
    vertices = {"source", "sink"} | set(shelters.keys()) | set(warehouses.keys())
    edges = {v: dict() for v in vertices}
    if transportable_pair != None:
        for shelter, warehouse in transportable_pair:
            assert shelter in shelters
            assert warehouse in warehouses
            edges[warehouse][shelter] = float("inf")
    else:
        for shelter, warehouse in product(shelters, warehouses):
            edges[warehouse][shelter] = float("inf")

    edges["source"] = shelters
    for shelter, num in shelters.items():
        edges[shelter]["sink"] = num
    
    #フローの計算
    Graph = MaxFlow(edges)
    Graph.ford_fulkerson("source", "sink")
    transport_data = []
    for shelter, warehouse in product(shelters, warehouses):
        transport_data.append({"from": warehouse, "to": shelter, "num": Graph.calculate_edge_flow(warehouse, shelter)})
    
    return transport_data
    

    


class MaxFlow:
    def __init__(self, graph: dict[str, dict[str, int]]):
        """
        入力
        graph: 隣接リスト {v: {w: capacity, ... }, ...}
        """
        self.graph = graph
        self.residual_graph = defaultdict(dict)
        self.build_residual_graph()

    def build_residual_graph(self):
        """
        残余グラフの構築
        """
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                self.residual_graph[u][v] = capacity
                self.residual_graph[v].setdefault(u, 0)  # 逆方向のエッジを追加（初期は容量0）

    def bfs(self, source, sink, parent):
        """
        残余グラフ上で経路探索
        """
        visited = set()
        queue = [source]
        visited.add(source)

        while queue:
            u = queue.pop(0)

            for v, capacity in self.residual_graph[u].items():
                if v not in visited and capacity > 0:  # 残余容量があるエッジを探索
                    parent[v] = u  # 親ノードを記録
                    if v == sink:
                        return True
                    queue.append(v)
                    visited.add(v)

        return False

    def ford_fulkerson(self, source, sink):
        parent = {}
        max_flow = 0

        # 増加パスがある間ループ
        while self.bfs(source, sink, parent):
            # 増加パスで流せるフローの最小値を見つける
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.residual_graph[u][v])
                v = u

            # 残余グラフを更新
            v = sink
            while v != source:
                u = parent[v]
                # フローを減少
                self.residual_graph[u][v] -= path_flow
                # 逆方向のエッジの容量を増加
                self.residual_graph[v][u] += path_flow
                v = u

            # パスフローを最大フローに加算
            max_flow += path_flow

        return max_flow
    
    def calculate_edge_flow(self, start: str, end: str) -> int:
        """
        入力
        start: 始点 v
        end: 終点 w

        出力
        辺(v, w)を流れるフロー
        """
        if start not in self.graph or start not in self.residual_graph or end not in self.graph[start] or end not in self.residual_graph[start]:
            return 0
        return self.graph[start][end] - self.residual_graph[start][end]

if __name__ == "__main__":
    #MaxFlowのテスト
    #test1
    graph1 = {"0":{"1": 2, "2": 4, "3": 1},
             "1":{"4": 100, "6": 100},
             "2":{"4": 100},
             "3":{"5": 100},
             "4":{"7": 1},
             "5":{"7": 3},
             "6":{"7": 1},
             "7":dict()
             }
    G1 = MaxFlow(graph1)
    print(G1.ford_fulkerson("0", "7"))
    for u in G1.residual_graph:
        print(f"{u}: {G1.residual_graph[u]}")
    print(G1.calculate_edge_flow("3","5"), G1.calculate_edge_flow("2","4"), G1.calculate_edge_flow("1","4"))
    
    #test2
    graph2 = {"0":{"1": 3, "2": 2, "3": 5, "4": 8},
             "1":{"5": 100, "6": 100, "7": 100},
             "2":{"5": 100, "6": 100, "7": 100},
             "3":{"6": 100, "7": 100, "8": 100},
             "4":{"7": 100, "8": 100},
             "5":{"9": 4},
             "6":{"9": 8},
             "7":{"9": 10},
             "8":{"9": 5},
             "9":dict()
             }
    G2 = MaxFlow(graph2)
    print(G2.ford_fulkerson("0", "9"))
    for u in G2.residual_graph:
        print(f"{u}: {G2.residual_graph[u]}")
    for i, j in product(range(1, 5), range(5, 9)):
        print(f"{i}->{j}:{G2.calculate_edge_flow(str(i), str(j))}")