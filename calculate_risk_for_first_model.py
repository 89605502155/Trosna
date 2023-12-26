import json
import math

class calculate_risk_for_first_model:
    def __init__(self):
        pass

    def __read_json_file(self):
        f = open('probit.json', "r")
        self.data = json.loads(f.read())
        f.close()

    def __calculate_probit_possibility(self,probit_value):
        if probit_value<self.data["probit_array"][0]:
            return 0
        elif probit_value>self.data["probit_array"][-1]:
            return 100
        else:
            for i in range(1,len(self.data["probit_array"])):
                if probit_value==self.data["probit_array"][i]:
                    return self.data["probit_func"][str(self.data["probit_array"][i])]
                elif probit_value<self.data["probit_array"][i]:
                    r1=self.data["probit_array"][i]-probit_value
                    r2=probit_value-self.data["probit_array"][i-1]
                    if r1<=r2:
                        return self.data["probit_func"][str(self.data["probit_array"][i])]
                    else:
                        return self.data["probit_func"][str(self.data["probit_array"][i-1])]
    def __calculation(self,params)->dict:
        keys = list(params.keys())
        try:
            number_car_with_dangerous=params[keys[0]]/params[keys[1]]
            # print(number_car_with_dangerous)
            lambda_=number_car_with_dangerous*params[keys[2]]*(10**(-6))*params[keys[3]]*params[keys[4]]
            # print(lambda_)
            c_ppm=params[keys[8]]*params[keys[7]]/params[keys[6]]
            # print(c_ppm)
            probit_=params[keys[12]]+(params[keys[13]]*(math.log((c_ppm**params[keys[14]])*params[keys[11]])))
            # print(probit_)
            probit_possibility=self.__calculate_probit_possibility(probit_)
            # print(probit_possibility)
            R_I = probit_possibility * 0.01 * lambda_ * params[keys[5]] / (24 * 60)
            # print(R_I)
            number_of_people=params[keys[9]]*0.01*params[keys[10]]
            R_pop=number_of_people*R_I
        except ZeroDivisionError:
            R_I = 0
            R_pop = 0
        return {
            "R_ind": R_I,
            "R_kol": R_pop
        }
    def main(self,param_dict)->dict:
        self.__read_json_file()
        return self.__calculation(param_dict)

