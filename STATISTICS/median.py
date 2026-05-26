frequency_data_1 = [
    {"lower_limit": 0, "upper_limit": 10, "frequency": 5},
    {"lower_limit": 10, "upper_limit": 20, "frequency": 8},
    {"lower_limit": 20, "upper_limit": 30, "frequency": 12},
    {"lower_limit": 30, "upper_limit": 40, "frequency": 18},
    {"lower_limit": 40, "upper_limit": 50, "frequency": 7}
]

class Median:
    def __init__(self, data):
        self.data = data


    def sorting(self):
        lower = []
        upper=[]
        freq = []
        for one_dict in self.data:
            low = one_dict['lower_limit']
            up = one_dict['upper_limit']
            frq = one_dict['frequency']
            lower.append(low)
            upper.append(up)
            freq.append(frq)





