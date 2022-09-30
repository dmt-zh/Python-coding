from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from itertools import zip_longest
from string import Template
from pathlib import Path
import webbrowser
import argparse
import difflib
import sys
import io


class TXTFilesMatching:

    @staticmethod
    def __make_table_row(line1='none', line2='none', blue='', n_row='', header=False):
        cell = 'h' if header else 'd'
        original = 'Original text' if line1 == 'none' else line1
        changed = 'Changed text' if line2 == 'none' else line2
        coef = 'BLUE coef' if blue == '' else blue
        bgr1_color = '#EFC7B7' if blue != '' and blue < 100 else ''
        bgr2_color = '#B7EFB7' if blue != '' and blue < 100 else ''

        table_row = (
            "\t<tr>\n",
            f"\t\t<t{cell}><font color='grey'>{n_row}</t{cell}>\n",
            f"\t\t<t{cell} bgcolor={bgr1_color}><font face='Calibri'>{original}</t{cell}>\n",
            f"\t\t<t{cell}><font color='grey'>{n_row}</t{cell}>\n",
            f"\t\t<t{cell} bgcolor={bgr2_color}><font face='Calibri'>{changed}</t{cell}>\n",
            f"\t\t<t{cell}><font face='Arial'>{coef}</t{cell}>\n",
            f"\t</tr>\n"
        )

        return ''.join(table_row)

    @staticmethod
    def __paste_string(all_words, diff_words, color):
        sentence = ''
        punctuation, stop_marks = ',:;"\'«»', '.!?'
        t = Template("<span style='background-color:$color'>$cur_str</span>")

        if len(all_words) >= 2:
            for idx in range(len(all_words) - 1):
                cur_str = all_words[idx]
                next_str = all_words[idx + 1]

                if cur_str in diff_words:
                    if next_str in punctuation or next_str in stop_marks:
                        sentence += t.substitute(color=color, cur_str=cur_str)
                    else:
                        sentence += t.substitute(color=color, cur_str=cur_str + ' ')
                else:
                    if next_str in punctuation or next_str in stop_marks:
                        sentence += cur_str
                    else:
                        sentence += cur_str + ' '

            last = all_words[-1]
            if last in diff_words:
                sentence += t.substitute(color=color, cur_str=last)
            else:
                sentence += last

        elif len(all_words) == 1:
            word = all_words[0]
            if word in diff_words:
                sentence += t.substitute(color=color, cur_str=word)
            else:
                sentence += word
        else:
            return sentence
        return sentence

    def __span_wrapper(self, words_lst1, words_lst2):
        delta = tuple(difflib.Differ().compare(words_lst1, words_lst2))
        diff_words1 = tuple(i[1:].strip().strip() for i in delta if i.startswith('-'))
        diff_words2 = tuple(i[1:].strip().strip() for i in delta if i.startswith('+'))

        s1 = self.__paste_string(words_lst1, diff_words1, '#B03608')
        s2 = self.__paste_string(words_lst2, diff_words2, '#2FB008')

        return s1, s2

    def compare_two_files(self, file_or_path1: Path, file_or_path2: Path):
        with io.open(file_or_path1, 'r', encoding='utf-8') as f1, io.open(file_or_path2, 'r', encoding='utf-8') as f2:
            text1, text2 = f1.readlines(), f2.readlines()

            html_table = "<table border='1' cellspacing='0' cellpadding='4' width='1100' align='center'>\n"
            html_table += self.__make_table_row(header=True)
            n_rows = 1

            for line1, line2 in zip_longest(text1, text2, fillvalue=' '):
                row1, row2 = line1.strip(), line2.strip()
                smooth = SmoothingFunction().method2

                ref, test = row1.split(), row2.split()
                coef = sentence_bleu([ref], test, smoothing_function=smooth, auto_reweigh=True)
                blue = round(coef * 100, 2)

                if blue < 100:
                    mod_row1, mod_row2 = self.__span_wrapper(ref, test)
                    html_table += self.__make_table_row(mod_row1, mod_row2, blue, n_rows)
                else:
                    html_table += self.__make_table_row(row1, row2, blue, n_rows)

                n_rows += 1
            html_table += "</table>"

        with open("html-table.html", "w", encoding="utf-8") as fout:
            fout.write(html_table)

        self.__view_html_table()

    def __view_html_table(self):
        webbrowser.open_new_tab('html-table.html')


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('original_text_file')
        parser.add_argument('changed_text_file')
        args = parser.parse_args()

        first_txt_file = Path(args.original_text_file)
        second_txt_file = Path(args.changed_text_file)

        text_maching = TXTFilesMatching()

        try:
            text_maching.compare_two_files(first_txt_file, second_txt_file)
        except FileNotFoundError:
            sys.stdout.write('Неверно указаны имена файлов или путь.')
        except:
            sys.stdout.write('Что-то пошло не так, скрипт аварийно завершился. Проверьте расширение файлов!.')
    except:
        print('Скипт запускается через терминал! Для запуска скрипта закомментируйте функцию "main".')



if __name__ == '__main__':
    main()