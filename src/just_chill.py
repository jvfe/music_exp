Clock.bpm=100; Scale.default="major"

p1 >> charm([1, 5, 3, 9], dur=2, room=7, sus=3, tremolo=4, echo=2, amp=.4, pan=linvar((1, -1), 8)) + (1, 3, const(9))

p2 >> pads(P[(1,7), (1,7), (3,9), (3,9)], dur=4, amp=.4, fmod=2, room=4, blur=2, coarse=2)

g1 >> glass([1], dur=4, room=4, fmod=2, blur=2)

m1 >> marimba([3, 5, 1, 7, 3], dur=PDur(3, 8), room=3, tremolo=2).shuffle()

p3 >> donk([1, 9], dur=PDur(3, 8), formant=.4, blur=2, room=4, echo=2).every(2, "shuffle")
d1 >> play("(x )( x)o{ vx[xx]}", crush=16, rate=.8).every([24,5,3], "stutter", 4, dur=3)
d2 >> play("<-s>< ~*~>").every(30.5, "jump", cycle=32)

s1 >> sinepad([1], dur=8, amp=.4)

s2 >> spark([1, 5, 3], amp=.2, dur=4, chop=4, sus=4).every(2, "stutter")

a1 >> ambi([[9, 4, 2, 1], [1, 5, 2, 7]], dur=8, sus=4, room=3)

g1.stop()
Group(p1, p2).solo()


