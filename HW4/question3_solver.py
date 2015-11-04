import sys
class Question3_Solver:
    def __init__(self):
        return;

    # Add your code here.
    # Return the centroids of clusters.
    # You must use [(30, 30), (150, 30), (90, 130)] as initial centroids
    def solve(self, points):
        centroids=[(30, 30), (150, 30), (90, 130)]
#        centroids = [(30, 60), (150, 60), (90, 130)]
        old_centroids=[(0,0),(0,0),(0,0)]
        while not is_end(centroids,old_centroids):
	#for i in range(1, 100):
            old_centroids=centroids
            centroids=update(points,centroids)
        return centroids


def is_end(old,new):
    sum=0
    L=len(old)
    for i in range(L):
        sum=sum+caldistance(old[i],new[i])
        if sum==0:
            return True
    return False
    '''
    return set(old)==set(new)
    '''


def update(points,centroids):
    dataclustered=[[],[],[]]
    for i in range(len(points)):
        tempdis=float("inf")
        templabel=-1
        for j in range(len(centroids)):
            dis=caldistance(points[i],centroids[j])
            if dis<tempdis:
                tempdis=dis
                templabel=j
        dataclustered[templabel].append(points[i])
        
    for p in range(len(centroids)):
        centroids[p]=calcenter(dataclustered[p])

    return centroids


def caldistance(a,b):
    d=((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    return d

def calcenter(data):
    '''
    l=len(data)*1.0
    x=1
    y=1
    for item in data:
        x=x*item[0]
        y=y*item[1]
    x=x**(1.0/l)
    y=y**(1.0/l)
    return (x,y)
    '''
    l=len(data)
    x=0
    y=0
    for item in data:
        x=x+item[0]
        y=y+item[1]
    x=x/l
    y=y/l
    return (x,y)



