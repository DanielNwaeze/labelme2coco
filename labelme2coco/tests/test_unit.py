import unittest


class Tests(unittest.TestCase):

    def test_read_and_validate_coco_annotation(self):
        from labelme2coco.utils import read_and_validate_coco_annotation

        false_sample_list = ["tests/data/coco_false_" + str(ind)+".json" for ind in range(17)]
        true_sample_list = ["tests/data/coco_true_" + str(ind)+".json" for ind in range(2)]

        for false_sample in false_sample_list:
            _, response = read_and_validate_coco_annotation(false_sample)
            self.assertEqual(response, False)

        for true_sample in true_sample_list:
            _, response = read_and_validate_coco_annotation(true_sample)
            self.assertEqual(response, True)

    def test_lableme2coco(self):
        from labelme2coco.labelme2coco import labelme2coco
        import json
        import os

        labelme_folder = "tests/data/labelme_annot"
        save_json_path = "tests/data/test_coco.json"
        labelme2coco(labelme_folder, save_json_path)

        with open(save_json_path) as json_file:
            test_coco = json.load(json_file)
        self.assertEqual(test_coco["annotations"][1]["bbox"][1], 96.0)
        self.assertEqual(test_coco["annotations"][1]["id"], 2)
        self.assertEqual(test_coco["annotations"][1]["category_id"], 1)
        self.assertEqual(test_coco["annotations"][1]["segmentation"][0][2], 0.9361702127659877)
        self.assertEqual(len(test_coco["annotations"]), 3)
        self.assertEqual(test_coco["images"][0]["height"], 375)
        self.assertEqual(len(test_coco["images"]), 1)
        self.assertEqual(test_coco["categories"][0]["name"], "bus")
        self.assertEqual(len(test_coco["categories"]), 2)

        os.remove(save_json_path)


if __name__ == '__main__':
    unittest.main()
