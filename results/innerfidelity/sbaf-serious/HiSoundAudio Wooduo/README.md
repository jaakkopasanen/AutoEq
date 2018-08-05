# HiSoundAudio Wooduo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -14.3; 22 -14.2; 23 -14.2; 25 -14.2; 26 -14.1; 28 -14.1; 30 -14.0; 32 -13.9; 35 -13.8; 37 -13.7; 40 -13.6; 42 -13.5; 45 -13.4; 49 -13.2; 52 -13.1; 56 -12.9; 59 -12.8; 64 -12.6; 68 -12.4; 73 -12.3; 78 -12.2; 83 -12.2; 89 -12.3; 95 -12.5; 102 -12.7; 109 -12.8; 117 -13.0; 125 -13.3; 134 -13.3; 143 -13.3; 153 -13.1; 164 -12.9; 175 -12.5; 188 -12.1; 201 -11.7; 215 -11.2; 230 -10.6; 246 -10.2; 263 -9.7; 282 -9.1; 301 -8.6; 323 -8.0; 345 -7.4; 369 -6.9; 395 -6.3; 423 -5.6; 452 -5.1; 484 -4.6; 518 -4.1; 554 -3.4; 593 -2.7; 635 -2.2; 679 -1.7; 726 -1.4; 777 -1.7; 832 -0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 0.0; 1167 -0.1; 1248 -0.1; 1336 -0.4; 1429 -0.7; 1529 -1.0; 1636 -1.2; 1751 -1.2; 1873 -1.1; 2004 -1.1; 2145 -1.1; 2295 -1.1; 2455 -0.9; 2627 -0.7; 2811 -0.7; 3008 -0.5; 3219 -0.5; 3444 -0.4; 3685 -0.8; 3943 -1.5; 4219 -3.3; 4514 -5.0; 4830 -6.2; 5168 -7.6; 5530 -9.8; 5917 -8.9; 6331 -4.8; 6775 -1.3; 7249 0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.0; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Wooduo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 1.32 | -14.0 dB |
| Peaking | 34 Hz   | 0.34 | -11.7 dB |
| Peaking | 159 Hz  | 0.74 | -8.5 dB  |
| Peaking | 328 Hz  | 1.22 | -3.1 dB  |
| Peaking | 5465 Hz | 3.6  | -10.3 dB |
| Peaking | 507 Hz  | 4.18 | -0.7 dB  |
| Peaking | 964 Hz  | 2.62 | 1.4 dB   |
| Peaking | 1853 Hz | 2.04 | -1.0 dB  |
| Peaking | 6122 Hz | 7.99 | -2.4 dB  |
| Peaking | 7251 Hz | 3.82 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Wooduo/HiSoundAudio%20Wooduo.png)