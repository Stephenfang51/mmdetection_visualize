# mmdetection_visualize_v1

It's a very simple version for visualizing the training result produced by mmdetection

The program supports drawing six curves including the following

  1. loss_rpn_bbox
  2. loss_rpn_cls
  3. loss_bbox
  4. loss_cls
  5. loss
  6. acc
  
  
### Installation

1. Clone it  
`git clone https://github.com/Stephenfang51/mmdetection_visualize`

  There will be total 3 files(json directory, output directory, visualize.py)

### How to use

1. After training finished, you will have **work_dir** directory in your mmdetection directory
2. take the latest json file and put into json directory in mmditection_visualize directory
3. command `python visualize.py json/xxxxxxxlog.json` in terminal
4. check the output directory, Done !


<img src="https://github.com/Stephenfang51/mmdetection_visualize/blob/master/example/20190808_041204.log.json_result.png?raw=true">
