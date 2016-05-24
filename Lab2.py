# coding: utf8
from spyre import server
import pandas


class VHIApp(server.App):
    title = "VHI App"

    inputs = [{"type": 'dropdown', "label": 'Time row', "value": 'VHI',
               "options": [{"label": "VHI", "value": "VHI"},
                           {"label": "VCI", "value": "VCI"},
                           {"label": "TCI", "value": "TCI"}], "key": 'number'},

              {"type": 'dropdown', "label": 'District', "value": 'Київська',
               "options": [{"label": "Vinnytsya", "value": "Вінницька"},
                           {"label": "Volyn", "value": "Волинська"},
                           {"label": "Dnipropetrovsk", "value": "Дніпропетровська"},
                           {"label": "Donetsk", "value": "Донецька"},
                           {"label": "Zhytomyr", "value": "Житомирська"},
                           {"label": "Zacarpathia", "value": "Закарпатська"},
                           {"label": "Zaporizhzhya", "value": "Запорізька"},
                           {"label": "Ivano-Frankivsk", "value": "Івано-Франківська"},
                           {"label": "Kiev", "value": "Київська"},
                           {"label": "Kirovograd", "value": "Кіровоградська"},
                           {"label": "Lviv", "value": "Львівська"},
                           {"label": "Mykolayiv", "value": "Миколаївська"},
                           {"label": "Odessa", "value": "Одеська"},
                           {"label": "Poltava", "value": "Полтавська"},
                           {"label": "Rivne", "value": "Рівненська"},
                           {"label": "Sumy", "value": "Сумська"},
                           {"label": "Ternopil", "value": "Тернопільська"},
                           {"label": "Kharkiv", "value": "Харківська"},
                           {"label": "Kherson", "value": "Херсонська"},
                           {"label": "Khmel'nyts'kyy", "value": "Хмельницька"},
                           {"label": "Cherkasy", "value": "Черкаська"},
                           {"label": "Chernivtsi", "value": "Чернівецька"},
                           {"label": "Chernihiv", "value": "Чернігівська"},
                           {"label": "Crimea", "value": "Республіка Крим"}], "key": 'region'},

              {"type": "text", "label": 'Year #1', "key": "year1", "value": '2007'},
              {"type": "text", "label": 'Interval of weeks from', "key": "w1", "value": '1'},
              {"type": "text", "label": 'to', "key": "w2", "value": '52'}]

    controls = [{"type": "button", "label": "Create a graph", "id": "submit_plot"}]
    tabs = ["Graph1", "Table1"]
    outputs = [{"type": "plot", "id": "plot", "control_id": "submit_plot", "tab": "Graph1"},
               {"type": "table", "id": "table", "control_id": "submit_plot", "tab": "Table1", "on_page_load": True}]

    def table(self, params):
        check_params(params)
        df = pandas.read_csv("/root/KPI2course/SRP/Lab2/data.csv", encoding='utf-8')
        df = df.drop('Unnamed: 0', 1)
        df = df[(df['region'] == params['region']) & (df['year'] == int(params['year1'])) &
                (df['week'] >= int(params['w1'])) & (df['week'] <= int(params['w2']))]
        return df


    def plot(self, params):
        df = self.table(params)
        plt = df.plot(x='week', y=params['number'])
        plt.set_title(params['year1'])
        return plt.get_figure()



def check_params(params):
    if int(params['year1']) < 1981: params['year1'] = 1981
    if int(params['year1']) > 2016: params['year1'] = 2016


    if int(params['w1']) < 1: params['w1'] = 1
    if int(params['w2']) > 52: params['w2'] = 52
    if int(params['w1']) > int(params['w2']):
        params['w1'] = 1
        params['w2'] = 52

app = VHIApp()
app.launch()
                          

