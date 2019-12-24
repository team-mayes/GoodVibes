import unittest
import os
from goodvibes_hmayes.goodvibes_hmayes import main
from common_wrangler.common import diff_lines, silent_remove, capture_stdout, capture_stderr
import logging

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
DISABLE_REMOVE = logger.isEnabledFor(logging.DEBUG)

__author__ = 'hmayes'

TEST_DIR = os.path.dirname(__file__)
MAIN_DIR = os.path.dirname(TEST_DIR)
DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

GOODVIBES_DAT = os.path.abspath(os.path.join(TEST_DIR, '..', 'Goodvibes_output.dat'))
GOODVIBES_CSV = os.path.abspath(os.path.join(TEST_DIR, '..', 'Goodvibes_output.csv'))

TEST_LOG1 = os.path.join(DATA_DIR, 'ethygly2_tzvp.log')
TEST_LOG2 = os.path.join(DATA_DIR, 'tpaegh1ats_ts.log')
TEST_LOG3 = os.path.join(DATA_DIR, 'ts3b_ircr_opt_gas.log')
TEST_LOG4 = os.path.join(DATA_DIR, 'co_gas.log')


class TestGoodVibesHM(unittest.TestCase):
    # These test/demonstrate different options
    def testFileName(self):
        test_input = [TEST_LOG1]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("-230.257454   0.083435   -230.167674   0.033971   0.033946   -230.201645   "
                                "-230.201620" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempVib(self):
        test_input = [TEST_LOG1, "-t", "788.15", "-v", "0.984"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("-230.257454   0.084552   -230.144250   0.122864   0.122499   -230.267114   "
                                "-230.266749" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testLinearMolecule(self):
        test_input = [TEST_LOG4, "--qs", "Truhlar"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("-113.322295   0.005041   -113.313948   0.022414   0.022414   -113.336362   "
                                "-113.336362" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempVibFreq(self):
        test_input = [TEST_LOG3, "-t", "788.15", "-v", "0.984", "-f", '30']
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("-460.884947   0.180092   -460.642788   0.204516   0.204169   -460.847303   "
                                "-460.846956" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempVibConc(self):
        test_input = [TEST_LOG1, "-t", "788.15", "-v", "0.984", "-c", "1"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("-230.257454   0.084552   -230.144250   0.112457   0.112093   -230.256708   "
                                "-230.256343" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempRangeVib(self):
        test_input = [TEST_LOG1, "-t", "788.15", "-v", "0.984", "--ti", "688.15,888.15,25"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("688.0              -230.149811   0.102064   0.101784   -230.251875   "
                                "-230.251595" in output)
                self.assertTrue("788.0              -230.144259   0.122832   0.122467   -230.267091   "
                                "-230.266726" in output)
                self.assertTrue("888.0              -230.138341   0.144694   0.144240   -230.283035   "
                                "-230.282581" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempRangeVibConc(self):
        test_input = [TEST_LOG1, "-t", "788.15", "-v", "0.984", "-c", "1", "--ti", "688.15,888.15,25"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("688.0              -230.149811   0.093276   0.092996   -230.243087   "
                                "-230.242807" in output)
                self.assertTrue("788.0              -230.144259   0.112428   0.112063   -230.256687   "
                                "-230.256322" in output)
                self.assertTrue("888.0              -230.138341   0.132634   0.132179   -230.270975   "
                                "-230.270521" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempRangeVibQ(self):
        test_input = [TEST_LOG1, "-t", "788.15", "-v", "0.984", "--ti", "688.15,888.15,25", "-q"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("688.0              -230.149811   -230.150105   0.102064   0.101784   -230.251875   "
                                "-230.251889" in output)
                self.assertTrue("788.0              -230.144259   -230.144593   0.122832   0.122467   -230.267091   "
                                "-230.267060" in output)
                self.assertTrue("888.0              -230.138341   -230.138717   0.144694   0.144240   -230.283035   "
                                "-230.282956" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempRangeVibConcQ(self):
        test_input = [TEST_LOG1, "-t", "788.15", "-v", "0.984", "-c", "1", "--ti", "688.15,888.15,25", "-q"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("688.0              -230.149811   -230.150105   0.093276   0.092996   -230.243087   "
                                "-230.243101" in output)
                self.assertTrue("788.0              -230.144259   -230.144593   0.112428   0.112063   -230.256687   "
                                "-230.256657" in output)
                self.assertTrue("888.0              -230.138341   -230.138717   0.132634   0.132179   -230.270975   "
                                "-230.270896" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass

    def testTempRangeVibConcQAltInput(self):
        test_input = [TEST_LOG2, "-t", "788.15", "-v", "0.984", "-c", "1", "--ti", "688.15,888.15,25", "-q"]
        try:
            # main(test_input)
            with capture_stdout(main, test_input) as output:
                self.assertTrue("688.0              -839.735142   -839.741153   0.211931   0.200195   -839.947074   "
                                "-839.941348" in output)
                self.assertTrue("788.0              -839.717116   -839.723992   0.261659   0.247292   -839.978776   "
                                "-839.971284" in output)
                self.assertTrue("888.0              -839.698030   -839.705771   0.314768   0.297659   -840.012798   "
                                "-840.003430" in output)
        finally:
            silent_remove(GOODVIBES_DAT, disable=DISABLE_REMOVE)
            pass
