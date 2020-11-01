var.chords = var([2, 6, 4, (4, 8)], 4)

# Lets make some waves
n1 >> noise(P(PSine(32), PSine(12), PSine(28), PSine(17)*.7), 
    dur=8, 
    amp=P(.05,.15), 
    delay=P(PRange(5)/5))

z1 >> space(P[-6, -3, -4], amp=0.3, dur=8, delay=0.5)

g1 >> gong([2, 4], dur=4, delay=P(PRange(5)/5), amp=.8, oct=7)
    
b1 >> blip(var.chords + P[2, 7], dur=4, amp=.5, oct=5, delay=0.7)

k1 >> klank(var.chords, dur=4, amp=.7)

k1.stop()

k2 >> keys(var.chords, dur=4, amp=.5)

k3 >> keys([2,4], dur=2, amp=.4)

b1 >> bass(var.chords + P[2, 7], dur=4, amp=.3, oct=4)

k4 >> keys(var.chords, dur=PDur(3, 8), amp=.4)

d1 >> play("x    x ", amp=.3)


k2.stop()
k3.stop()
k4.stop()

b1.stop()

d1.stop()

g1.stop()

z1.solo()
