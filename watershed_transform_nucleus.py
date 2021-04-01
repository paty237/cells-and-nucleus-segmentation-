t =110
mask = im<t
mask = closing(opening(mask, disk(3)), disk(2))
plt.figure()
plt.subplot(121)
plt.imshow(mark_boundaries(im,mask))
plt.subplot(122)
plt.imshow(mask)
plt.show()

lab = label(mask, connectivity=1) # connectivity=1 on ne  prend pas la diagonale , connectivity=2 on prend la diagonal
# donc les pixels qui sont en diagonale sont considéré comme connectes donc ducoup font partir du meme objet.
print(lab.max())
plt.show()

obj_sizes = []
for i in range(1,lab.max()+1): 
    obj_sizes += [(lab==i).sum()]
obj_sizes = np.array(obj_sizes)
plt.figure()
plt.hist(obj_sizes, bins=100)
plt.show()

lab_noyau = np.zeros_like(lab)
for i in range(1,lab.max()):
    if( (lab==i).sum() < 218):
        lab_noyau[lab==i] = i
plt.figure()
plt.imshow(lab_noyau)
plt.show()

print(mask.sum()/218)
# me donne environ 47 cellules dans mon image dependant ainsi du seuil.

props = regionprops(lab)
features = np.zeros((lab.max(),3))
for obj in props:
    features[obj.label-1,:] = [obj.solidity, (obj.major_axis_length+1)/(obj.minor_axis_length+1), obj.area]
plt.figure()
plt.scatter(features[:,0], features[:,1])
plt.show()

min_solidity = 0.92
max_axis = 1.81
max_area = 218
idobjs = np.arange(1,lab.max()+1)
idnoyau = idobjs[(features[:,0] > min_solidity)*(features[:,1] < max_axis)*(features[:,2] < max_area)]
idlarge = idobjs[False==((features[:,0] > min_solidity)*(features[:,1] < max_axis)*(features[:,2] < max_area))]

lab_noyau = np.zeros_like(lab)
lab_large = np.zeros_like(lab)
for i in idsmall:
    lab_noyau[lab==i] = i
for i in idlarge:
    lab_large[lab==i] = i
plt.figure()
plt.subplot(121)
plt.imshow(lab_noyau)
plt.subplot(122)
plt.imshow(lab_large)
plt.show()

mask = lab_noyau
distance = distance_transform_edt(mask)


markers = peak_local_max(distance, min_distance=3, indices=True)
plt.figure()
plt.imshow(im)
plt.plot(markers[:,1],markers[:,0],'b+')


grad = gradient(mask,disk(1))
markers = label(peak_local_max(distance, min_distance=3, indices=False)) 
#la methode label est utiliser ici pour etiquetter chaque marqueur avec un identifiant different  
ws = watershed(grad,markers,mask=mask) # application de la methode watershed sur l'image degrade avec les marqueurs
plt.figure(figsize =(9,6))
plt.subplot(1,2,1)
plt.imshow(mark_boundaries(im,ws))# cette methode  mark_boundaries permet d'afficher les differentes frontieres entre les regions
plt.subplot(1,2,2)
plt.imshow(ws,cmap="twilight")
plt.show()

