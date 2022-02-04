# PendulumSim_mujoco

## 概要
mujoco上で振り子のシミュレーションを行うスクリプトです．  
振り子の同期現象のシミュレーションのために作成しました．

<img src="img/pendulum_2.png" width=500>

カートとスライダーの位置と速度をcsvファイルに出力します．
(mujoco上でレンダリングも行います)

リアルタイムで振り子の位置を出力するスクリプトは未完成です．(plot_realtime.py)

## Usage
```
python3 pendulum_sim.py --xmlfile pendulum_2 --exportcsv result_pendulum2 --timestep 10000 --duration 10
```
`--xmlfile`は読み込むxmlファイル名, `--exportcsv`は出力されるcsvファイルの名前，`--timestep`はmujoco上のシミュレーション時間(1timestepが0.02秒です．), `--duration`はcsvファイルに出力するタイムステップの間隔を指定します．

