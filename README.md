# Image to CSV

This script exports images as a two-dimensionnal CSV, containing RGB values.

It uses:
  * **,** to separate RGB values
  * **|** to separate pixels
  * **Line feed** to separate the image vertical lines

## Usage

First, export the script in /usr/bin or somewhere else using :

```shell
sudo mv img_to_csv.py /usr/bin/img_to_csv
```

Then simply:

```shell
img_to_csv path/to/image.ext
```

The CSV will be saved as <file>.csv in the original image's folder.
