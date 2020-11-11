Clock.bpm = 55
Root.default.set("C")
Scale.default = "major"

rnd_amp = [PRand([0.2, 1])*.03*i for i in PRange(10)]
chop_sus1 = (PRand(4, 9)/5) * (PRand(1, 3)/2)
p1 >> ambi(PRand([1, 1, 2, 4, 7, 5, 8, 12])[:10] + 0, 
    dur=1,
    sus=chop_sus1,
    oct=4,
    amp=rnd_amp,
    room=.2,
    mix=0.7
    )
rndAmp2 = [PRand([0, 1])*.02*i for i in PRange(10)]
p2 >> ambi(PxRand([2, 6, 8, 4, 12])[:10] + 0, 
    dur=1,
    sus=PRand(4, 9)/5,
    oct=5,
    lpf=650,
    lpr=.5,
    amp=rndAmp2,
    room=1,
    mix=0.95
    )    
    
rnd_amp6 = [PRand([0, 1])*.005*i for i in PRange(10)]    
g1 >> glass(PxRand([2, 2, 4, 6, 6, 8, 9])[:10] + 0,
    dur=PRand(4, 8)/2,
    amp=rnd_amp6,
    sus=4,
    room=.5)
    

rnd_amp3 = [PRand([0, 1])*.2*i for i in PRange(10)]
k1 >> klank(PxRand([1, 4, 9, 7]) + 0,
    dur=PRand(4,8)/2,
    sus=4,
    oct=4,
    amp=rnd_amp3)
    

b1 >> blip(PxRand([1, 4, 9, 7]) + 0,
    dur=PRand(1,2)/4,
    sus=4,
    amp=rndAmp2).every(2, "stutter")
    
    
g1 >> gong(PRand([1, 4, 7, 9]) + 0,
    dur=PRand(4, 8)/2,
    chop=4,
    sus=4,
    oct=4,
    amp=rnd_amp3
    )
    
rnd_amp4 = [PRand([0, 1])*.05*i for i in PRange(10)]
k2 >> klank(PxRand([2, 2, 4, 6, 6, 8, 9]) + 2,
    dur=PRand(4, 8)/2,
    sus=4,
    oct=5,
    amp=rnd_amp4,
    room=1,
    mix=0.5)
    
k3 >> bass([1, 3, 7, 5, PRand(10, 12)] * 2,
    dur=PRand(1, 2)/4,
    oct=5,
    chop=chop_sus1,
    sus=chop_sus1,
    amp=rnd_amp4,
    blur=.2,
    lpf=1500,
    room=.5,
    mix=0.5,
    lpr=.8).every(15, "shuffle")

s1 >> space(PRand([1, 4, 7, 9]) + 0,
    dur=PRand(1,2)/4,
    oct=3,
    sus=4,
    amp=rnd_amp).every(2, "stutter").every(4, "shuffle")

rnd_amp5 = [PRand([0, 1])*.05*i for i in PRange(10)]    
b2 >> bell(PwRand([2, 2, 4, 6, 6, 8, 9], [2, 4]) + 0,
    oct=5,
    amp=rnd_amp5,
    sus=PRand(4, 8)/4,
    dur=PRand(2, 4)/2,
    lpf=750,
    formant=2,
    room=.3,
    mix=0.6, 
    )
    
p4 >> pluck(PxRand([2, 6, 8, 4, 12]) + 0,
    amp=rnd_amp5,
    chop=chop_sus1,
    sus=chop_sus1,
    formant=6,
    blur=.44,
    room=.3,
    dur=PRand(2, 4)/4).every(2, "stutter")
    
s4 >> space(PxRand([2, 2, 4, 6, 6, 8, 9]),
    amp=rnd_amp6,
    sus=4,
    room=.5)
    

Group(s1, s4).solo(0)
