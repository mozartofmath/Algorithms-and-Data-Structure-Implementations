class proto_vEB:
    def __init__(self,u):
        if u == 2:
            self.u = 2
            self.summary = None
            self.cluster = [0,0]
        else:
            self.u = u
            self.sqrt_u = int(self.u**0.5)
            self.summary = proto_vEB(self.sqrt_u)
            self.cluster = [proto_vEB(self.sqrt_u) for x in range(self.sqrt_u)]

    def Member(self,x):
        if self.u == 2:
            return self.cluster[x]
        else:
            high = x // self.sqrt_u
            low = x % self.sqrt_u
            return self.cluster[high].Member(low)

    def Min(self):
        if self.u == 2:
            if self.cluster[0] == 1:
                return 0
            elif self.cluster[1] == 1:
                return 1
            else:
                return None
        else:
            min_cluster = self.summary.Min()
            if min_cluster == None:
                return None
            return self.sqrt_u*min_cluster + self.cluster[min_cluster].Min()

    def Max(self):
        if self.u == 2:
            if self.cluster[1] == 1:
                return 1
            elif self.cluster[0] == 1:
                return 0
            else:
                return None
        else:
            max_cluster = self.summary.Max()
            if max_cluster == None:
                return None
            return self.sqrt_u*max_cluster + self.cluster[max_cluster].Max()

    def Successor(self,x):
        if self.u == 2:
            if x == 0 and self.cluster[1] == 1:
                return 1
            else:
                return None
        else:
            high = x // self.sqrt_u
            low = x % self.sqrt_u
            offset = self.cluster[high].Successor(low)
            if offset != None:
                return high*self.sqrt_u + offset
            else:
                succ_cluster = self.summary.Successor(high)
                if succ_cluster == None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].Min()
                    return succ_cluster*self.sqrt_u + offset

    def Predecessor(self,x):
        if self.u == 2:
            if x == 1 and self.cluster[0] == 1:
                return 0
            else:
                return None
        else:
            high = x // self.sqrt_u
            low = x % self.sqrt_u
            offset = self.cluster[high].Predecessor(low)
            if offset != None:
                return high*self.sqrt_u + offset
            else:
                succ_cluster = self.summary.Predecessor(high)
                if succ_cluster == None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].Max()
                    return succ_cluster*self.sqrt_u + offset

    def Insert(self,x):
        if self.u == 2:
            self.cluster[x] = 1
        else:
            high = x // self.sqrt_u
            low = x % self.sqrt_u
            self.cluster[high].Insert(low)
            self.summary.Insert(high)

t = proto_vEB(16)





























