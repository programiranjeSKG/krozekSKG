
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


#________branje posamezne vrstice:
def preberi_vnos():
     vnos = input().split(', ')
     vnos[2]=int(vnos[2])
     vnos[3]= int(vnos[3])
     return vnos

def vpisi_v_plosco():
     #začetek funkcije (poberem novo besedo)
     vnos = preberi_vnos()
     beseda=vnos[0].upper()
     smer=vnos[1].upper()
     vr = vnos[2]
     st = vnos[3]



     if smer == 'R':
          vrDodaj=0
          stDodaj=1
          '''
     if smer == 'L':
          vrDodaj=0
          stDodaj=-1
          '''
     if smer == 'D':
          vrDodaj=1
          stDodaj=0
          '''
     if smer == 'U':
          vrDodaj=-1
          stDodaj=0
          '''
     #preveri ustreznost:
     enak = False
     
     for znj in range(len(beseda)):
          
          if vr <= -1 or st <= -1 or vr >= 15 or st >= 15:
                print("Napaka!")
                raise IndexError('padel si s plošče')

          if plosca[vr][st]=='%' or plosca[vr][st] == beseda[znj]:
               if plosca[vr][st] == beseda[znj]:
                    enak = True
          else:
               raise ValueError('Polje je zasedeno z drugo črko')

     if enak == True:
          #zapiši v tabelo
          for znj in range(len(beseda)):
               plosca[vr][st] = beseda[znj]
               vr += vrDodaj
               st += stDodaj
     else:
          raise ValueError('Tvoja beseda se ne dotika drugih besed')
     #konec funkcije (dodam besedo v ploščo)

for i in range(5):
     vpisi_v_plosco()
     print(plosca)


##########to do list:
     '''naredi zalogo črk,
          točkovanje,
          več igralcev,
          shrani igro.'''

