# TexnLog
Απαλλακτική εργασία στο μάθημα τεχνολογία λογισμικού

Προαπαιτούμενα:
<li>
  Docker
</li>

<br>

Για την εγκατάσταση της εφαρμογης πρέπει να γίνει clone του αποθετηρίου:
<br>
```git clone https://github.com/Thomasth01/TexnLog```
<br>
Μεταβιβαση στο directory της εφαρμογής
<br>
```cd TexnLog```
<br>
Δημιουργια conteiner
<br>
```docker build -t streamlit .```
<br>
Εκτέλεση conteiner
<br>
```docker run -p 8501:8501 streamlit```
<br>
Η εφαρμογή είναι προσβάσιμη από τον περιγητή στο ```localhost:8501``` δηλαδή η default πόρτα του streamlit
