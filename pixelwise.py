images_names = os.listdir(images_dir)
img_count = len(images_names)
difference_matrix = np.zeros((img_count, img_count))
similarity_matrix = np.zeros((img_count, img_count))
names = []
for i in range(img_count):
    names.append(images_names[i])
    current_image = cv2.imread(os.path.join(images_dir, images_names[i]))
    gray_current = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
    for j in range(img_count):
        target_img = cv2.imread(os.path.join(images_dir, images_names[j]))
        target_img = cv2.resize(target_img, (current_image.shape[1], current_image.shape[0]))
        gray_target = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
        dif = (np.sum(current_image != target_img))
        count_px = current_image.shape[0] * current_image.shape[1] * 3
        # на сколько похожи 
        elem = round((1 - (dif / count_px)), 5)
        similarity_matrix[i][j] = elem * 100

        # на сколько отличаютс€ 
        elem = round((dif / count_px), 5)
        difference_matrix[i][j] = elem * 100

print("ћатрица различий")
print(difference_matrix)

print()
print("ћатрица схожести")
print(similarity_matrix)
