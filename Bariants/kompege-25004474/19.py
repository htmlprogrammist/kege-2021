"""
Задание 19 (№1810). Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежит лист бумаги, на котором написано двоичное число. Игроки ходят по очереди, первый ход делает Петя.
За один ход игрок может приписать справа или слева к имеющемуся на листе числу двоичную запись любого из чисел 2^n +1,
где n - произвольное натуральное число, либо приписать справа или слева от имеющегося числа его копию.
Например, имея двоичное число 11001, за один ход можно получить путем копирования число 1100111001
или путем приписывания двоичной записи числа 3 числа 1100111 или 1111001.

Игра завершается в тот момент, когда количество единиц в двоичной записи числа становится не менее 60.
Победителем считается игрок, сделавший последний ход, то есть первым получивший двоичное число,
в котором будет 60 или больше единиц. В начальный момент единиц в числе было S , 1 ≤ S ≤ 58.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Описать стратегию игрока – значит описать, какой ход он должен сделать в любой ситуации,
которая ему может встретиться при различной игре противника.
В описание выигрышной стратегии не следует включать ходы играющего по этой стратегии игрока,
не являющиеся для него безусловно выигрышными, т.е. не являющиеся выигрышными независимо от игры противника.

Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Укажите минимальное значение S, когда такая ситуация возможна.

Задание 20 .
Для игры, описанной в предыдущем задании, найдите два таких значения(минимальное и максимальное) S,
при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.

Задание 21 .
Для игры, описанной в задании 19, найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
"""
