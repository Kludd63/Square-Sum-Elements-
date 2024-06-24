#Gerbicz Proof

import time


from math import sqrt

#glues not included by the algorithim
from glues import glue

#get an index of small solutions for n
from small import small

#import a list of base cases s.t. each sequence starts with 1 and ends
# with 3(odd length) or 8(even length), and each number in the case maintains positional parity
from baseCases import Base


#"nice" pair check
start = time.time()
def isNice(P0,P1):
    #condition: both start with 1
    if P0[0] != 1 or P1[0] != 1:
        print("Start with 1")
        return False
    
    #condition: one ends with a 3 and one with an 8
    if (P0[-1] == 3 and P1[-1] == 8) or (P0[-1]==8 and P1[-1] == 3):
       for n in range(len(P0)): 
           #condition: parity is maintained
            if (P1.index(P0[n]) - n) % 2 != 0:
                print(f'parity issue {P0[n]},{n},{P1.index(P0[n])}')
                return False
            else:
                pass
    else: 
        print(f'wrong endpoints {P0[-1]},{P1[-1]}')
        return False
    
    return True
    
#check of the base cases in Base, "bases" is a list of base cases
def baseCheck(bases):
    for c in bases:
        pc = bases.index(c)
        if pc %2 ==0:
            if isNice(c,bases[(pc+1)]) != True:
                return False
    #print('Bases all work')
    return True



#glue check

