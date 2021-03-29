import rubik

"""
Using BFS, returns the number of cube configurations that are
exactly a given number of levels away from the starting position
(rubik.I), using the rubik.quarter_twists move set.
"""

def getPositionsFromPosition(position):
  #Returns a set of all positions  that can be reached within one quarter twist from position

  #The set which will contain the resulting positions
  positions = set()

  #Loop through all possible moves
  for move in rubik.quarter_twists:
    #Loop through each move, make the move from the given position
    #Save the resulting position in positions
    positions.add(rubik.perm_apply(move, position))

  #Return the resulting positions
  return positions

def positions_at_level(level):
  #Returns the number of positions at level levels away from a starting position
  #A map which tracks what level a given vertex is at
  levelMap = {rubik.I: 0}
  #Which level are we currently on?
  i = 1
  #The current frontier of vertices to be searched
  frontier = [rubik.I]

  #Keep looping as long as we have verticies in the frontier and we haven't surpassed level yet
  while len(frontier) > 0 and i <= level:
    #The next frontier to be searched
    next = []

    #Loop through all vertices in the current frontier
    for position in frontier:
      #Get all possible next positions from positon
      for nextPosition in getPositionsFromPosition(position):
        #If we haven't been to this positoin already
        if nextPosition not in levelMap:
          #Store nextPosition in levelMap so we know later that we've been here before
          levelMap[nextPosition] = i
          #Store nextPosition in next so we can inspect it in the next frontier
          next.append(nextPosition)
    #If this is the level that we're searching for
    if i == level:
      #Return how many nextPositions were discovered in this level
      return len(next)

    #This wasn't the level we were looking for, continue searching on the next level
    #Reset frontier to next
    frontier = next
    #Increment i (since we're moving on to the next level)
    i += 1

  #Only one vertex in the starting level
  return 1
