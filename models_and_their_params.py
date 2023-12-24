class models_and_their_params:
    def __init__(self,model):
        self.model =model

    def get_empty_model(self)->dict:
        resuolt={}
        match self.model:
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