import numpy as np
from pydmd import DMD, MrDMD
from PIL import Image
from dmd_utils import getVideoFrames

X = getVideoFrames('data/MOT16-13-raw.webm',(100,150))
mrdmd = MrDMD(svd_rank=6, max_level=4, max_cycles=1)
#X = X.astype(np.float64)
print("input shape: " + str(X.T.shape))
print("input: " + str(X.T))
mrdmd.fit(X.T)
#mrdmd.plot_eigs()
#mrdmd.plot_modes_2D()
print("modes shape: " + str(mrdmd.modes.shape))
print("mrdmd_modes: " + str(mrdmd.modes.T))
#print(dmd.dynamics)
#post_dmd = np.reshape(dmd.reconstructed_data.T.real[0].astype(np.uint8), (540,960,3))
#new_image = Image.fromarray(post_dmd,'RGB')
#new_image.show(title='after compression')
'''for i in range(5):
    recon = mrdmd.partial_reconstructed_data(i).T[0].real
    print("reconstructed shape: " + str(recon.shape))
    image = Image.fromarray(np.reshape(recon,(540,960,3)).astype(np.uint8))
    image.show()'''
count=0
for mode in mrdmd.modes.T.real:
    print(mode)
    if max(mode) != 0:
        image = Image.fromarray(np.reshape(mode*255/max(mode), (540,960,3)).astype(np.uint8),'RGB')
        image.show("mode #"+str(count))
    count += 1
