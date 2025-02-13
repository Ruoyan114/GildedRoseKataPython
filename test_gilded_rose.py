# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras, Hand of Ragnaros", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = [item.name for item in items]
        self.assertEqual(["Sulfuras"], all_items)


    # The Quality of an item is never more than 50
    def test_aged_brie_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)


    # Aged Brie increases in quality as it gets older
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

    # the quality of an item should never be negative
    def test_quality_never_negative(self):
        items = [Item("Normal Item", 3, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Syntax error test
    def test_gilded_rose_incorrect_instantiation(self):
        with self.assertRaises(TypeError):
            gilded_rose = GildedRose()


if __name__ == '__main__':
    unittest.main()