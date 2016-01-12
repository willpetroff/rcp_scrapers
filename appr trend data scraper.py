from urllib.request import urlopen
import json
from codecs import decode
import csv


def scraping_rcp_json(url, target, length):
    data_master = []
    text_file = open('test.txt', 'w')
    target_url = urlopen(url).read()
    data = target_url.decode(encoding='UTF-8')
    text_file.write(data[length:-4])
    text_file.close()
    data_file = open('test.txt', 'r')
    target_text = json.load(data_file)
    counter = 0
    while counter < len(target_text):
        ind_poll_data = {}
        ind_poll_data['date'] = target_text[counter]['date']
        ind_poll_data['appr'] = target_text[counter]['candidate'][0]['value']
        ind_poll_data['disapp'] = target_text[counter]['candidate'][1]['value']
        data_master.append(ind_poll_data)
        counter += 1
    data_file.close()
    with open(target+'_appr_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in data_master:
            temp_list = [item['date'], ['appr'], ['disapp']]
            writer.writerow(temp_list)
    print('Done with '+target)


def main():
    pres_url = 'http://www.realclearpolitics.com/epolls/json/1044_historical.js?1413737132781&callback=return_json'
    pres_len = 194
    cong_url = 'http://www.realclearpolitics.com/epolls/json/903_historical.js?1413818247461&callback=return_json'
    cong_len = 188
    other_url = {}
    scraping_rcp_json(pres_url, 'pres', pres_len)
    scraping_rcp_json(cong_url, 'cong', cong_len)
    if len(other_url) >= 1:
        for item in other_url:
            scraping_rcp_json(item['url'], item['target'], item['len'])

if __name__ == '__main__':
    main()