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
 #           frontier.push(child_node for child_node in [node(problem.getSuccessors(present_node.state))] if child_node not in frontier and child_node.state not in explored]
            child_nodes=problem.getSuccessors(present_node[0])
            for child_node in child_nodes:
                if child_node[0] not in explored:
                    solution=present_node[1]+[child_node[1]]
                    path_cost=present_node[2]+1
                    frontier.push(child_node for child_node in child_nodes)
    return []

def depth_first_graph_search(problem):
  frontier=util.Stack()
  frontier.push((problem.getStartState(),[],0))
  explored=[]
  while frontier:
    present_node=frontier.pop()
    explored.append(present_node[0])
    if problem.isGoalState(present_node[0]):
      return present_node[1]
    else:
      child_nodes=problem.getSuccessors(present_node[0])
      for child_node in child_nodes:
        if child_node[0] not in explored:
          solution=present_node[1]+[child_node[1]]
          path_cost=child_node[2]
          frontier.push((child_node[0],solution,path_cost))
  return []

def uniformCostSearch()
  frontier=util.PriorityQueue
  frontier.push((problem.getStartState(),[],0),0)
  explored=[]
  cost_dict={}
  while frontier:
    present_node=frontier.pop()
    explored.append(present_node[0])
    if problem.isGoalState(present_node[0]):
      return present_node[1]
    else:
      child_nodes=problem.getSuccessors(present_node[0])
      for child_node in child_nodes:
        solution=present_node[1]+[child_node[1]]
        step_cost=child_node[2]
        path_cost=present_node[2]+child_node[2]
        if not cost_dict.has_key(child_node[0]):
          frontier.push((child_node[0],solution,step_cost),path_cost)
        elif cost_dict[child_node[0]]>path_cost:
          frontier.push((child_node[0],solution,step_cost),path_cost)
          cost_dict[child_node[0]]=path_cost
  return []
              
    
        
    
      
    
