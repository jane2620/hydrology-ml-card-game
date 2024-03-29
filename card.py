class Card:

    def __init__(self, k, temp, precip, 
    slope, wtd, num):
        self._k = k
        self._temp = temp
        self._precip = precip
        self._slope = slope
        self._wtd = wtd
        self._num = num
        # self._group is only set from the auditionee page (where it is
        # needed)

    def __str__(self):
        # should probably make this better
        s = str(self._k)
        s += " " + str(self._temp)
        s += " " + str(self._precip)
        s += " " + str(self._slope)
        s += " " + str(self._wtd)
        s += " " + str(self._num)
        return s

    def to_dict(self):
        '''
        Returns audition object as a dictionary
        '''

        d = {}

        d['k'] = self._k
        d['temp'] = self._temp
        d['precip'] = self._precip
        d['slope'] = self._slope
        d['wtd'] = self._wtd
        d['num'] = self._num

        return d

    def get_k(self):

        return self._k

    def get_temp(self):

        return self._temp

    def get_precip(self):

        return self._precip

    def get_slope(self):

        return self._slope

    def get_wtd(self):

        return self._wtd
    
    def get_num(self):

        return self._num

    def get_color(self, var):
        if (var == "Low"):
            return "success"
        elif (var == "Medium"):
            return "warning"
        else:
            return "danger"
