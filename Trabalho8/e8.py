import numpy as np
import pandas as pd
from scipy.spatial import distance
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

np.seterr(divide='ignore',invalid='ignore')

TAMANHO_COLUNAS = 72

cols = list(range(TAMANHO_COLUNAS))
data = pd.read_csv('leukemia_new.csv',names=cols)

data = pd.DataFrame.transpose(data)

y = data[0]

data = data.loc[:,1:]

k = int(input("Insira k-media(2 ou 3):\t "))

maxInterations = 1

actualMaxSize = 0
iterations = 0
protoClusterDictionary = {}
clusterLengths = []
clustersOld = np.array([[] for i in range(k)])


while iterations < maxInterations:
    if k == 2:
        centersOld = np.array([data.loc[0,:], data.loc[21,:]])
    elif k == 3:
        centersOld = np.array([data.loc[0,:], data.loc[20,:],data.loc[30,:]])
    centers = centersOld
    while True:
        clusters = [[] for i in range(k)]
        for i in range(len(y)):
            amostraAtual = data.iloc[i,:]
            distances = []
            closest = []
            
            for j in range(len(centers)):
                dist_ponto_centroide = distance.euclidean(amostraAtual,centers[j])
                distances.append([dist_ponto_centroide])
                
                if distances[j] == min(distances):
                    closest = centers[j]
                    closest_index = j 

            clusters[closest_index].append(amostraAtual)

        showClusters = clusters
        for i in range(len(clusters)):
            clusters[i] = np.array(clusters[i])
            for j in range(len(clusters[i])):
                clusters[i][j] = np.array(clusters[i][j])
        clusters = np.array(clusters)
        centersOld = centers
        centers = []
        for i in range(len(clusters)):
            if clusters[i].size == 0:
                centers.append(centersOld[i])
            else:
                centers.append(clusters[i].mean(0))
               
        centers = np.array(centers)
        
        equals = 1
        if (clusters.shape == clustersOld.shape):
            for i in range(len(clusters)):
                if not np.array_equal(clusters[i], clustersOld[i]):
                    equals = 0
        else:
            equals = 0
        if equals == 1:
            for i in range(len(clusters)):
                clusterLengths.append(len(clusters[i]))
            
            actualMaxSize = max(clusterLengths)
            protoClusterDictionary[actualMaxSize] = showClusters
            break
        
        clustersOld = clusters
    iterations = iterations + 1
chosenClustersKey = min(list(protoClusterDictionary.keys()))
showClusters = protoClusterDictionary.get(chosenClustersKey)

clusLengths = []
for i in range(len(showClusters)):
    clusLengths.append(len(showClusters[i]))

clusList = []
for i in range(len(clusLengths)):
    if clusLengths[i] != 0:
        aux = np.full((clusLengths[i],1), i)
        showClusters[i] = np.hstack((aux, showClusters[i]))
        clusList.append(showClusters[i])

clusList = tuple(clusList)

showClusters = np.vstack(clusList)     

showClusters = pd.DataFrame(showClusters)
t = showClusters[0]
X = showClusters.loc[:,1:]





X_norm = (X - X.min())/(X.max() - X.min())
pca = PCA(n_components=k)
fig = plt.figure()
fig.canvas.set_window_title('Trabalho 8: Parte 1')
transformed = pd.DataFrame(pca.fit_transform(X_norm))
plt.scatter(transformed[t==0][0], transformed[t==0][1], label=('Classe 0', clusLengths[0]), c='black')
plt.scatter(transformed[t==1][0], transformed[t==1][1], label=('Classe 1', clusLengths[1]), c='yellow')
plt.savefig('k2-cluster.png')
if k == 3:
    plt.scatter(transformed[t==2][0], transformed[t==2][1], label=('Classe 2: ', clusLengths[2]), c='lightgreen')
    plt.savefig('k3-cluster.png')
plt.legend()
plt.show()


Z = data

Z_norm = (Z - Z.min())/(Z.max() - Z.min())
pca = PCA(n_components=2)
fig = plt.figure()
fig.canvas.set_window_title('Trabalho 8: Parte 2')
transformed_og = pd.DataFrame(pca.fit_transform(Z_norm))
plt.scatter(transformed_og[y==1][0], transformed_og[y==1][1], label='ALL', c='black')
plt.scatter(transformed_og[y==2][0], transformed_og[y==2][1], label='AML', c='green')
plt.savefig('endings.png')
plt.legend()
plt.show()       