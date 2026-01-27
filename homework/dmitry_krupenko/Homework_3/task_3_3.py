import numpy as np
# решил использовать нампи как более простой в наглядности способ получения среднего геометрического значения
origin_integers = [12, 16, 20]
print(sum(origin_integers) / len(origin_integers))

result = np.prod(origin_integers)**(1 / len(origin_integers))
print(result)
