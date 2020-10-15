<CsoundSynthesizer>
<CsOptions>
;-odac
-o out_file2.wav
</CsOptions>
; ==============================================
<CsInstruments>

sr	    =	96000
ksmps	=	20
nchnls	=	2
0dbfs	=	4

    instr 1
a1          oscil    p4, p5, p6
            outs     a1, a1
    endin

</CsInstruments>
; ==============================================
<CsScore>
; f tables
f1 0 16384 10 1                                          ; Sine
f2 0 16384 10 1 0.5 0.3 0.25 0.2 0.167 0.14 0.125 .111   ; Sawtooth

; p1   p2    p3   p4     p5     p6
; INS  STRT  DUR  AMP    FREQ   WAVESHAPE
i 1    0     2    0.5    440    1

</CsScore>
</CsoundSynthesizer>
