from math import sqrt

class similarity:

    # Returns the Pearson correlation coefficient for p1 and p2
    def sim_pearson(self,x,y):

        # Add up all the preferences
        sum1=sum(x)
        sum2=sum(y)
        # Sum up the squares
        sum1Sq=sum([pow(i,2) for i in x])
        sum2Sq=sum([pow(i,2) for i in y])
        # Sum up the products
        pSum=sum([i*j for i,j in zip(x,y)])
        # Calculate Pearson score
        num=pSum-(sum1*sum2/len(x))
        den = sqrt((sum1Sq-pow(sum1,2)/len(x))*(sum2Sq-pow(sum2,2)/len(x)))
        if den==0: return 0
        r=num/den
        return r


sm = similarity()
print sm.sim_pearson([1,2,3,2323,5,6],[1,2,3,4,5,6])
