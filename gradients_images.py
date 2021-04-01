img= cv2.imread('image 1.png')
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]
gr = skr.gradient(r, disk(3))
gg = skr.gradient(g, disk(3))
gb = skr.gradient(b, disk(3))
grad = np.maximum(np.maximum(gr,gg),gb) 

img2=cv2.imread('image2.png')
r = img2[:,:,0]
g = img2[:,:,1]
b = img2[:,:,2]
gr = skr.gradient(r, disk(3))
gg = skr.gradient(g, disk(3))
gb = skr.gradient(b, disk(3))
grad2 = np.maximum(np.maximum(gr,gg),gb)

img3=cv2.imread('image3.png')
r = img3[:,:,0]
g = img3[:,:,1]
b = img3[:,:,2]
gr = skr.gradient(r, disk(3))
gg = skr.gradient(g, disk(3))
gb = skr.gradient(b, disk(3))
grad3 = np.maximum(np.maximum(gr,gg),gb)


img7=cv2.imread('image7.png')
r = img7[:,:,0]
g = img7[:,:,1]
b = img7[:,:,2]
gr = skr.gradient(r, disk(3))
gg = skr.gradient(g, disk(3))
gb = skr.gradient(b, disk(3))
grad7 = np.maximum(np.maximum(gr,gg),gb)

plt.figure(figsize=(8,4))
plt.subplot(1,4,1)
plt.imshow(grad)
plt.subplot(1,4,2)
plt.imshow(grad2)
plt.subplot(1,4,3)
plt.imshow(grad3)
plt.subplot(1,4,4)
plt.imshow(grad7)
