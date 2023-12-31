class models_and_their_params:
    def __init__(self,model):
        self.model = model

    def get_empty_model(self)->dict:
        resuolt={}
        match self.model:
            case "первая":
                resuolt={
                    "количество авто в год":0,
                    "1 из скольки машин опасная":0,
                    "Частота аварий на км *1е6":0,
                    "Длина пути вдоль людей км":0,
                    "Вероятность условного выброса":0,
                    "Утечка может продолжаться мин":0,
                    "Молярная масса вещества г/моль":0,
                    "V_m ":22.4,
                    "концентрация в зоне выброса мг/м3":0,
                    "Площадь поражения, га":0,
                    "Плотность населения чел/км2":0,
                    "Пробит время мин":0,
                    "Пробит a":0,
                    "Пробит b":0,
                    "Пробит n":0,
                }
            case "вторая":
                resuolt={
                    "частота аварий/год":0,
                    "концентрация канц мкг/м3": 0,
                    "SF (мг/кг*сут)-1": 0,
                    "воздействие дней/год EF": 0,
                    "повторяемость ветра С %": 0,
                    "повторяемость ветра СВ %": 0,
                    "повторяемость ветра В %": 0,
                    "повторяемость ветра ЮВ %": 0,
                    "повторяемость ветра Ю %": 0,
                    "повторяемость ветра ЮЗ %": 0,
                    "повторяемость ветра З %": 0,
                    "повторяемость ветра СЗ %": 0,
                    "сектор негативн. воздей.": 0,
                    "направление - Север-1, СВ-2, В-3,...": 0,
                    "плотность населения днём":0,
                    "плотность населения ночь":0,
                    "общая полщадь поражения": 0,
                    "количество воздуза в час": 0,
                    "коэффициент биосохранения": 1,
                    "коэффициент абсорбции": 1,
                    "ED": 0,
                    "weight (BW)": 0,
                    "AT in years": 0,
                }
            case "третья":
                resuolt={
                    "Concentration": 0,
                    "Quantity in a day (CR)":0,
                    "SF": 0,
                    "EF": 0,
                    "ED":0,
                    "weight (BW)": 0,
                    "AT in years":0,
                    "population": 0
                }
            case "четвёртая":
                resuolt={
                    "Lambda пораж.фактора":0,
                    "Зона пораж. при аварии %":0,
                    "Время нахождения часов/неделю":0,
                    "Количество человек в смене":0
                }
            case "пятая":
                resuolt = {
                    "Lambda пораж.фактора": 0,
                    "Зона пораж. при аварии %": 0,
                    "Площадь поражения, га":0,
                    "Время нахождения недель/год": 0,
                    "Плотность людей, чел/га": 0
                }
        return resuolt
    def get_key_name_list(self)->list:
        key_dict = self.get_empty_model()
        keys=list(key_dict.keys())
        return keys