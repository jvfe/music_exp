
var.chords = var([0, 4, 2, (6, 8)], 8)

var.chords2 = var([0, 2, 4, [6, 8]], 8)

k1 >> klank([4, 2], dur=4, amp=.5)

p1 >> glass(0, dur=8, amp=.3)

n1 >> blip(4, dur=8, amp=.2)

s1 >> swell(2, dur=8, amp=.2)

s2 >> space(var.chords2, dur=8, amp=.4)

v1 >> viola(var.chords2, dur=8, amp=.2)

b1 >> jbass(var.chords, dur=PDur(4, 8), amp=.4)


d3 >> play("V o-", amp=.2)

d2 >> play("x V", amp=.3)

d1 >> play("x [--] x", amp=.5)


p2 >> keys(var.chords, dur=8, amp=1)



d3.stop()
d2.stop()
d1.stop()
