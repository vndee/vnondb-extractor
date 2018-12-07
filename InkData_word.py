""" Duy Huynh 2018 @ MIT License   
    VNOnDB2018 dataset extractor tool
"""

import sys, os, argparse
import xml.etree.ElementTree as ET
import numpy as np
from skimage.draw import line
from skimage.io import imread, imsave
import scipy.ndimage as ndimage
import pickle
import matplotlib.pyplot as plt
import glob
import warnings
warnings.filterwarnings('ignore')

dataFolder = "InkData_word"
targetFolder = dataFolder + "_processed"
lineWidth = 0.5

def get_traces_data(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    firstAnnotationXML = []

    trace_all = []
    label = []

    for child in root:
        if child.tag == 'annotationXML':
            firstAnnotationXML.append(child)
            continue 

        trace_group = []

        for tr_id in child:
            if tr_id.tag == 'annotationXML':
                label.append({'id': child.get('id'), 'gt': tr_id[0].text})
                continue

            trace_line = []
            txt = (tr_id.text).replace('\n', '').split(',')

            for ch in txt:
                temp = ch.split(' ')
                trace_line.append([round(float(temp[0])), round(float(temp[1]))])
                    
            trace_group.append({'id': tr_id.get('id'), 'coords': trace_line})

        trace_all.append({'id': child.get('id'), 'trace': trace_group})

    return trace_all, label

def makeLabelingImage(input_path, output_base_path):
    traces, ground_truth = get_traces_data(input_path)
    
    output_base_path = targetFolder + '/' + output_base_path
    
    for line in ground_truth:
        outFile = open(output_base_path + '_' + str(line['id']) + '.txt', 'w+')
        outFile.write(str(line['gt']))
        outFile.close()

    for trace_group in traces:
        plt.gca().invert_yaxis()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.axes().spines['top'].set_visible(False)
        plt.axes().spines['right'].set_visible(False)
        plt.axes().spines['bottom'].set_visible(False)
        plt.axes().spines['left'].set_visible(False)

        for trace_line in trace_group['trace']:
            ls = trace_line['coords']
            data = np.array(ls)
            x, y = zip(*data)
            plt.plot(x, y, linewidth=lineWidth, c='black')

        plt.savefig(output_base_path + '_' + trace_group['id'] + '.png', bbox_inches='tight', dpi=100)
        plt.gcf().clear()

if __name__ == '__main__':
    if not os.path.exists(targetFolder): 
        os.mkdir(targetFolder)

    listFile = glob.glob(dataFolder + '/*')
    numberOfFile = len(listFile)
    cnt = 0

    for fileData in listFile:
        cnt = cnt + 1
        print('Processing', end=' ')
        print(cnt, end='')
        print('/', end='')
        print(numberOfFile)
        fileName = fileData.split('/')[1]
        makeLabelingImage(fileData, fileName.split('.')[0])
