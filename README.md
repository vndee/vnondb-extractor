# VNOnDB_extractor
Converting VNOnDB inkml file format to image (.png) and grouth truth text.

Converted dataset can be download [here](https://github.com/vndee/vnondb-extractor/releases).

## What is VNOnDB?
HANDS-VNOnDB (VNOnDB in short) provides 1,146 Vietnamese paragraphs of handwritten text composed of 7,296 lines, more than 480,000 strokes and more than 380,000 characters written by 200 Vietnamese. Writers were asked to write freely ground-truth text from a corpus of Vietnamese text. Our ground-truth text is derived from the VieTreeBank corpus, which contains all of the Vietnamese characters and some special symbols since it bases on Vietnamese newspapers. 

More at: [ICFHR2018-VOHTR-VNOnDB](https://sites.google.com/view/icfhr2018-vohtr-vnondb/database-tools?authuser=0)

## Usage:
```bash
pip install -r requirements.txt
python InkData_word.py
python InkData_line.py
python InkData_paragraph.py
```
All data after extracting will be stored in `InkData_word_processed`, `InkData_line_processed` and `InkData_paragraph_processed` folder. Sample output:
<p align="center"> 
<img src="example.png">
</p>
