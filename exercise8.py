def vokon_zählen(x):
     x_lower = x.lower()
     x_lower_list = list(x_lower)
     vokale = "aeiou"
     
     v = [] # Hier speichern wir alle Vokale
     k = [] # Hier speichern wir alle Buchstaben
     
     for b in x_lower_list:
         # Hier prüfen wir, ob b ein Buchstabe ist
         if b.isalpha():
             k.append(b)
         # Hier prüfen wir, ob B ein Vokal ist
         if b in vokale:
             v.append(b)
             
     return f"Im String '{x}' gibt es {len(v)} Vokale und {len(k)-len(v)} Konsonanten."

print(vokon_zählen("Berlin I love you!"))
