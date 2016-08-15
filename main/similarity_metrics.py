from math import sqrt

class similarity:

    """
        Dataset format

        {
            key1:
                {
                    inner_key1 : inner_value1
                    inner_key2 : inner_value2
                    .......
                    .......
                }
            key2:
                {
                    inner_key1 : inner_value1
                    inner_key2 : inner_value2
                    .......
                    .......
                }
        }

    """
    def get_mutually_rated(self,key1,key2,data):
        common = []
        for inner_keys in data[key1]:
            if inner_keys in data[key2]:
                common.append(inner_keys)
        # print common
        return common

    def sim_pearson(self,key1,key2,data):

        mut_lst = self.get_mutually_rated(key1,key2,data)

        n = len(mut_lst)
        if n==0:
            return 0
        # Add up all the preferences
        sum1=sum([data[key1][i] for i in mut_lst])
        sum2=sum([data[key2][i] for i in mut_lst])
        # Sum up the squares
        sum1Sq=sum([pow(data[key1][i],2) for i in mut_lst])
        sum2Sq=sum([pow(data[key2][i],2) for i in mut_lst])
        # Sum up the products
        pSum=sum([(data[key1][i]*data[key2][i]) for i in mut_lst])
        # Calculate Pearson score
        num=pSum-(sum1*sum2/n)
        den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
        if den==0: return 0
        r=num/den
        return r


# sm = similarity()
# print sm.sim_pearson([1,2,3,2323,5,6],[1,2,3,4,5,6])
