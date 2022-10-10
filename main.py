from FMD import FMD

fmnist_dir = './fmnist'
label_names = ['top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankel_boot']
fmnist_label_dirs = [f'{fmnist_dir}/{label_name}'for label_name in label_names]

fmd = FMD()

fmd.show_all_effectiveness(fmnist_label_dirs)