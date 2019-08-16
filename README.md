# mmdetection_visualize_v1

It's a very simple version for visualizing the training result produced by mmdetection

### Updata
> 2019.8.16 ----- PR_curve,  F_measure for VOC dataset

### Readme
The program supports drawing six training result and the most important evaluation tool:PR curve(only for VOC now)

  1. loss_rpn_bbox
  2. loss_rpn_cls
  3. loss_bbox
  4. loss_cls
  5. loss
  6. acc
  
  
  7. PR_curve
  8. F-measure
  
  
### Installation

1. Clone it  
`git clone https://github.com/Stephenfang51/mmdetection_visualize`

  There will be total 5 files(json directory, output directory, visualize.py, mean_ap_visualize.py, voc_eval_visualize.py)
  
2. 
- put `voc_eval_visualize.py` under `/mmdetection/tools/`

- put `mean_ap_visualize.py` under `mmdetection/mmdet/core/evaluation/`

### How to use

#### six training result
1. After training finished, you will have **work_dir** directory in your mmdetection directory
2. take the latest json file and put into json directory in mmditection_visualize directory
3. command `python visualize.py json/xxxxxxxlog.json` in terminal
4. check the output directory, Done !

#### PR curve and F-measure
1. make sure `voc_eval_visualize.py` and `mean_ap_visualize.py` settled down
2. command as usual like `python tools/voc_eval_visualize.py {your pkl file} {your network configs file}`
     - example `python tools/voc_eval_visualize.py result.pkl ./configs/faster_rcnn_r101_fpn_1x.py`
3. check the /mmdetection main directory, you will see the **PR_curve_each_class.png** there， Done !

<img src="https://github.com/Stephenfang51/mmdetection_visualize/blob/master/example/20190808_041204.log.json_result.png?raw=true">

<img src="https://github.com/Stephenfang51/mmdetection_visualize/blob/master/example/PR_curve_each_class.png?raw=true">



