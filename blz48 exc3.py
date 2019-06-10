CENTEN_IN_EURO = 100
CENTEN_IN_50CT= 50
CENTEN_IN_20CT = 20
CENTEN_IN_DUBBELTJE = 10
CENTEN_IN_STUIVER = 5

bedrag = 1199
centen = bedrag

euro       = int( centen / CENTEN_IN_EURO )
centen -= euro  *  CENTEN_IN_EURO
50ct        = int(  centen / CENTEN_IN_50CT)
centen -=euro * CENTEN_IN_50CT
20ct        = int( centen / CENTEN_IN_20CT )
centen -= 20ct  *  CENTEN_IN_20CT
dubbeltjes = int( centen / CENTEN_IN_DUBBELTJE )
centen -= dubbeltjes  *  CENTEN_IN_DUBBELTJE
stuivers = int( centen / CENTEN_IN_STUIVER )
centen -= stuivers  *  CENTEN_IN_STUIVER
centen = int( centen )

print( bedrag / CENTEN_IN_EURO, "bestaat uit:" )
print( "Euro:", euro)
print( "50ct:", 50ct)
print( "20ct:", 20ct )
print( "Dubbeltjes:", dubbeltjes )
print( "Stuivers:", stuivers )
print( "Centen:", centen )
