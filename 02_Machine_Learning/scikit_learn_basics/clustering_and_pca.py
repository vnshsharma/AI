'''
Find groups (clusters) in data such that similar points are in the same group.

EXAMPLE:
        You have a bunch of customers and want to group them based on buying habits — clustering will form groups like:

            -> High spenders

            -> Budget buyers

'''


from sklearn.cluster import KMeans

x = [[1], [2], [9], [10]]

model = KMeans(n_clusters=2, random_state=0)
model.fit(x)

print('Cluster for 2:', model.predict([[2]]))