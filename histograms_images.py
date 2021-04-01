 # Maintenant on peut donc segmenter l'image  et ducoup il existe  plusieurs methodes qui sont regroupées en deux groupes: les methodes automatiques et la methode non automatiques.
 # Ducoup   vue le type d'image à analyser,la  methode de segmentation a utilisé  est  la methode automatisée plus particulierment le watershed transform.
 # Watershed transform est une methode de segmentation automatique  qui permet de diviser l'image en ces differents bassins, permettant ainsi une segmentation de l'image. 
 # Pour un debut on va utiliser la methode distance transform qui generallement est utilisé pour la detection des noyaux dans le cellules.
 # on va premierement essayer de segmenter uniquement les  noyaux et ensuites vois si cest possibles de segmenter aussi unique le cytoplasme de la cellule.ceci peut etre fait si seulement on a un seuil t( qui peut etre determiner automatiquement "optimal and otsu threshold" ou  manuellement "manual threshold").
 # Avant d'appliquer une methode de segmentation on va tout d'abord determiner l'histogramme de chaque image afin de trouver le seuil adequat grace a  une meilleure visualisation des pixels.

img_copy = np.copy(img)
plt.figure(figsize=(6,3))
plt.hist(img_copy.ravel(), bins=255)
plt.show()

img2_copy = np.copy(img2)
plt.figure(figsize=(6,3))
plt.hist(img2_copy.ravel(), bins=255)
plt.show()

img3_copy = np.copy(img3)
plt.figure(figsize=(6,3))
plt.hist(img3_copy.ravel(), bins=255)
plt.show()

img7_copy = np.copy(img7)
plt.figure(figsize=(6,3))
plt.hist(img7_copy.ravel(), bins=255)
plt.show()
