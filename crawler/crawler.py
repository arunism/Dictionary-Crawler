import json
import copy
import string
import requests
from bs4 import BeautifulSoup
from utils.utils import read_all_links

fields = list()
rows = list()


for alphabet in string.ascii_lowercase[1]:
    word_links = read_all_links(alphabet)
    total_list = list()

    for url in [word_links[i] for i in range(len(word_links))]:
        # url = word_links[41]
        response = requests.get(url[1])

        if response.status_code == 200:
            bs_obj = BeautifulSoup(response.text, 'html.parser')
            if bs_obj.find('span', {'class': 'pron-spell-content'}):
                pronunciation = bs_obj.find('span', {'class': 'pron-spell-content'}).get_text()
            all_meanings = bs_obj.find('div', {'class': 'e16867sm0'}).findAll('section', {'class': 'css-pnw38j'})
            
            current_word_list = list()
            all_meanings_dict = dict()
            classificationName = dict()

            for meaning in all_meanings:
                grammar = ''
                lines= ''

                if meaning.find('span', {'class': 'luna-pos'}) or meaning.find('span', {'class': 'pos'}):
                    if meaning.find('span', {'class': 'luna-pos'}):
                        grammar = meaning.find('span', {'class': 'luna-pos'}).get_text()
                    elif meaning.find('span', {'class': 'pos'}):
                        grammar = meaning.find('span', {'class': 'pos'}).get_text()
                    lines = meaning.findAll('div', {'class': 'e1q3nk1v2'})
                    
                    each_grammar_meaning = list()
                    each_grammar_example = list()
                    current_word = dict()

                    for line in lines:
                        example = ''
                        
                        text = line.findAll('span')[-1].get_text()
                        if line.find('span', {'class': 'luna-example'}):
                            example = line.find('span', {'class': 'luna-example'}).get_text()
                        each_grammar_meaning.append(text)
                        each_grammar_example.append(example)

                    all_meanings_dict['definition'] = each_grammar_meaning
                    all_meanings_dict['usage'] = each_grammar_example
                    classificationName['classificationName'] = grammar
                    all_meanings_dict['entryClassification'] = classificationName

                    current_word['term'] = url[0]
                    current_word['entryDefinitionsList'] = all_meanings_dict
                    # If the below line is not added:
                    # 1. We are not creating a new dictionary object each time
                    # 2. We'll be simply mutating the same object within each iteration
                    # So we'll be deep copying the dictionary using the copy module
                    # Then after obtaining this copy, we'll mutate it and append to list
                    current_word = copy.deepcopy(current_word)
                    current_word_list.append(current_word)

        total_list.append(current_word_list)


        with open(f'./my_files/json_files/{alphabet}.json', 'w', encoding='utf-8') as file:
            json.dump(total_list, file, ensure_ascii=False, indent=4)