def glueCheck(data):
    for g in data:
        #data[][][] is a list of lists of lists
        #the 1st tier is the list of all 196 glues
        #the 2nd list contains info on each individual glue
        #the 3rd list is one of two types, data[i][j][0] is general info, and data[i][j][1:74] contains specific info about a sequence
        #data[i][j][0] is structured as a list with 4 terms. the 1st is the scaling factor, 49, the 2nd is the base residual in question
        #the 3rd term is whether the n in 49n+res is even or odd, if 0, n is even, if 1, n is odd
        #the 4th term indicates the 'nice' pair, a 1 in this position indicates that this sequence is a 'nice' pair of the sequence before it
        #the data[i][j][1:74] lists are structured as such:
        #the 1st position indicates either the c(shift) value, or the integer(1-24) in that position
        #the 2nd position indicates whether the list is an integer or a scaled and shifted sequence, and if it is a sequence,
        #whether or not you reverse it. a 0 in this position indicates an integer, 1 indicates a sequence going forwards, -1 going backwards
        #the 3rd slot indicates the choice of short or long list, 0 being short, 1 being long

        if g[0][3]==0:
            

            #check parity of the input so that we know what endpoints to use
            #if g[-1][0]== 8:
            #    pari = 'e'
            #elif g[-1][0]== 3:
            #   pari = 'o'

            #create a functional path from each glue
            HP = []
            for p in g[1:74]:
                if p[1] == 0:
                    #add the integer to the sequence
                    HP.append(p[0])

                elif p[1] == 1:
                    #add the first term of the scaled chunk
                    HP.append(49+p[0])

                    #add the last number of the scaled chunk
                    if p[2]==0 and g[0][2] == 0:
                        HP.append(49*8-p[0])
                    elif p[2] ==0 and g[0][2] == 1:
                        HP.append(49*3 +p[0])
                    elif p[2]==1 and g[0][2] == 0:
                        HP.append(49*3 +p[0])
                    elif p[2]==1 and g[0][2] == 1:
                        HP.append(49*8 -p[0])

                
                elif p[1] == -1:
                    #if reversed, add the last number first 
                    if p[2]==0 and g[0][2] == 0:
                        HP.append(49*8-p[0])
                    elif p[2] ==0 and g[0][2] == 1:
                        HP.append(49*3 +p[0])
                    elif p[2]==1 and g[0][2] == 0:
                        HP.append(49*3 +p[0]) 
                    elif p[2]==1 and g[0][2] == 1:
                        HP.append(49*8 -p[0])

                    #add the first number second
                    HP.append(49+p[0])
        
        #check paths sums
        
            for n in HP:
                if n+1 <= len(HP):
                    if sqrt(HP[n]+HP[n+1]) % 1 != 0:
                        if abs(HP[n]-HP[n+1]) != 98:
                            return f"Break in Sum property at {g[0]}, the break was between {HP[n]} and {HP[n+1]}"
                            

            #create the same functional path, but add placeholders to maintain original parity
            HP =[]
            for p in g:
                if p[1] == 0:
                    HP.append(p[0])

                elif p[1] == 1:
                    HP.append(49+p[0])
                    if p[2]==0 and g[0][2] == 0:
                        HP.append(49*8-p[0])
                    elif p[2] ==0 and g[0][2] == 1:
                        #using '.' to create a space s. t. 49+p[0] and 49*3+p[0] have the same parity
                        HP.append('.')
                        HP.append(49*3 +p[0])
                    elif p[2]==1 and g[0][2] == 0:
                        HP.append('.')
                        HP.append(49*3 +p[0])
                    elif p[2]==1 and g[0][2] == 1:
                        HP.append(49*8 -p[0])

                
                elif p[1] == -1:
                    if p[2]==0 and g[0][2] == 0:
                        HP.append(49*8-p[0])
                    elif p[2] ==0 and g[0][2] == 1:
                        HP.append(49*3 +p[0])
                        HP.append('.')
                    elif p[2]==1 and g[0][2] == 0:
                        HP.append(49*3 +p[0])
                        HP.append('.')
                    elif p[2]==1 and g[0][2] == 1:
                        HP.append(49*8 -p[0])
                    HP.append(49+p[0])


            HP1 = []
            #create the same path, but with the alledged 'nice' pair
            for z in data[data.index(g)+1]:
                if z[1] == 0:
                    HP1.append(z[0])
                
                elif z[1] == 1:
                    HP1.append(49+z[0])
                    if z[2]==0 and g[0][2] == 0:
                        HP1.append(49*8-z[0])
                    elif z[2] ==0 and g[0][2] == 1:
                        HP1.append('.')
                        HP1.append(49*3 +z[0])
                    elif z[2]==1 and g[0][2] == 0:
                        HP1.append('.')
                        HP1.append(49*3 +z[0])
                    elif z[2]==1 and g[0][2] == 1:
                        HP1.append(49*8 -z[0])
                            
                        
                elif z[1] == -1:
                    if z[2]==0 and g[0][2] == 0:
                        HP1.append(49*8-z[0])
                    elif z[2] ==0 and g[0][2] == 1:
                        HP1.append(49*3 +z[0])
                        HP1.append('.')
                    elif z[2]==1 and g[0][2] == 0:
                        HP1.append(49*3 +z[0])
                        HP1.append('.')
                    elif z[2]==1 and g[0][2] == 1:
                        HP1.append(49*8 -z[0])
                    HP1.append(49+z[0])


            #check for 'nice' pair
            if HP[0] != 1 or HP1[0] != 1:
                return "Please start with 1"
    
                #condition: one ends with a 3 and one with an 8
            if (HP[-1] == 3 and HP1[-1] == 8) or (HP[-1]==8 and HP1[-1] == 3):
                for n in range(len(HP)): 
                    #condition: parity is maintained
                    if (HP[n] in HP1) and HP[n] !='.':
                            if (HP1.index(HP[n]) - n) % 2 != 0:
                                return f'{g[0]}parity issue {n},{HP[n]},{HP1.index(HP[n])},{HP},{HP1}'
                            else:
                                pass
            else: 
                return f'{g[0]}endpoint issue {HP[-1]},{HP1[-1]}, {HP}'
                
                
    return "Glues Checked"




