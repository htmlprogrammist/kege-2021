# 19 - 21 задания
##ВАЖНО! 
* Для поиска ответа в 19 задаче, можно заменить `all` на `any` в условии, возвращающим `V1`
(только на время выполнения **задания 19**).  
Таким образом минимальное значение камней в куче, которое  равно `V1` - ответ на задание.

* Чет не всегда этот алгоритм срабатывает. Либо это моя ошибка просто. [Пример](https://github.com/htmlprogrammist/unified-state-exam/blob/master/Bariants/statgrad-ov-03-21/task_19-21.py)

Библиотека, без которой ничего работать не будет:
```
from functools import *
```
или
```
from functools import lru_cache
```
Потом перед основной функцией ставим следующий декоратор:
```
@lru_cache(None)
```

Следующий алгоритм, по сути, нужно **выучить**:
```
if any(game(m) == 'W' for m in moves(h)):
    return 'P1'
if all(game(m) == 'P1' for m in moves(h)):
# if any(game(m) == 'P1' for m in moves(h)):  # для 19 задания
    return 'V1'
if any(game(m) == 'V1' for m in moves(h)):
    return 'P2'
if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
    return 'V2'
```

Код целиком:
```
from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a * 4, b), (a, b + 1), (a, b * 4)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 133:
        return "W"

    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in moves(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)):
        return 'V2'


for s in range(1, 125 + 1):
    h = 7, s
    print(s, game(h))
```
