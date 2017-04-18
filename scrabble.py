vrecka={'Č': 1, 'A': 10, 'C': 1, 'B': 2, 'E': 11, 'D': 4, 'G': 2, 'F': 1, 'I': 9, 'H': 1, 'K': 3, 'J': 4, 'M': 2, 'L': 4, 'O': 8, 'N': 7, 'P': 2, 'S': 6, 'R': 6, 'U': 2, 'T': 4, 'V': 4, 'Z': 2, 'Š': 1, 'Ž': 1}
vrednost={'Č': 5, 'A': 1, 'C': 8, 'B': 4, 'E': 1, 'D': 2, 'G': 4, 'F': 10, 'I': 1, 'H': 5, 'K': 3, 'J': 1, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'P': 3, 'S': 1, 'R': 1, 'U': 3, 'T': 1, 'V': 2, 'Z': 4, 'Š': 6, 'Ž': 10}
with open('igralna_plosca.txt', mode='r') as f: #f=open(...)
      vnos = f.read()
#samodejno f.close()





plosca=vnos.strip('\n').split('\n')
for indVrst in range(len(plosca)):
     plosca[indVrst]=list(plosca[indVrst])

'''#_______________vaje
plosca[0][0]='Ž'

for znj in range(15):
      plosca[znj][11]='C'

for i in range(15):
      for j in range(15):
            if (i+j)%2==0:
                  plosca[i][j]='S'

#___________________ '''

print('''#________branje posamezne vrstice:
#beseda, smer (D ali R), koordinata vrstice(0 - 14), korrdinata stolpca(0 - 14)
#primer:
#morje, D, 4, 5
#za prikaz ploske napiši: pokazi, d, 0, 0''')
def preberi_vnos():
     vnos = input().split(', ')
     vnos[2]=int(vnos[2])
     vnos[3]= int(vnos[3])
     return vnos

def vpisi_v_plosco(beseda, smer, vr, st):

     #določi smer
     if smer == 'R':
          vrDodaj=0
          stDodaj=1
          '''
     if smer == 'L':
          vrDodaj=0
          stDodaj=-1
          '''
     elif smer == 'D':
          vrDodaj=1
          stDodaj=0
          '''
     if smer == 'U':
          vrDodaj=-1
          stDodaj=0
          '''
     #preveri ustreznost:
     enak = False
     tempVr = vr
     tempSt = st
     for znj in range(len(beseda)):

          #pregledam robove
          if tempVr <= -1 or tempSt <= -1 or tempVr >= 15 or tempSt >= 15:
                print("Napaka!")
                raise IndexError('padel si s plošče')

          #pregledam zasedenost

          if plosca[tempVr][tempSt]=='%' or plosca[tempVr][tempSt] == beseda[znj]:
               if plosca[tempVr][tempSt] == beseda[znj]:
                    enak = True
          else:
               raise ValueError('Polje je zasedeno z drugo črko')

          #tockovanje
          

          tempVr += vrDodaj
          tempSt += stDodaj
          

     if enak == True:
          #zapiši v tabelo
          for znj in range(len(beseda)):
               plosca[vr][st] = beseda[znj]
               vr += vrDodaj
               st += stDodaj
     else:
          raise ValueError('Tvoja beseda se ne dotika drugih besed')
     #konec funkcije (dodam besedo v ploščo)

def prikazi_plosco():
    print(plosca)
    return

for i in range(5):
    
    #začetek funkcije (poberem novo besedo)
    vnos = preberi_vnos()
    #.upper() naredi velike črke
    beseda1 = vnos[0].upper()
    smer = vnos[1].upper()
    vr = vnos[2]
    st = vnos[3]

    if beseda1 == "POKAZI":
        prikazi_plosco()
    else:
        vpisi_v_plosco(beseda1, smer, vr, st)
     


##########to do list:
'''naredi zalogo črk, VID URH
  točkovanje, LEA BRIŠKI
  več igralcev, 
  neskoncno kreogov + klomanda za konec URŠA
  shrani igro.'''

