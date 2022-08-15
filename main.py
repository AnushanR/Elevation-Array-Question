# loop through the array and find the current water at each point via the following equation cw = min(maxL,maxR)-currentHeight
# Before moving to the next element, if maxL < currentHeight then MaxL = currentHeight 
#[0,1,0,2,1,0,3,1,0,1,2]
def Bf(arr):
  total = 0 


  for i in range(0,len(arr)-1):
    leftPointer = i 
    rightPointer = i 
    maxL = 0   
    maxR = 0 
    while leftPointer > 0:
      maxL = max(maxL,arr[leftPointer])
      leftPointer = leftPointer - 1

    while rightPointer < len(arr):
        maxR = max(maxR,arr[rightPointer])
        rightPointer = rightPointer + 1
    print(maxR,maxL,arr[i])
  

    waterToAdd = min(maxR,maxL)-arr[i]
    if waterToAdd > 0:
      total += waterToAdd
  return total

print(Bf([0,1,0,2,1,0,3,1,0,1,2]))

def doublePointer(arr):
  pointerLeft = 0 
  pointerRight = len(arr)-1
  maxLeft = 0 
  maxRight = 0 
  total = 0 

  while pointerLeft != pointerRight:
    if arr[pointerLeft] > arr[pointerRight]:
      workingPointer = pointerRight
    else:
      workingPointer = pointerLeft
    if workingPointer == pointerLeft:
      if maxLeft > arr[workingPointer]:
        total += maxLeft - arr[workingPointer]
      else:
        maxLeft = arr[workingPointer]
      pointerLeft = pointerLeft + 1
    else:
      if maxRight > arr[workingPointer]:
        total += maxRight - arr[workingPointer]
      else:
        maxRight = arr[pointerRight]
      pointerRight = pointerRight - 1
  return total

print(doublePointer([0,1,0,2,1,0,3,1,0,1,2]))
        