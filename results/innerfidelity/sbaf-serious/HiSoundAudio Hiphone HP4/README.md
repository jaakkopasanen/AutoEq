# HiSoundAudio Hiphone HP4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -9.9; 22 -9.9; 23 -10.0; 25 -10.0; 26 -10.0; 28 -10.0; 30 -10.0; 32 -10.0; 35 -10.0; 37 -9.9; 40 -9.9; 42 -9.9; 45 -9.8; 49 -9.7; 52 -9.7; 56 -9.6; 59 -9.5; 64 -9.5; 68 -9.4; 73 -9.4; 78 -9.4; 83 -9.5; 89 -9.7; 95 -10.0; 102 -10.3; 109 -10.6; 117 -10.9; 125 -11.2; 134 -11.4; 143 -11.4; 153 -11.4; 164 -11.2; 175 -10.9; 188 -10.6; 201 -10.2; 215 -9.9; 230 -9.4; 246 -9.0; 263 -8.6; 282 -8.0; 301 -7.6; 323 -7.1; 345 -6.5; 369 -6.1; 395 -5.5; 423 -4.9; 452 -4.4; 484 -3.9; 518 -3.5; 554 -2.8; 593 -2.2; 635 -1.7; 679 -1.3; 726 -0.8; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.4; 1336 0.5; 1429 0.8; 1529 1.2; 1636 1.5; 1751 1.8; 1873 2.3; 2004 2.7; 2145 1.9; 2295 0.9; 2455 1.8; 2627 2.9; 2811 3.7; 3008 5.1; 3219 5.7; 3444 6.0; 3685 5.9; 3943 5.1; 4219 3.4; 4514 2.0; 4830 1.4; 5168 1.0; 5530 -0.1; 5917 -2.0; 6331 -4.7; 6775 -4.0; 7249 -1.6; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.6; 17469 -1.5; 18692 -0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Hiphone HP4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.44 | -9.0 dB  |
| Peaking | 170 Hz   | 0.45 | -10.3 dB |
| Peaking | 1195 Hz  | 0.4  | 1.7 dB   |
| Peaking | 3485 Hz  | 2.31 | 5.8 dB   |
| Peaking | 6453 Hz  | 5.3  | -5.9 dB  |
| Peaking | 784 Hz   | 3.62 | 0.7 dB   |
| Peaking | 1242 Hz  | 1.5  | -0.6 dB  |
| Peaking | 2094 Hz  | 2.7  | 1.9 dB   |
| Peaking | 2295 Hz  | 6.12 | -2.6 dB  |
| Peaking | 17352 Hz | 4.91 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Hiphone%20HP4/HiSoundAudio%20Hiphone%20HP4.png)