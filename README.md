# Wavetable Oscillator &amp; Step Sequence Sampler

**需要用到的库：**

> pyaudio numpy pygame

**安装：**

``` bash
pip install pyaudio numpy pygame
```

## Wavetable Oscillator

### wtOsc 模块： (Wavetable Oscillator)

> 使用 pyaudio 模块、 struct 模块、 numpy 模块、 time 模块。

1. **init(sample, tempo, division) 函数：**

**初始化：*在使用该模块前必须初始化***

- sample 是需要读入的存储一个周期的 wav 文件的路径；
- tempo(bpm) 是曲速，以 bpm 为单位；
- division 是一个数组，以 \[beats, steps\] 的形式输入。

**Example:**
``` python
wtOsc.init('Shapes/HQ/HQ_Saw.wav', 120, [4, 4])
```

2. **playKey(key, volume, steps) 函数：**

- key 是键名；
- volume 是音量，通常设置为 0 ~ 1 之间的浮点数；
- steps 是步长，例如之前设置 division(\[beats, steps\]) 为 \[4, 4\] ，即 4 steps 每 beat ，如果一个 beat 为一个四分音符，那 4 steps 为一个 beat ，一个 step 为一个十六分音符。

**Example:**
``` python
wtOsc.playKey('C5', 0.5, 4) #: 键名： 'C5' ，音量： 0.5 ，步长： 4 （相当于一个四分音符）。
```

3. **delay(steps) 函数：**

- 原本这个函数是为了代替休止符使用的。
- 但是这个函数目前还有点 Bug ，修复中。


## Step Sequence Sampler

### sSSampler 模块： (Step Sequence Sampler)

> 使用 pygame 模块、 time 模块。

1. **init(path, tempo, division) 函数：**

**初始化：*在使用该模块前必须初始化***

- path 为装有采样 wav 文件的目录；
- tempo, division 同 wtOsc 模块的 init() 的使用方法一样。

**Example:**
``` python
sSSampler.init('Samples/Drums/default', 120, [4,4])
```

2. **playKeys(\*k) 函数：**

- 输入的是一个你想在当前步数播放的采样的序列。

**Example:**
``` python
sSSampler.playKeys('Kick', 'Snare') #: 这个时候同时播放 'Kick' 和 'Snare' 的采样。
```

3. **releaseKeys() 函数：**

- 此时停止播放所有采样。

## 内置的歌曲：

> default-song.py

1. 打开这个 python 脚本会播放一段《おてんば恋娘》。
