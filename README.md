# IPCA
Image Principal Component Analysis (IPCA) is an image encoder/decoder based on Principal Component Analysis.

## RGB to YUV

- IPCA performs an PCA on all pixels to decorelate the 3 channels, producing a YUV signal.
- The transformation matrix (orthonormal) is stored on the disk


## Compression

For each channel of the YUV :
- IPCA performs an PCA on all blocks (composed of NxN pixel)
- For each block, an quantization is performed on its corresponding weights (in the new basis of NxN vectors of size NxN)
- Each quantized weight is encoded using huffman code
- The huffman table and the new basis is saved on the disk


## Uncompressing the image

- The huffman table and the new basis is retrived from the disk
- Huffman decoding
- Each block is decoded using the loaded basis
- The YUV -> RGB transform matrix is retrived from the disk
- Each pixels is converted back to RGB using 