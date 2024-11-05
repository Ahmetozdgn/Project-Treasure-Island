# https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Hazine Adası'na hoş geldiniz.")
print("Göreviniz hazineyi bulmak.")
seçim1 = input('Bir yol ayrımındasınız. '
               'Nereye gitmek istiyorsun? "sol" veya "sağ" yazın.\n').lower() #lower() kullanıcı girdiğinde büyük-küçük harf duyarlılığını kaldırır 

if seçim1 == "sol":
    seçim2 = input('Bir göle geldiniz. '
                  'Gölün ortasında bir ada var. '
                  'Bir tekneyi beklemek için "bekle" yazın. '
                  'Karşıya geçmek için "yüzmek" yazın.\n').lower()
    if seçim2 == "bekle":
        seçim3 = input("Adaya zarar görmeden varıyorsunuz."
                      " 3 kapılı bir ev var. "
                      "Biri kırmızı, biri sarı ve biri mavi."
                      " Hangi rengi seçersiniz?\n").lower()
        if seçim3 == "kırmızı":
            print("Ateşle dolu bir oda. Oyun Bitti.")
        elif seçim3 == "sarı":
            print("Hazineyi buldun! Sen kazandın!")
        elif seçim3 == "mavi":
            print("Canavarlarla dolu bir odaya giriyorsunuz. Oyun Bitti.")
        else:
            print("var olamayan bir kapıyı seçtiniz. Oyun bitti")
    else:
        print("Kızgın bir alabalık tarafından saldırıya uğradınız. Oyun bitti.")
else:
    print("Bir çukura düştün. Oyun Bitti.")

