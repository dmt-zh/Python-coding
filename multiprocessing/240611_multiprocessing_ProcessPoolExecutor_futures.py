# Напишите функцию crypto_handler, выполняющую расчетные задачи используя пул процессов с контролем времени выполнения и простым
# логированием исключений. В качестве расчетной задачи возьмем хорошо известную функцию шифрования. Функция crypto_handler принимает
# единственный аргумент - уставку контрольного времени выполнения. За установленное время все запланированные задачи должны быть успешно завершены.

# В тестирующей системе определена функция шифрования crypto_utils, которая принимает текстовый блок и возвращает кортеж
# из двух элементов: шифр (str) и оценка качества шифрования (float). Функция шифрования может "зависать", включая бесконечные 
# ожидания и может завершаться ошибкой из группы Exception.
# Также определен список text_blocks, в котором хранятся текстовые блоки для шифрования.

# Сформируйте словарь результатов results, где ключ - это шифр, значение - кортеж:
# (блок текста, число - оценка качества шифрования). Если за установленное контрольное время не все запланированные задачи завершились,
# считаем, что функция crypto_utils "зависла" и в таком случае формируем словарь ошибок errors, где ключ - это блок текста, на котором 
# подвисла задача, а значение - строка (str) с сообщениемtimeout_error

# Словарь ошибок также заполняется в случае возбуждения исключений при выполнении функции crypto_utils. В этом случае ключом будет блок текста,
# а вот значение должно содержать класс ошибки и сообщение ошибки.

# Например, если в процессе выполнения функции crypto_utils была возбуждена ошибка:
# raise ValueError("timeout")
# то в словаре errors должна быть пара ключ - значение: <блок теста>: ValueError('timeout')



import concurrent.futures

results = {}
errors = {}

def crypto_handler(timeout: float | int = 2) -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_works = {executor.submit(crypto_utils, txt): txt for txt in text_blocks}
        done, not_done = concurrent.futures.wait(future_works.keys(), timeout=timeout)
        for future in done:
            txt_value = future_works.get(future)
            if not future.exception():
                cypher, score = future.result()
                results[cypher] = (txt_value, score)
            else:
                errors[txt_value] = future.exception()

        for future in not_done:
            txt_value = future_works.get(future)
            errors[txt_value] = 'timeout_error'
