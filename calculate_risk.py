# from models_and_their_params import  models_and_their_params
class calculate_risk:
    def __init__(self):
        pass

    def calculate_third_risk(self,params:dict):
        keys=list(params.keys())
        #['Concentration', 'Quantity in a day (CR)', 'SF', 'EF', 'ED', 'weight (BW)', 'AT in years', 'population']
        I=params[keys[0]]*params[keys[1]]*params[keys[3]]*params[keys[4]]/(params[keys[5]]*params[keys[6]]*365)
        R_I=I*params[keys[2]]
        R_pop=R_I*params[keys[7]]
        MeanMinusLife=params[keys[4]]*(params[keys[6]]-params[keys[4]])*R_I
        # print("I",I)
        return {
            "R_ind":R_I,
            "R_pop":R_pop,
            "ССОПЖ":MeanMinusLife
        }
    def main(self,variant:str,params:dict):
        response={}
        print("variant",variant)
        print("params",params)
        # name_model=models_and_their_params(model=variant)
        # names=name_model.get_key_name_list()
        match variant:
            case "третья": response=self.calculate_third_risk(params)
        return response