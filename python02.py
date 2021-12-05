def getFactorial(acc, start)
  acc = acc * getFactorial(acc, start - 1)
  return acc
