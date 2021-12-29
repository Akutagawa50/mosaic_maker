# mosaic_make
## リポジトリの概要
[cv_camera](https://github.com/OTL/cv_camera)からウェブカメラの画像データを取得して，人の顔が含まれていたらモザイクをかけるプログラム．

## 動作環境
以下の環境を前提として開発した
* Raspberry Pi 4 Model B / 8GB
* Ubuntu 20.04

## 使用したもの
* ROS Noetic Ninjemys
* OpenCv 4.2.0

## デモンストレーション
[<img src="https://lh3.googleusercontent.com/pw/ACtC-3ePeztCp1Rhk5ELwn2uJw6yJFkEdXPWuuMA26i3K6W-rENSu8EGw4kaHwKMX1ypo1i5SPPbFyySkEHQBycQImRa5hkWmY7bxcfdVlonHQ7B0JLISx4h4oy4fonmdJyahF9LK3_D0LpiJ4suvwbqa7Dd=w1306-h979-no?authuser=2">](https://youtu.be/BlISqbMTJes)
https://youtu.be/BlISqbMTJes


## インストール方法
### 前提条件
* ROS NorticがRaspberry Pi にあらかじめインストールされていること\
インストール方法は[Ryuichi Ueda](https://github.com/ryuichiueda)氏の[ros_setup_scripts_Ubuntu20.04_server](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server/blob/master/step1.bash)からインストールできる
* 同じくRyuichi Ueda氏の[ロボットシステム学第10回（ROS）](https://www.youtube.com/watch?v=PL85Pw_zQH0)に従って，cv_cameraとweb_video_serverが動作する環境を整えてあること
* OpenCVを使うことができる環境であること

### インストール
1. `$ ls ~/catkin_ws/src`でディレクトリを移動する
2. `$ git clone https://github.com/Akutagawa50/2020_robosys.git`でリポジトリを複製する
3. `$ sudo chmod +x ./2020_robosys/scripts/mosaic.py `で実行権限を与える
4. `$ find / 2>/dev/null | grep haarcascade_frontalface_default.xml `で haarcascade_frontalface_default.xml のあるディレクトリを探してコピーしておく
5. `$ vi 2020_robosys/scripts/mosaic.py `でテキストエディタを開いて，20行目のcascade_pathに 4. でコピーしたパスを代入して保存しておく
6. これでインストール完了

## 使用方法
1. `$ roscore &`でroscoreをバックグラウンド立ち上げる
2. `$ rosrun cv_camera cv_camera_node &`でcv_cameraをバックグラウンドで実行する
3. `$ rosrun web_video_server web_video_server &`でweb_camera_serverをバックグラウンドで実行する
4. `$ rosrun 2020_robosys mosaic.py`でmosaic.pyを実行する
5. 同じネットワーク内にある端末のウェブブラウザで`{ラズベリーパイのIPアドレス}:8080`にアクセスして`/mosaic_face`をクリックするとカメラに写っている映像が見える
6. カメラに人の顔を映すとモザイクをかけて画面に出力される

## ライセンス
このリポジトリはBSD-2-Clause Licenseを付与している．
詳しくは[LICENSE](https://github.com/Akutagawa50/2020_robosys/blob/main/LICENSE)で確認できる．

## 参考文献
[1] [ロボットシステム学第10回（ROS）](https://www.youtube.com/watch?v=PL85Pw_zQH0)\
[2] [ROSで画像処理ができるようになるまで[python編]](https://qiita.com/wakaba130/items/d3a041164c316a9e7a97)\
[3] [Python, OpenCVで画像にモザイク処理（全面、一部、顔など）](https://note.nkmk.me/python-opencv-mosaic/)
