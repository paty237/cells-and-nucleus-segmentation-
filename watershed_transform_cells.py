# pour la segmentation uniquement des cellules, cest en effet le meme sauf qu'on change quelque ligne de code:
# - le seuil qui devient biensur plus grand en fonction de l'histogramme 
# - puisque t change on change aussi le nouveau mask qui prend uniquement les objets larges
# - min distance qu'il faut faire varier au niveau de l'application des marqueurs pour eviter des sursegmentation avec plusieurs marqueurs sur un meme objet .


t =225
mask = im3<=t
# operations morphologiques ouverture et fermeture
mask = closing(opening(mask, disk(7)), disk(2))
plt.figure()
plt.subplot(121)
plt.imshow(mark_boundaries(im3,mask))
plt.subplot(122)
plt.imshow(mask)
plt.show()


lab = label(mask, connectivity=1)

# histogram of sizes:
obj_sizes = []
for i in range(1,lab.max()+1):
    obj_sizes += [(lab==i).sum()]
obj_sizes = np.array(obj_sizes)
plt.figure()
plt.hist(obj_sizes, bins=100)
plt.show()

lab_small = np.zeros_like(lab)
for i in range(1,lab.max()):
    if( (lab==i).sum() < 700 ):
        lab_small[lab==i] = i
plt.figure()
plt.imshow(lab_small)
plt.show()

props = regionprops(lab)
features = np.zeros((lab.max(),3))
for obj in props:
    features[obj.label-1,:] = [obj.solidity, (obj.major_axis_length+1)/(obj.minor_axis_length+1), obj.area]
plt.figure()
plt.scatter(features[:,0], features[:,1])
plt.show()


min_solidity = 0.9
max_axis = 1.75
max_area = 700
idobjs = np.arange(1,lab.max()+1)
idsmall = idobjs[(features[:,0] > min_solidity)*(features[:,1] < max_axis)*(features[:,2] < max_area)]
idlarge = idobjs[False==((features[:,0] > min_solidity)*(features[:,1] < max_axis)*(features[:,2] < max_area))]

lab_small = np.zeros_like(lab)
lab_large = np.zeros_like(lab)
for i in idsmall:
    lab_small[lab==i] = i
for i in idlarge:
    lab_large[lab==i] = i
plt.figure()
plt.subplot(121)
plt.imshow(lab_small)
plt.subplot(122)
plt.imshow(lab_large)
plt.show()


mask =lab_large
distance = distance_transform_edt(mask)

markers = peak_local_max(distance, min_distance=45, indices=True)
plt.figure()
plt.imshow(im3)
plt.plot(markers[:,1],markers[:,0],'b+')

grad = gradient(mask,disk(1))
markers = label(peak_local_max(distance, min_distance=45, indices=False))
ws = watershed(grad,markers,mask=mask)
plt.figure(figsize =(10,7))
plt.subplot(1,2,1)
plt.imshow(mark_boundaries(im3,ws))
plt.subplot(1,2,2)
plt.imshow(ws,cmap="twilight")
plt.show()

