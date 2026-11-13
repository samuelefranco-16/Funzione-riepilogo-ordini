dati_errati = [
  {"id": 1, "impo": 120, "stato": "pagato"},  #chiave con nome errato
  {"importo": 50, "stato": "annullato"},  #campo id mancante
  {"id": 3, "importo": 80, "stato": "pag"},  #valore del campo "stato" anomalo 
  {"id": 4, "importo": -20, "stato": "pagato"},   #valore negativo dell'importo
  {"id": 5, "importo": 0, "stato": "pagato"},  #valore 0 dell'importo
  {"importo": 40, "id": 6, "stato": "pagato"}   #ordine delle chiavi scambiato
]

dati_normali = [
  {"id": 1, "importo": 120, "stato": "pagato"},
  {"id": 2, "importo": 50, "stato": "pagato"},
  {"id": 3, "importo": 80, "stato": "pagato"},
  {"id": 4, "importo": 200, "stato": "pagato"},
  {"id": 5, "importo": 40, "stato": "in_attesa"}

]

def sommaImporti(dizio):
  listaPagati = []
  contaOrdiniPagati = 0
  campiObbligatori = ["id","importo","stato"]

  for i in dizio:
    if set(campiObbligatori) <= i.keys():
      for k,v in i.items():  
        if k=="stato" and v=="pagato":
          if str(i["importo"]).isdigit():
            if i["importo"] > 0 :
              listaPagati.append(i["importo"])
              contaOrdiniPagati += 1

  return f"Il totale pagato ammonta a: {sum(listaPagati)} \nIl totale degli ordini pagati è: {contaOrdiniPagati}"
        

print(sommaImporti(dati_errati))

print(sommaImporti(dati_normali))