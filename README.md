# NP_D7
NB Если вы не против, я закинула стадию D6 в отдельную директорию, так как хочу сохранить пошаговое выполнение задания (я потом не вспомню, как это все делается) + я там закомментировала пару строчек, не обращайте внимание.
А еще я неправильно назвала директорию. Она должна называться D6, а не D7.


У меня есть пара вопросов. 

1. В задании нужно было вывести общее количество новостей, но я не знала, куда это вставить, поэтому вставила сюда, хотя по идее эта функция должна отвечать только за дату. Скажите, как должно было быть?

<img width="775" alt="image" src="https://user-images.githubusercontent.com/115484055/216842194-9d8fd277-3450-4419-afcf-d03146227a7a.png">

2. Я сначала думала сделать цензурирование через __contains__, но не придумала, как можно будет потом "вытащить" нужное слово. Если знаете, можете подсказать? Если нет, то просто проигнорируйте этот вопрос.

3. Не уверена, что фильтр с цензурой работает именно так, как предполагалось. Например, я решила просто так зацензурировать слово "кот" и теперь слова, которые содержат эти буквы, тоже цензурируются. Так и должно быть? Я не стала писать обсценную лексику, чтобы вам не было некомфортно. Но что, например, делать с такими словами как употреблять и скипидар? Они же пострадают. Или это на данном этапе не важно?
Пример из новости
<img width="484" alt="image" src="https://user-images.githubusercontent.com/115484055/216842342-fe209194-287b-46d4-898f-e3b077b07e53.png">

4. В модели Post название у меня обозначено как title. Может ли возникнуть конфликт из-за того, что оно совпадает с методом title?

<img width="484" alt="image" src="https://user-images.githubusercontent.com/115484055/216842452-2a9d3e9b-4208-461b-b63e-b2045f5cd7df.png">

