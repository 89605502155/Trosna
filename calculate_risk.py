# from models_and_their_params import  models_and_their_params
class calculate_risk:
    def __init__(self):
        pass

    def calculate_second_risk(self,params:dict):
        keys=list(params.keys())
        # ['частота аварий/год', 'концентрация канц мкг/м3', 'SF (мг/кг*сут)-1', 'воздействие дней/год EF',
        #  'повторяемость ветра С %', 'повторяемость ветра СВ %', 'повторяемость ветра В %', 'повторяемость ветра ЮВ %',
        #  'повторяемость ветра Ю %', 'повторяемость ветра ЮЗ %', 'повторяемость ветра З %', 'повторяемость ветра СЗ %',
        #  'сектор негативн. воздей.', 'направление - Север-1, СВ-2, В-3,...', 'плотность населения днём',
        #  'плотность населения ночь', 'общая полщадь поражения', 'количество воздуза в час',
        #  'коэффициент биосохранения', 'коэффициент абсорбции', 'ED', 'weight (BW)', 'AT in years']

        # print(params[keys[13]])
        napr=(int(params[keys[13]]-1+4))%8
        geo_napr=params[keys[4+napr]]
        # print(keys[4+napr],geo_napr)
        I=((params[keys[1]]*0.001*geo_napr*0.01)*params[keys[17]]*24*params[keys[3]]*
           params[keys[20]]*params[keys[19]]*params[keys[18]])/(params[keys[21]]*params[keys[22]]*365)
        R_I=I*params[keys[2]]*(params[keys[12]]/45)*params[keys[0]]
        # print("I",I)
        # print("R_I", R_I)
        N_day=params[keys[14]]*params[keys[16]]
        N_night=params[keys[15]]*params[keys[16]]
        R_pop=R_I*(N_day*(2/3)+N_night*(1/3))
        return {
            "R_ind": R_I,
            "R_pop": R_pop
        }
    def calculate_third_risk(self,params:dict):
        keys=list(params.keys())
        #['Concentration', 'Quantity in a day (CR)', 'SF', 'EF', 'ED', 'weight (BW)', 'AT in years', 'population']
        try:
            I=params[keys[0]]*params[keys[1]]*params[keys[3]]*params[keys[4]]/(params[keys[5]]*params[keys[6]]*365)
            R_I=I*params[keys[2]]
            R_pop=R_I*params[keys[7]]
            MeanMinusLife=params[keys[4]]*(params[keys[6]]-params[keys[4]])*R_I
        except ZeroDivisionError:
            R_I =0
            R_pop =0
            MeanMinusLife =0
        # print("I",I)
        return {
            "R_ind":R_I,
            "R_pop":R_pop,
            "ССОПЖ":MeanMinusLife
        }

    def calculate_fourth_risk(self, params: dict):
        keys=list(params.keys())
        #['Lambda пораж.фактора', 'Зона пораж. при аварии %', 'Время нахождения часов/неделю', 'Количество человек в смене']
        try:
            R_I=params[keys[0]]*params[keys[1]]*0.01*(params[keys[2]]/(24*7))
            R_pop=R_I*params[keys[3]]
        except ZeroDivisionError:
            R_I =0
            R_pop =0
        return {
            "R_ind": R_I,
            "R_pop": R_pop
        }
    def calculate_fifth_risk(self, params: dict):
        keys=list(params.keys())
        #print(keys)
        #['Lambda пораж.фактора', 'Зона пораж. при аварии %', 'Площадь поражения, га', 'Время нахождения недель/год', 'Плотность людей, чел/га']
        try:
            R_I=params[keys[0]]*params[keys[1]]*0.01*((params[keys[3]]*7)/365)
            R_pop=R_I*params[keys[2]]*params[keys[4]]
        except ZeroDivisionError:
            R_I =0
            R_pop =0
        return {
            "R_ind": R_I,
            "R_pop": R_pop
        }
    def main(self,variant:str,params:dict):
        response={}
        print("variant",variant)
        print("params",params)
        # name_model=models_and_their_params(model=variant)
        # names=name_model.get_key_name_list()
        match variant:
            case "вторая": response=self.calculate_second_risk(params)
            case "третья": response=self.calculate_third_risk(params)
            case "четвёртая": response=self.calculate_fourth_risk(params)
            case "пятая": response=self.calculate_fifth_risk(params)
        return response