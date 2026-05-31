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


    def dividing(self):
        lower = [i['lower_limit'] for i in self.data]
        upper = [i['upper_limit'] for i in self.data]
        frequency = [i['frequency'] for i in self.data]
        return lower, upper, frequency


    def x(self):
        lower, upper, _ = self.dividing()

        new_x = [(x+y)/2 for x,y in zip(lower,upper)]
        return new_x

    def cum_freq(self):
        _, _, frequency = self.dividing()
        cf = []
        loop = frequency[0]

        for i in range(len(frequency)):
            loop += frequency[i]
            cf.append(loop)
        return cf

    def n_by_2(self):
        total_f = self.cum_freq()[-1]
        return total_f / 2





