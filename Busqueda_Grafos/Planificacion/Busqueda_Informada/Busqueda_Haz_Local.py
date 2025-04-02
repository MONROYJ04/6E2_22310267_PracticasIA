def beam_search(graph, start, goal, heuristic, beam_width=2, max_depth=100):
    from heapq import heappush, heappop
    current_level = [(0 + heuristic[start], start, [start])]  # (g + h, node, path)
    visited = set()

    for _ in range(max_depth):
        next_level = []
        for f_score, node, path in current_level:
            if node == goal:
                return path
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                g_score = len(new_path)  # Costo real = número de pasos
                heappush(next_level, (g_score + heuristic[neighbor], neighbor, new_path))
        
        current_level = next_level[:beam_width]
    return None