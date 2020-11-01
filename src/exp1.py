bd >> play("x( x)  ")
hh >> play("---[--]")
sn >> play("  o ")
p1 >> play("|x[12]| o ")

s1 >> swell((0, 2, 4, const(6)), dur=4) + var([0, 1], 8)

Scale.default = "major"

p1 >> pluck([0,4,2, (6, 8)], dur=[1,1/2,1/2], amp=[1,3/4,3/4])

