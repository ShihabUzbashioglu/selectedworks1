from PIL Import image

def images_pdf(filename,output):
    images =[]

    for file in filename :
        lm = image.open(file)
        lm = lm.convert('rgb')
        images.append(lm)

        images[0].save(output,save_all=true,append_imags= images[1:])


images_pdf(["binod_mirror.png","Binood.png","binod.jpg"],"output.pdf")