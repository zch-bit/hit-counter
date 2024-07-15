import unittest
from hit_counter import HitCounter


class TestHitCounter(unittest.TestCase):

    def test_hit_counter(self):
        counter = HitCounter()

        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.get_hits(4), 3)  # Should return 3 hits: [ 1 2 3]

        counter.hit(300)
        self.assertEqual(counter.get_hits(300), 4)  # Should return 4 hits: [1 2 3 300]
        self.assertEqual(counter.get_hits(301), 3)  # Should return 3 hits after 300: [2 3 300]

        counter.hit(301)
        counter.hit(302)
        #self.assertEqual(counter.get_hits(303), 3)  # Should return 3 hits: [300, 301, 302]
        self.assertEqual(counter.get_hits(601), 1)  # Should return 1 hits: [302]
        self.assertEqual(counter.get_hits(602), 0)  # Should return 0 hits: []

    def test_no_hits(self):
        counter = HitCounter()
        self.assertEqual(counter.get_hits(100), 0)
        self.assertEqual(counter.get_hits(200), 0)

    def test_old_hits(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.get_hits(301), 2)  # All hits are outside the 5 minute window


if __name__ == '__main__':
    unittest.main()