# generate a Gerbicz path based on one of the HCs in the list, m in the range from 41-2032, and res from 24-72
def genGerbicz(m:int ,res:int, data:list, bases:list, sf:int, cm:int, np:bool):
    #define the possible shifts 'c'
    C = [*range(-cm, cm+1)]
    #create our shifted 'nice' pair
    NP0 = []
    NP1 = []
    #determine parity of m, 0 for even, 1 for odd
    if m%2 ==0:
        pari = 0
    elif m%2 ==1:
        pari = 1
    

    if m <= 2032:
        
        #scale the base sequences
        for s in bases[2*(m-41)]:
            NP0.append(sf*s)
        
        for s in bases[2*(m-41)+1]:
            NP1.append(sf*s)

    #or generate bases and scale them if not already in Base
    elif m > 2032:
        for re in range(24,73):
            if ((m-re)/49)%1 ==0:
                k = (m-re)//49
                for s in genGerbicz(k, re, glue, Base, sf, cm, 0):
                    NP0.append(sf*s)
                

                for s in genGerbicz(k, re, glue, Base, sf, cm, 1):
                    NP1.append(sf*s)
                

                

                
                
    #shift the thingamadoobers around
    NP0f =[]
    NP1f =[]
    for c in C:
        NP0t =[]
        NP1t =[]

        #give us the ajusted nice pair for both pairs
        for po in range(1, len(NP0)+1):
            if (po % 2) == 1: 
                NP0t.append(NP0[po-1]+c)
            else: 
                NP0t.append(NP0[po-1]-c)
            
        for po in range(1, len(NP1)+1):
            if (po % 2) == 1: 
                NP1t.append(int(NP1[po-1])+c)
            else: 
                NP1t.append(int(NP1[po-1])-c)

        NP0f.append(NP0t)
        NP1f.append(NP1t)

        #find the glue pattern
    for b in data:
        if [sf, res, pari, np] in b:
            i = data.index(b)
            break
        #translate the sequences through the glue patterns
    FinG = []
    for p in data[i][1:74]:
        NP0t = NP0f[p[0]+24]
        NP1t = NP1f[p[0]+24]
        if p[1] ==0:
            FinG.append(p[0])

        elif p[1] ==1:
            if p[2]==0:
                for n in NP0t:
                    FinG.append(n)
            elif p[2]==1:
                for n in NP1t:
                    FinG.append(n)
                

        elif p[1] ==-1:
            NP0t.reverse()
            NP1t.reverse()
            if p[2]==0:
                for n in NP0t:
                    FinG.append(n)
            elif p[2]==1:
                for n in NP1t:
                    FinG.append(n)
    #make sure that the sequence works
    for d in FinG: 
        if sqrt(d+FinG[FinG.index(d)-1]) %1 !=0: 
            return f"Break in square property at {FinG[FinG.index(d)-1]},{d}"
    for s in range(1,49*m+res+1):
        if s not in FinG:
            return f'missing{s}'
    if (49*m+res+1) in FinG and np == 0:
        return f'Extra numbers'

    return FinG


            

#find a Parkers Square Sum Path for a number n, bases wants the base cases, and view asks if you want
#to see the unreasonably long list of numbers for huge n
def ParkPath(n:int, bases:list, view:bool):

    #exeptions for failed cases
    fail = {*range(1,15),18,19,20,21,22,24}
    if n < 1 or n %1 !=0:
        return f'Number must be a strictly positive integer'
    elif n in fail:
        return f'No path possible for {n}'

    #use algorithm to make path for big n
    elif n > 2032:
        for res in range(24,73):
            if ((n-res)/49)%1 ==0:
                m = ((n-res)//49)
                FinG = genGerbicz(m, res, glue, Base, 49, 24, 0) 
                if view == False:
                    return f'Sequence exists, and is very long. If you wish to see it, use "print(ParkPath(n,Base,True)" if you dare'
                elif view == True:
                    return f'You asked for it: {FinG}'

    #if n in base cases, return the base case                
    elif n > 40:
        FinG = []
        for i in Base[2*n-41]:
            FinG.append(i)
        return FinG
    
    elif n < 40: 
        FinG =[]
        for s in small:
            if s[0]==n:
                for d in s[1]:
                    FinG.append(d)
        return FinG
        

print(ParkPath(1000000,Base, False))
end = time.time()
print(end-start)
