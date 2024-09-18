import constants
import globals

def InitSq120To64AndSq64To120():
    sq = 0
    sq64 = 0
    for rank in range(constants.RANK.R1.value, constants.RANK.R8.value+1): # from rank 1 -> rank 8
        for file in range(constants.FILE.A.value, constants.FILE.H.value + 1): # from file A -> file H
            sq = constants.FR2SQ(file, rank) # calculating the square for 120 bit representation
            globals.Sq64ToSq120[sq64] = sq  # at 0 i.e A1 -> we put 21 i.e FR2SQ(file, rank) 120 bit representation of A1 is 21
            globals.Sq120ToSq64[sq] = sq64  # now sq has 21, so at sq in 120to64 array we put sq64
            sq64 += 1
    

def AllInit():
    InitSq120To64AndSq64To120()

