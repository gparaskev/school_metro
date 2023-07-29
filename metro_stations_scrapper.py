import pandas as pd
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('html_lines/metro_line_3.html', encoding='UTF-8'), 'html.parser')
tb = soup.find('tbody')
# print(tb)
table_rows = []
for row in tb.findAll('tr'):
    print('-------------------')
    row_dict = {}
    for idx, col in enumerate(row.findAll('td')):
        # print(idx, col.text)
        if idx == 6:
            coords = col.text.replace('\n', "")
            coords_list = coords.split("/")
            lat_lon = coords_list[-1]
            lat_lon_list = lat_lon.split(" ")
            row_dict['lat'] = lat_lon_list[1].replace(";", "")
            row_dict['lon'] = lat_lon_list[2].replace("\ufeff", "")
        else:
            row_dict[idx] = col.text.replace('\n', "")
    table_rows.append(row_dict)
print(table_rows)
data = pd.DataFrame.from_records(table_rows)
print(data)
data.to_csv("output/metro_line_3.csv", index=False)
# temp = data.iloc[0,-1]
# print(temp.split("/"))

