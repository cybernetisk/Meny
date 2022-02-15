import json  
#use this instead: miller
data = json.load(open("./data.json"))
csv = open("data.csv", 'w')
csv.write("Navn;Egendefinert enhet (maks 4 tegn);MVA.;Variant1 navn;Variant1 variant;Variant2 navn;Variant2 variant;Variant3 navn;Variant3 variant;SKU;Pris;Innkjøpspris;Strekkode;På lager;Variant-ID;Produkt-ID;ID (Ikke rediger): [n-un-vat-vo0n-vo0v-vo1n-vo1v-vo2n-vo2v-sku-p-cp-bc-ib-vid-id-k]\n")
for d in data:
    t= d['name']=='Alkoholfritt'
    for p in d['products']:
        f = p['type'] != "flaske"
        print(p)
        csv.write(p['name']+";;25;Prisklasse; Ekstern;;;;;;"+str(p['price'] if f else p['price1'])+";0;;;;;\n" )
        csv.write(";;;Prisklasse; Intern;;;;;;"+str(int(p['priceIntern']) if f else int(p['price1Intern'])-5)+";0;;;;;\n" )
        # csv.write(p['name'])


