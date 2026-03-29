# pārbaudīsim pandas versiju
import pandas as pd # importējam pandas bibliotēku ar saīsinājumu pd
print("Pandas versija:", pd.__version__)

# jā pandas nav tad uzstādam ar sekojošo komandu:
# pip install pandas
# mums vajag arī lasīt un rakstīt Excel failus, tāpēc uzstādam arī openpyxl bibliotēku:
# pip install openpyxl
# rakstīšanā Excel failā:
# xlslwriter arī
# pip install xlsxwriter
# kopā vienā rindā:
# pip install pandas openpyxl xlsxwriter

# nolasīsism terini.csv failu un izvadīsim to uz ekrāna
# svarīgi lai terini.csv būtu tajā pašā mapē kur atrodas šis Python fails, pretējā gadījumā būs jānorāda pilns ceļš līdz failam
df = pd.read_csv("terini.csv") # nolasām csv failu
# df ir ļoti populārs saīsinājums datu rāmim (dataframe)
print(df) # izvadām datu rāmi uz ekrāna