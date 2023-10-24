##elimit.py should have been named eLimit.py I suppose, but it was my first program and I didn't know that.  I do not have the original file anymore, but I have tried to do it justice. When I first ran this on my school issued laptop, it took 45 minutes to complete elimit(75,000)

def elimit(number):
  x = 1
  while x < number:
    new = (1 + (1/x))^^x
    print("Current value of e: " + str(new))
    x++
  
