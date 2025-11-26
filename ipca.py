import argparse
import numpy as np
from PIL import Image


class IPCAEncoder:
    def __init__(self):
        pass

class IPCADecoder:
    def __init__(self):
        pass



if __name__ == "__main__":
    # Arguments

    parser = argparse.ArgumentParser(
        prog="Image Principal Component Analysis (IPCA)",
        description="IPCA is an image encoder/decoder using principal component analysis for inter block compression."
    )

    parser.add_argument("input", help="Image to encode/decode.")
    parser.add_argument("-o", "--out",help="Encodes the input image in a file.")
    parser.add_argument("-b" "--blocksize", default=8, help="Block size in pixels. Default=8.")

