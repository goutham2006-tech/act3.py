def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[a].append(b)
    # 0=unvisited, 1=visiting, 2=visited
    state = [0] * numCourses

    def dfs(node):
        if state[node] == 1:
            return False  # cycle detected
        if state[node] == 2:
            return True
        state[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        state[node] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

# Test Cases
print("Test 1:", canFinish(2, [[1,0]]))           # Expected: True
print("Test 2:", canFinish(2, [[1,0],[0,1]]))     # Expected: False
