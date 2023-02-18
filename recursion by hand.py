stack = []
stack.append({'n': int(input()), 'prevFac': '?', 'labelFrom': 0})
while len(stack) > 0:
    localVars = stack[-1]
    labelFrom = localVars['labelFrom']
    if labelFrom <= 0:
        if localVars['n'] == 1:
            returnedValue = 1
            stack.pop()
            continue
        localVars['labelFrom'] = 1
        stack.append({'n': localVars['n'] - 1, 'prevFac': '?', 'labelFrom': 0})
        continue
    if labelFrom <= 1:
        localVars['prevFac'] = returnedValue
        returnedValue = localVars['n'] * localVars['prevFac']
        stack.pop()
        continue
    print(returnedValue)
