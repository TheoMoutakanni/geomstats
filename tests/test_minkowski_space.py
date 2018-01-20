"""Unit tests for minkowski space module."""

import numpy as np
import unittest

from geomstats.minkowski_space import MinkowskiSpace


class TestMinkowskiSpaceMethods(unittest.TestCase):
    TIME_LIKE_DIM = 0
    DIMENSION = 2
    SPACE = MinkowskiSpace(DIMENSION)
    METRIC = SPACE.metric

    def test_inner_product_matrix(self):
        result = self.METRIC.inner_product_matrix()

        expected = np.eye(self.DIMENSION)
        expected[self.TIME_LIKE_DIM, self.TIME_LIKE_DIM] = -1
        self.assertTrue(np.allclose(result, expected))

    def test_inner_product(self):
        point_a = np.array([0, 1])
        point_b = np.array([2, 10])

        result = self.METRIC.inner_product(point_a, point_b)
        expected = np.dot(point_a, point_b)
        expected -= (2 * point_a[self.TIME_LIKE_DIM]
                     * point_b[self.TIME_LIKE_DIM])
        self.assertTrue(np.allclose(result, expected))

    def test_squared_norm(self):
        point = np.array([-2, 4])

        result = self.METRIC.squared_norm(point)
        expected = np.dot(point, point)
        expected -= 2 * point[self.TIME_LIKE_DIM] * point[self.TIME_LIKE_DIM]
        self.assertTrue(np.allclose(result, expected))


if __name__ == '__main__':
        unittest.main()