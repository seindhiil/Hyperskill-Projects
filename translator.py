import requests
import sys
from bs4 import BeautifulSoup


x = False


def lang_choice(choice):
    lang = ''
    if choice == 1:
        lang = 'arabic'
    elif choice == 2:
        lang = 'german'
    elif choice == 3:
        lang = 'english'
    elif choice == 4:
        lang = 'spanish'
    elif choice == 5:
        lang = 'french'
    elif choice == 6:
        lang = 'hebrew'
    elif choice == 7:
        lang = 'japanese'
    elif choice == 8:
        lang = 'dutch'
    elif choice == 9:
        lang = 'polish'
    elif choice == 10:
        lang = 'portuguese'
    elif choice == 11:
        lang = 'romanian'
    elif choice == 12:
        lang = 'russian'
    elif choice == 13:
        lang = 'turkish'
    else:
        pass
        # print('no')
        # word_txt_edit.write('no\n')
    return lang


try:
    def trans_all(lang_1_, word_):
        # var_1_ = ''
        for i_ in range(13):
            # var_1_ = lang_choice(i_ + 1)
            if lang_1 != lang_choice(i_ + 1):
                trans_url = 'https://context.reverso.net/translation/' + lang_1_ + '-' + lang_choice(i_ + 1) + '/' + str(word_)
                # print(trans_url)
                # word_txt_edit.write(trans_url + '\n')
                transl_ = requests.get(trans_url, headers={'User-Agent': 'Mozilla/5.0'})
                soup_ = BeautifulSoup(transl_.content, 'html.parser')
                stuff_ = soup_.select('div#translations-content.wide-container')
                var_2 = str(stuff_[0].text)
                print(lang_choice(i_ + 1).capitalize() + ' Translations:')
                word_txt_edit.write(lang_choice(i_ + 1).capitalize() + ' Translations:\n')
                var_3_ = []
                for i1 in var_2:
                    if i1 != ' ' and i1 != '\n':
                        var_3_.append(i1)
                    elif i1 == ' ':
                        var_3_.append(' ')
                hello_ = "".join(var_3_)
                hello_ = hello_.replace('     ', '\n')
                for i_________ in range(1):
                    print(hello_.split()[i_________]+'\n')
                    word_txt_edit.write(hello_.split()[i_________]+'\n')

                # examples
                word_txt_edit.write('\n')
                print(lang_choice(i_ + 1).capitalize() + ' Examples:')
                word_txt_edit.write(lang_choice(i_ + 1).capitalize() + ' Examples:\n')
                translation_ = []
                limit = 0
                for o in soup_.select('span.text'):
                    if limit == 0:
                        if 'lang="fr"' not in str(o) and '<em>' in str(o):
                            translation_.append(o)
                        if 'lang="fr"' in str(o) and len(translation_) != 0:
                            translation_.append(o)
                        if len(translation_) == 2:
                            for translated_ in translation_:
                                x_1 = str(translated_.text.strip('\n').replace('          ', ''))
                                print(x_1)
                                word_txt_edit.write(x_1 + '\n')
                            translation_ = []
                            if lang_choice(i_+1) != 'turkish':
                                word_txt_edit.write('\n\n')
                                print('\n')
                            limit = 1


    # beans = input()
    # print(beans)

    # stuff = input().split()
    # print(stuff)

    if len(sys.argv) >= 1:
        lang_1 = str(sys.argv[1])
        lang_2 = str(sys.argv[2])
        word = str(sys.argv[3])
        word_txt_edit = open(word + '.txt', 'w', encoding='UTF-8')
        for i in range(13):
            if lang_choice(i+1) == lang_2:
                x = True
        if lang_2 == 'all':
            x = True
        if lang_2 != 'all':
            transl_link = 'https://context.reverso.net/translation/' + lang_1 + '-' + lang_2 + '/' + word

            # transl = requests.get('https://context.reverso.net/')
            transl = requests.get(transl_link, headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(transl.content, 'html.parser')

            # definitions
            print(lang_2.capitalize() + ' Translations:')
            word_txt_edit.write(lang_2.capitalize() + ' Translations:\n')

            var = str(soup.select('div#translations-content.wide-container')[0].text)
            # var__ = var.strip(' ')
            var___ = []
            for i in var:
                if i != ' ' and i != '\n':
                    var___.append(i)
                elif i == ' ':
                    var___.append(' ')
            hello = "".join(var___)
            hello = hello.replace('     ', '\n')
            hello = hello.split()
            for i in range(5):
                print(hello[i])
                word_txt_edit.write(hello[i] + '\n')

            # examples
            print('\n')
            word_txt_edit.write('\n\n')
            print(lang_2.capitalize() + ' Examples:')
            word_txt_edit.write(lang_2.capitalize() + ' Examples:\n')
            translation = []
            for i in soup.select('span.text'):
                if 'lang="fr"' not in str(i) and '<em>' in str(i):
                    translation.append(i)
                if 'lang="fr"' in str(i) and len(translation) != 0:
                    translation.append(i)
                if len(translation) == 2:
                    for translated in translation:
                        print(translated.text.strip('\n').replace('          ', ''))
                        word_txt_edit.write(translated.text.strip('\n').replace('          ', '') + '\n')
                    translation = []
                    print('\n')
                    word_txt_edit.write('\n\n')
        elif lang_2 == 'all':
            trans_all(lang_1, word)

        word_txt_edit.close()
except IndexError:
    if x:
        print('Sorry, unable to find ' + word)
    elif not x:
        print('Sorry, the program doesn\'t support ' + lang_2)
    # print(lang_1)
    # print(lang_2)
