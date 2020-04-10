import numpy as np
from dmd_utils import getVideoFrames, shape_frames
from pydmd import DMD, MrDMD
shape = (540,960,3)
frames = getVideoFrames('data/test_video.webm', (75,200))
dmd = DMD(svd_rank=6)
dmd.fit(frames.T)
mrdmd = MrDMD(svd_rank=6, max_level=4, max_cycles=1)
mrdmd.fit(frames.T.astype(np.float64))

dmd_frames = dmd.reconstructed_data.real.T.astype(np.uint8)
shape_frames(dmd_frames,"data/dmd_test.avi",shape)

for i in range(4):
    mrdmd_frames = mrdmd.partial_reconstructed_data(i).real.T.astype(np.uint8)
    shape_frames(mrdmd_frames,"data/mrdmd_level%d_test.avi"%i, shape)
mrdmd_frames = mrdmd.reconstructed_data.real.T.astype(np.uint8)
shape_frames(mrdmd_frames,"data/mrdmd_all_test.avi",shape)

