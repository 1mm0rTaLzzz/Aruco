import numpy as np

camera_matrix = np.array([[623.69211543, 0., 423.08454002],
                 [0., 625.22607753, 214.72853252],
                 [0., 0., 1.]])

distortion_coefficient = np.array([[-0.02766246, -0.04359756, -0.00698582, 0.01280042, -0.34497222]])

rotation_vectors = np.array(([[-0.76088923], [0.63364828], [1.41109258]], [[-0.31871235], [0.4589448], [1.44303834]],
                    [[-0.05401971], [-0.80789265], [-1.36391512]], [[0.35272296], [0.26593669], [1.25298769]],
                    [[0.15845486], [0.95523601], [1.27633153]], [[0.28651076], [-0.84243653], [-1.30221809]],
                    [[-0.38554522], [-1.05857168], [-1.25347326]]))

translation_vectors = np.array(([[1.46376672], [-1.16830377], [21.82019119]],
                                [[-0.56336271], [-2.00377684], [18.53913993]],
                       [[-3.81874164], [3.06918413], [15.64245205]],
                                [[2.44179746], [-2.36434736], [13.00450451]],
                       [[1.80537823], [-2.09545166], [17.74163493]],
                                [[-5.33124391], [2.98589006], [14.1500819]],
                       [[-4.07655637], [1.79119804], [15.61587011]]))
