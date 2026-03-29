# vispirms jāimportē nepieciešamās bibliotēkas
import statistics # šī bibliotēka nodrošina funkcijas vidējā, mediāna un citas statistikas aprēķināšanai
# ši bibliotēka nāk līdz ar Python, tāpēc nav nepieciešams to instalēt

atzimes =[7,8,5,9,8,10]
vidējais = statistics.mean(atzimes)
mediana = statistics.median(atzimes)
mode = statistics.mode(atzimes)# visbiežāk sastopamā vērtība
minimums = min(atzimes)
maksimums = max(atzimes)
# izdrukājam rezultātus
print("Atzīmes:", atzimes)
print("Vidējais:", vidējais)
print("Mediana:", mediana)
print("Mode:", mode)
print("Minimums:", minimums)
print("Maksimums:", maksimums)