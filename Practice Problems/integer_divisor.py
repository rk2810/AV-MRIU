# l and r are two numbers , find the integer divisor from l to r inclusive that occurs maximum times
l = raw_input("Enter l : ")
r = raw_input("Enter r : ")
l = int(l)
r = int(r)

if r < l:
    print "Invalid" 
    exit()
if l is r: # when l and r are same
    print l
    exit()
else: # since every second number is even number, the occurrence of 2 must be max in all cases
    print '2'
