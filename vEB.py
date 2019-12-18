import math
class vEB:
    def __init__(self,u):
        if u == 2:
            self.u = u
            self.upper_root = math.ceil(u**0.5)
            self.lower_root = math.floor(u**0.5)
            self.min = None
            self.max = None
            self.summary = None
            self.cluster = None
        else:
            self.u = u
            self.upper_root = math.ceil(u**0.5)
            self.lower_root = math.floor(u**0.5)
            self.min = None
            self.max = None
            self.summary = vEB(self.upper_root)
            self.cluster = [vEB(self.lower_root) for x in range(self.upper_root)]

    def high(self,x):
        return math.floor(x/self.lower_root)

    def low(self,x):
        return x % self.lower_root

    def index(self,x,y):
        return x*self.lower_root + y

    def Min(self):
        return self.min

    def Max(self):
        return self.max

    def Member(self,x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].Member(self.low(x))

    def Successor(self,x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min != None and x < self.min:
            return self.min

        else:
            max_low = self.cluster[self.high(x)].Max()
            if max_low != None and self.low(x) < max_low:
                offset = self.cluster[self.high(x)].Successor(self.low(x))
                return self.index(self.high(x),offset)
            else:
                succ_cluster = self.summary.Successor(self.high(x))
                if succ_cluster == None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].Min()
                    return self.index(succ_cluster,offset)
    def Predecessor(self,x):
        if self.u == 2:
            if x == 1 and self.min == 0:
                return 0
            else:
                return None
        elif self.max != None and x > self.max:
            return self.max

        else:
            min_low = self.cluster[self.high(x)].Min()
            if min_low != None and self.low(x) > min_low:
                offset = self.cluster[self.high(x)].Predecessor(self.low(x))
                return self.index(self.high(x),offset)
            else:
                pred_cluster = self.summary.Predecessor(self.high(x))
                if pred_cluster == None:
                    if self.min != None and x > self.min:
                        return self.min
                    else:
                        return None
                else:
                    offset = self.cluster[pred_cluster].Max()
                    return self.index(pred_cluster,offset)

    def Empty_Insert(self,x):
        self.min = x
        self.max = x

    def Insert(self,x):
        if self.min == None:
            self.Empty_Insert(x)
        else:
            if x < self.min:
                temp = self.min
                self.min = x
                x = temp
            if self.u > 2:
                if self.cluster[self.high(x)].Min() == None:
                    self.summary.Insert(self.high(x))
                    self.cluster[self.high(x)].Empty_Insert(self.low(x))
                else:
                    self.cluster[self.high(x)].Insert(self.low(x))
            if x > self.max:
                self.max = x

    def Delete(self,x):
        if self.min == self.max:
            self.min = None
            self.max = None
        elif self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
                self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.summary.Min()
                x = self.index(first_cluster, self.cluster[first_cluster].Min())
                self.min = x

            self.cluster[self.high(x)].Delete(self.low(x))
            if self.cluster[self.high(x)].Min() == None:
                self.summary.Delete(self.high(x))
                if x == self.max:
                    summary_max = self.summary.Max()
                    if summary_max == None:
                        self.max = self.min
                    else:
                        self.max = self.index(summary_max, self.cluster[summary_max].Max())
            elif x == self.max:
                self.max = self.index(self.index(self.high(x),self.cluster[self.high(x)].Max()))

t = vEB(16)                            


















            
            
