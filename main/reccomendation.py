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
    def top_match(self,key,n):


        scores= [(self.s.sim_pearson(key,keys,self.data),keys) for keys in self.data if keys != key]
        scores.sort()
        scores.reverse()
        print scores[0:n]






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
r.top_match('Toby',3)
