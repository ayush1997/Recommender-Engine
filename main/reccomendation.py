from similarity_metrics import similarity




class reccomendation:

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
    data={}
    s = similarity()
    def __init__(self,dataset):
        self.data = dataset

    # Returns Top matches for an inputed key
    def top_match(self,key,n,data):


        scores= [(self.s.sim_pearson(key,keys,data),keys) for keys in data if keys != key]
        scores.sort()
        scores.reverse()
        return scores[0:n]

    def get_recommendation_collaborative(self,key):

        totals ={}
        simSums = {}
        for keys in self.data:
            print keys
            # don't compare the key to key
            if keys == key:
                continue
            sim = self.s.sim_pearson(key,keys,self.data)
            print sim
            # ignore scores of zero or lower
            if sim<=0: continue
            for inner_keys in self.data[keys]:

                if inner_keys not in self.data[key]:
                    totals.setdefault(inner_keys,0)
                    print inner_keys
                    totals[inner_keys]+=self.data[keys][inner_keys]*sim
                    simSums.setdefault(inner_keys,0)
                    simSums[inner_keys]+=sim

        # Create the normalized list
        ranking = [((totals[inner_keys]/simSums[inner_keys]),inner_keys) for inner_keys in totals.keys()]

        # Return the sorted list
        ranking.sort()
        ranking.reverse()

        print totals

    def transform_data(self):
        result = {}

        for keys in self.data:
            for inner_keys in self.data[keys]:

                result.setdefault(inner_keys,{})

                #Flip items
                result[inner_keys][keys] = self.data[keys][inner_keys]
        # print result
        return result

    def CalculateSimilar_innerkeys(self):
        result={}

        transformed = self.transform_data()

        for inner_keys in transformed:
            scores = self.top_match(inner_keys,10,transformed)
            result[inner_keys] = scores
        # print result
        return result

    def get_recommendation_contentbased(self,key):
        userRating = self.data[key]
        scores = {}
        totslSim = {}
        transformed_sim = CalculateSimilar_innerkeys()
        for inner_keys in self.data[key]:
            for other_inner_keys in transformed_sim[inner_keys]:
                # Ignore if this user has already rated this item
                if other_inner_keys in userRatings: continue

                scores.setdefault(other_inner_keys,0)
                scores[other_inner_keys]+=






Dataset={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


r  = reccomendation(Dataset)
# r.top_match('Toby',3)
# r.get_recommendation_collaborative('Claudia Puig')
new = r.transform_data()
# r1  = reccomendation(new)
r.CalculateSimilar_innerkeys()
# r1.get_recommendation_collaborative('Just My Luck')
