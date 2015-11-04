import util

def depth_first_graph_search(problem):
    frontier=util.Stack()
    frontier.push((problem.getStartState(),[],0))
    explored=[]
    solution=[]
    while frontier:
        present_node=frontier.pop()
        if problem.isGoalState(present_node[0]):
            return solution
        else:
            explored.append(present_node[0])
            child_nodes=problem.getSuccessors(present_node[0])
            for child_node in child_nodes:
                if child_node[0] not in explored:
                    solution=present_node[1]+[child_node[1]]
                    path_cost=present_node[2]+1
                    frontier.push(child_node for child_node in child_nodes)
    return []
