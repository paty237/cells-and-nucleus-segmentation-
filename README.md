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
![image](https://user-images.githubusercontent.com/63290119/113278104-c7a97300-92e1-11eb-9215-2a3d17499abf.png)
![image](https://user-images.githubusercontent.com/63290119/113278703-85346600-92e2-11eb-8b81-f5f9bb48ed0a.png)

![image](https://user-images.githubusercontent.com/63290119/113278617-6f26a580-92e2-11eb-9442-e8a4b24a09c9.png)

![image](https://user-images.githubusercontent.com/63290119/113273371-dd686980-92dc-11eb-8926-aac1ece98584.png)
# pour la segmentation des cellules 
![image](https://user-images.githubusercontent.com/63290119/113278246-fd4e5c00-92e1-11eb-92f2-d07755323c8f.png)
![image](https://user-images.githubusercontent.com/63290119/113278425-34247200-92e2-11eb-8be3-7f600c753d7c.png)
![image](https://user-images.githubusercontent.com/63290119/113273610-1d2f5100-92dd-11eb-9f8c-8834798407d4.png)
![image](https://user-images.githubusercontent.com/63290119/113273658-2a4c4000-92dd-11eb-8d02-79d6b8144196.png)
# Travaux futurs 
mise en oeuvre d'un reseau neuronal (U-net ) vue qu'il est plus efficace quand il s'agit de la segmentation dans le domaine médical 
