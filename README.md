# AsciiArt Project

AsciiArt Project, given an image, converts that image with some Ascii characters.
At moment (2022.12.07) those characters are fixed and are:
'@', '#', '|', '$', '.', '_', ' ', '-'

Optionally, in ascii_art_mod, the result could be saved in a file.


## How to use the ascii_art_mod script
___
This script needs at least 2 parameters:

| Parameters | Required | Functionality | Default Value |
| ---------- | -------- | ------------- | ------------- |
| image_path | True     | path where is the image's file | - |
| image_name | True     | name of image's file | - |
| image_type | False    | type of image's file | jpg |
| scale_factor | False    | reduce the image's dimension on this factor | 4 |
| save_result | False    | True if the result must be saved in file | True |
| save_path | False    | path where the ascii file will be saved. If it will not declare, the ascii file will be saved in same script's folder | None |

With these parameters, it's possible to customize the behaviour of the script