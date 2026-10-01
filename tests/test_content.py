"""Mutation tests for the pre-build gate (stdlib only)."""
import copy
import json
from pathlib import Path
import unittest
from validate_content import validate_chapter, validate_ledger

ROOT = Path(__file__).resolve().parents[1]


class ContentGateTests(unittest.TestCase):
    def setUp(self):
        self.chapter = json.loads((ROOT / 'data/ch01.json').read_text())

    def validate(self):
        validate_chapter(self.chapter, 1, 'Diarrhea', 1)

    def test_valid(self):
        self.validate()

    def test_schema_mutations(self):
        original = copy.deepcopy(self.chapter)
        changes = [('opts', ['one', 'two', 'three']), ('ans', 4), ('ans', True),
                   ('exp', 'Wrong. (Book p9)'), ('id', 'MED-C1-02'),
                   ('page', 0), ('fmt', 'unsupported')]
        for key, value in changes:
            with self.subTest(key=key, value=value):
                self.chapter = copy.deepcopy(original)
                self.chapter['questions'][0][key] = value
                with self.assertRaises(ValueError):
                    self.validate()

    def test_page_order(self):
        self.chapter['questions'][0]['page'] = 2
        self.chapter['questions'][0]['exp'] = 'Example. (Book p2)'
        with self.assertRaisesRegex(ValueError, 'page order'):
            self.validate()

    def test_fillup(self):
        next(q for q in self.chapter['questions'] if q['fmt'] == 'fillup')['q'] = 'Missing blank'
        with self.assertRaisesRegex(ValueError, 'blank'):
            self.validate()

    def test_true_false_balance(self):
        q = next(q for q in self.chapter['questions'] if q['fmt'] == 'truefalse')
        q['opts'] = ['True — a', 'True — b', 'True — c', 'False — d']
        with self.assertRaisesRegex(ValueError, 'two True'):
            self.validate()

    def test_unit_order(self):
        self.chapter['units'][0]['qs'].reverse()
        with self.assertRaises(ValueError):
            self.validate()

    def test_missing_unit(self):
        self.chapter['units'].pop()
        with self.assertRaisesRegex(ValueError, 'unit coverage'):
            self.validate()

    def test_guide_lines(self):
        self.chapter['units'][0]['guide'] = 'Single line'
        with self.assertRaisesRegex(ValueError, '2–4 lines'):
            self.validate()

    def test_ledger(self):
        chapters = [json.loads((ROOT / f'data/ch{n:02}.json').read_text()) for n in range(1, 62) if (ROOT / f'data/ch{n:02}.json').exists()]
        ledger = json.loads((ROOT / 'audit/coverage.json').read_text())
        validate_ledger(chapters, ledger)
        bad = copy.deepcopy(ledger)
        bad[0]['page'] = 999
        with self.assertRaisesRegex(ValueError, 'page mismatch'):
            validate_ledger(chapters, bad)
        missing = [r for r in ledger if r['question'] != 'MED-C1-01']
        with self.assertRaisesRegex(ValueError, 'complete question coverage'):
            validate_ledger(chapters, missing)
        with self.assertRaisesRegex(ValueError, 'duplicate point'):
            validate_ledger(chapters, ledger + [ledger[0]])


if __name__ == '__main__':
    unittest.main()
