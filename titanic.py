import pandas as pd
from ydata_profiling import ProfileReport
from IPython.display import display

base = pd.read_csv("Titanic-Dataset.csv")
base.columns = ["IDpassageiro", "Sobrevivente","ClassePassagem","Nome","Genero","idade","NrParentes","NrPaisFilhos","NrTicket","Tarifa","Cabine","PortoEmbarque"]
display (base) 
