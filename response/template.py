mcnp_template = '''Bonner Sphere Template
c
c ******************************************************************************
c                               CELL CARDS
c ******************************************************************************
c
c                          -----Beam Port------
1 0         11 -13 -21         IMP:N=1  {}     $ Inside Collimator
2 1 -2.699  11 -13  21 -22     IMP:N=1             $ Al Tube (Collimator)
3 6 -1.300  11 -12  22 -23     IMP:N=1             $ Borated Poly Wrapping
4 0         12 -13  22 -23     IMP:N=1             $ Borated Poly Missing
5 0       (-11) : (11 -13 23)  IMP:N=0             $ Coreside and Radial Graveyard
6 0         13                 IMP:N=1  {}     $ Mouthside Graveyard
c
c
c                          -----Bonner Sphere------
111 2  -0.95    (-101 -111):
                (-101  111 -115 124):
                (-101  115 -117 125):
                (-101  117 126)         U=1  IMP:N=1        $ HDPE Sphere
121 11 -3.84     -121  113 -114         U=1  IMP:N=1        $ Detector Assembly
122 0           ( 112 -113 -122):
                ( 113 -114 121 -122)    U=1  IMP:N=1        $ Vacuum Around Crystal
123 12 -2.50    (-122  114 -116):
                (-123  116 -118)        U=1  IMP:N=1        $ PMMA Light Guide
124  1 -2.699   (-124  111 -112):
                (-124  122  112 -115):
                (-125  115 -116 122):
                (-125  116 -117 123):
                (-126  117 -118 123):
                (-126  118 -119 127)    U=1  IMP:N=1        $ Aluminum Casing
125 0            -127  118 -119         U=1  IMP:N=1        $ PMT Vacuum
190 0           (101 -199 124  111 -115):
                (101 -199 125  115 -117):
                (101 -199 126  117 -119):
                (101 -199  119):
                (101 -199 -111)         U=1  IMP:N=1        $ Air Around Sphere
199 0                 199               U=1  IMP:N=0        $ Graveyard
c
c
c                          -----Foil Tube------
201  1 -2.699   201 -202 211 -223                          U=2  IMP:N=1        $ Aluminum Tube
202  0         (-299 -211):(-299 202 211 -223):(-299 223)  U=2  IMP:N=1        $ Space outside everything
203  0           299                                       U=2  IMP:N=0        $ Graveyard
{}c
c
c                          -----Wire Tube------
c
c
c                          -----Graveyard------
401 0   -401      U=4   IMP:N=0   $ These two cells are just used
402 0    401      U=4   IMP:N=0   $ to produce a graveyard universe.

c ******************************************************************************
c                               SURFACE CARDS
c ******************************************************************************
c                          -----Beam Port------
11 PX     0.0     $ BP Inner
12 PX    45.0     $ BP Outer
13 PX    50.0     $ Outside Wall
21 CX    0.9525   $ Al Inner
22 CX    1.27     $ Al Outer, BP Inner
23 CX    10.16    $ BP Outer
c
c
c                          -----Bonner Sphere------
101 1 SO    {:6.4f}          $ Bonner Sphere
c
111 1 PX   -0.9             $ plane tip top
112 1 PX   -0.7             $ plane tip bot
113 1 PX   -0.2             $ plane crystal top
114 1 PX    0.2             $ plane crystal bot
115 1 PX    3.6             $ plane 1.5
116 1 PX    3.8             $ plane 1.6
117 1 PX    9.6             $ plane 1.7
118 1 PX   10.8             $ plane 1.8
119 1 PX   19.1             $ plane 1.9
c
121 1 CX    0.20            $ cylinder 1.1
122 1 CX    0.50            $ cylinder 1.2
123 1 CX    0.60            $ cylinder 1.3
124 1 CX    0.70            $ cylinder 1.4
125 1 CX    0.90            $ cylinder 1.5
126 1 CX    2.54            $ cylinder 1.6
127 1 CX    2.14            $ cylinder 1.7
c
c
199 1 SO   50.0             $ graveyard
c
c
c                          -----Foil Tube------
201 2 CX  0.8525               $ tube inner rad
202 2 CX  0.9524               $ tube outer rad
203 2 CX  0.2500               $ foil chamber rad
c
{}c
c
299 1 SO   80.0             $ graveyard
c
c                          -----Wire Tube------
c
c
c                          -----Graveyard------
401 SO 1                   $ A sphere

c ******************************************************************************
c                               DATA CARDS
c ******************************************************************************
NPS 5e9
c
c  -----------------------------------------------------------------------------
c                                                          Transformations
c  -----------------------------------------------------------------------------
TR1  75 0 0
TR2  50.01 0 0
c
c  -----------------------------------------------------------------------------
c                                                     SOURCE SPECIFICATIONS
c  -----------------------------------------------------------------------------
SDEF    PAR=1
        POS=50.001 0 0
        AXS=1 0 0
        EXT=0
        VEC=1 0 0
        RAD=D1
        ERG=D2
        DIR=FERG=D3
c
SI1   {}  {}
SP1 -21  1
{}c
c  -----------------------------------------------------------------------------
c                                                          MATERIAL CARDS
c  -----------------------------------------------------------------------------
c  -----------------------------------------------------------------------------
c  MATERIAL 1:      Al
c  ---------------------------(density 2.699 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M1  13027.70c   -1
c
c  -----------------------------------------------------------------------------
c  MATERIAL 2:      HDPE
c  ---------------------------(density 0.950 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M2     1001     -0.143
       6000     -0.857
MT2    poly.10t
c  -----------------------------------------------------------------------------
c  MATERIAL 3:      ABS
c  ---------------------------(density 1.070 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M3     1001     -0.0811
       6000     -0.85260563
       7014     -0.0662911
c  -----------------------------------------------------------------------------
c  MATERIAL 4:      Poly
c  ---------------------------(density 1.300 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M4     1001     -0.05595
       6000     -0.5035887
       8000.70c -0.4404612
c  -----------------------------------------------------------------------------
c  MATERIAL 5:      In
c  ---------------------------(density 7.310 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M5    49000     -1
c
c  -----------------------------------------------------------------------------
c  MATERIAL 6:      Borated Poly
c  ---------------------------(density 1.000 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M6    1001       -0.125355
      5010.70c   -.100000
      6000       -.774645
c
c  -----------------------------------------------------------------------------
c  MATERIAL 7:      Cadmium
c  ---------------------------(density 8.65 g/cm^3)-----------------------------
c  -----------------------------------------------------------------------------
M7    48000     -1
c
c  -----------------------------------------------------------------------------
c  MATERIAL 8:      Gad
c  ---------------------------(density 7.90 g/cm^3)-----------------------------
c  -----------------------------------------------------------------------------
M8   64000      -1
c
c  -----------------------------------------------------------------------------
c  MATERIAL 9:      Au
c  ---------------------------(density 19.30 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M9   79197      -1
c
c  -----------------------------------------------------------------------------
c  MATERIAL 10:      Moly
c  ---------------------------(density 10.28 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M10   42000      -1
c
c
c  -----------------------------------------------------------------------------
c  MATERIAL 11:      LiI(Eu)
c  ---------------------------(density 3.84 g/cm^3)-----------------------------
c  -----------------------------------------------------------------------------
M11    3006.70c -0.0518
      53127.70c -0.9482
c
c  -----------------------------------------------------------------------------
c  MATERIAL 12:      PMMA Light Pipe
c  ---------------------------(density 7.858 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M12    1001     -0.08
       6000     -0.60
      16000     -0.32
c
c  -----------------------------------------------------------------------------
c                                                             TALLY CARDS
c  -----------------------------------------------------------------------------
c
c  -----------------------------------------------------------------------------
c  TALLY 124:      Light Creation within Li in Lithium Crystal
c  -----------------------------------------------------------------------------
c                               -----cell tally in crystal region
F124:N 121
c
c                               -----tally multiplier
c     Constant of proportionality | material  | 105 is (n,t) reaction of Li-6
FM124: 1 11 105
FT124  SCX 2
c
c  -----------------------------------------------------------------------------
c  TALLY 134-374:      Foil Tube
c  -----------------------------------------------------------------------------
{}c
c
c ******************************************************************************
c                             END OF INPUT FILE
c ******************************************************************************
'''
