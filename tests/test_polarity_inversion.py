import unittest

import numpy as np
import torch
from numpy.testing import assert_almost_equal

from torch_audiomentations import PolarityInversion


class TestPolarityInversion(unittest.TestCase):
    def test_polarity_inversion(self):
        samples = np.array([1.0, 0.5, -0.25, -0.125, 0.0], dtype=np.float32)
        sample_rate = 16000

        augment = PolarityInversion(p=1.0)
        inverted_samples = augment(
            samples=torch.from_numpy(samples), sample_rate=sample_rate
        ).numpy()
        assert_almost_equal(
            inverted_samples, np.array([-1.0, -0.5, 0.25, 0.125, 0.0], dtype=np.float32)
        )
        self.assertEqual(inverted_samples.dtype, np.float32)

    def test_polarity_inversion_multichannel(self):
        samples = np.array(
            [[1.0, 0.5, -0.25, -0.125, 0.0], [1.0, 0.5, -0.25, -0.125, 0.0]],
            dtype=np.float32,
        )
        sample_rate = 16000

        augment = PolarityInversion(p=1.0)
        inverted_samples = augment(
            samples=torch.from_numpy(samples), sample_rate=sample_rate
        ).numpy()
        assert_almost_equal(
            inverted_samples,
            np.array(
                [[-1.0, -0.5, 0.25, 0.125, 0.0], [-1.0, -0.5, 0.25, 0.125, 0.0]],
                dtype=np.float32,
            ),
        )
        self.assertEqual(inverted_samples.dtype, np.float32)
