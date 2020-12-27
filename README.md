# 2020_robosys
[cv_camera](https://github.com/OTL/cv_camera)からウェブカメラの画像データを取得して，人の顔が含まれていたらモザイクをかけるプログラム．
# 動作環境
以下の環境を前提として開発した
* Raspberry Pi 4 Model B / 8GB
* Ubuntu 20.04
* ROS Noetic Ninjemys

# 前提条件
* ROS Norticがあらかじめインストールされていること\
インストール方法はRyuichi Ueda氏の[ros_setup_scripts_Ubuntu20.04_server](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server/blob/master/step1.bash)からインストールできる
* 同じくRyuichi Ueda氏の[ロボットシステム学第10回（ROS）](https://www.youtube.com/watch?v=PL85Pw_zQH0)に従って，cv_cameraとweb_video_serverが動作する環境を整えてあること

# インストール方法
1. `$ ls ~/catkin_ws/src`でディレクトリを移動する
2. `$ git clone https://github.com/Akutagawa50/2020_robosys.git`でリポジトリを複製する
3. `$ sudo chmod +x ./2020_robosys/scripts/mosaic.py `で実行権限を与える
4. `$ roscore &`でroscoreを立ち上げる
5. `$ rosrun cv_camera cv_camera_node &`でcv_cameraをバックグラウンドで実行する
6. `$ rosrun web_video_server web_video_server &`でweb_camera_serverをバックグラウンドで実行する
7. `$ rosrun 2020_robosys mosaic.py`でmosaic.pyを実行する
8. 同じネットワーク内にある端末のウェブブラウザで`{ラズベリーパイのIPアドレス}:8080`にアクセスして`/mosaic_face`をクリックすると見ることができる

# デモンストレーション
https://www.youtube.com/embed/BlISqbMTJe

# 参考文献
[1] [ロボットシステム学第10回（ROS）](https://www.youtube.com/watch?v=PL85Pw_zQH0)\
[2] [ROSで画像処理ができるようになるまで[python編]](https://qiita.com/wakaba130/items/d3a041164c316a9e7a97)\
[3] [Python, OpenCVで画像にモザイク処理（全面、一部、顔など）](https://note.nkmk.me/python-opencv-mosaic/)

# ライセンス

