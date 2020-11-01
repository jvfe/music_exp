bd >> play("x(x x)  ")

s1 >> soft((0, 2, 4, const(6)), dur=4) + var([0, 2], 8)

p2 >> karp([2,2,4, (8, 6)], dur=[1,1/2,1, 1], amp=[1,3/4,3/4])

s3 >> soft([2, 6, 4, (8, 2)], dur=[1, 1, 1, 1/2])

s4 >> glass([6, 8, [8, 6]], dur=[1, 1/2])

g2 >> glass([6, 8, (8, 6, 4)], dur=[1, 1/2])

p3 >> arpy([2, 4, [8, 6]], dur=[1, 1/2]) 



print(SynthDefs)


