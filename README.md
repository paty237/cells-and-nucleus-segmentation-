# cells-and-nucleus-segmentation
# Introduction 
L’objectif principal de ce projet  est la segmentation cellulaire pour l’analyse automatisée d’échantillons de cytologie cervicale. C’est à dire la cible est d’extraire les limites du cytoplasme et du noyau  à partir d’images de cytologie cervicale.
# compatibilite 
Ce code a été testé sur Windows 7 , Dépendances - python, OpenCV ,skimage 
# Méthodes utilisées
_  detection des contours
_ calcul des gradients 
_ recherche de seuil 
_ Algorithme watershed transform
# Résultats obtenues 
# pour la segmentation des noyaux 
![image](https://user-images.githubusercontent.com/63290119/113273256-c32e8b80-92dc-11eb-89b0-baf6a83d39e7.png)
![image](https://user-images.githubusercontent.com/63290119/113273293-ccb7f380-92dc-11eb-8db7-ce0b9c3fa098.png)
![image](https://user-images.githubusercontent.com/63290119/113273371-dd686980-92dc-11eb-8926-aac1ece98584.png)
# pour la segmentation des cellules 
![image](https://user-images.githubusercontent.com/63290119/113273582-14d71600-92dd-11eb-9e48-38fbfb30081b.png)
![image](https://user-images.githubusercontent.com/63290119/113273610-1d2f5100-92dd-11eb-9f8c-8834798407d4.png)
![image](https://user-images.githubusercontent.com/63290119/113273658-2a4c4000-92dd-11eb-8d02-79d6b8144196.png)
# Travaux futurs 
mise en oeuvre d'un reseau neuronal (U-net ) vue qu'il est plus efficace quand il s'agit de la segmentation dans le domaine médical 
