#Множества работают быстрее
#Одинаковых элементов быть не может
#Не изменяемый тип
##m = {1,2,3,4,5,6,1}
##s = {"a","b","c","d"}
##m.add(10)
##m.discard(2)
###z = m.union(s)
##m.update(s)
##print(m)

new_set = set()

r = open('d:\Обработки\ЗаказПокупателя.txt')
#new_set.update(set(r.read().split()))#Конвертируем в множество
r1 = set(r.read().split())
r.close()

r2 = open('d:\Обработки\Текстовый документ (3).txt')
#new_set.update(set(r2.read().split()))#Конвертируем в множество
r3 = set(r2.read().split())
r2.close()

new_words = r1.intersection(r3)#Слова из обоих текстов
print(new_words)
