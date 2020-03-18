import numpy as np
from pydmd import DMD, MrDMD
from PIL import Image
from dmd_utils import getVideoFrames

X = getVideoFrames('MOT16-09-raw.webm',(100,105))
dmd = MrDMD(svd_rank=-1, max_level=3, max_cycles=1)
print("X shape: " + str(X.T.shape))
X = X.astype(np.float)
dmd.fit(X.T)
print(dmd.reconstructed_data.real.shape)
#print(dmd.modes.real.shape)
#print(dmd.dynamics.real.shape)
post_dmd = np.reshape(dmd.reconstructed_data.T.real[0].astype(np.uint8), (540,960,3))
new_image = Image.fromarray(post_dmd,'RGB')
new_image.show(title='after compression')
count=0
for mode in abs(dmd.modes.T.real):
    image = Image.fromarray(np.reshape((mode*255/max(mode)).astype(np.uint8), (540,960,3)),'RGB')
    image.show("mode #"+str(count))
    count += 1
