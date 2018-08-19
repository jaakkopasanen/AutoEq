# HiSoundAudio Wooduo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -14.3; 22 -14.3; 23 -14.3; 25 -14.3; 26 -14.3; 28 -14.2; 30 -14.2; 32 -14.2; 35 -14.1; 37 -14.1; 40 -14.0; 42 -14.0; 45 -14.0; 49 -13.9; 52 -13.9; 56 -13.9; 59 -13.9; 64 -13.8; 68 -13.8; 73 -13.9; 78 -13.9; 83 -13.9; 89 -13.9; 95 -13.9; 102 -13.8; 109 -13.6; 117 -13.4; 125 -13.3; 134 -13.0; 143 -12.8; 153 -12.6; 164 -12.4; 175 -12.0; 188 -11.6; 201 -11.3; 215 -10.8; 230 -10.3; 246 -9.9; 263 -9.5; 282 -8.9; 301 -8.5; 323 -7.9; 345 -7.3; 369 -6.8; 395 -6.3; 423 -5.5; 452 -5.0; 484 -4.6; 518 -4.1; 554 -3.4; 593 -2.7; 635 -2.2; 679 -1.7; 726 -1.4; 777 -1.7; 832 -0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 0.0; 1167 -0.1; 1248 -0.1; 1336 -0.4; 1429 -0.7; 1529 -1.0; 1636 -1.2; 1751 -1.2; 1873 -1.1; 2004 -1.1; 2145 -1.1; 2295 -1.1; 2455 -0.9; 2627 -0.7; 2811 -0.7; 3008 -0.5; 3219 -0.5; 3444 -0.4; 3685 -0.8; 3943 -1.5; 4219 -3.3; 4514 -5.0; 4830 -6.2; 5168 -7.6; 5530 -9.8; 5917 -8.9; 6331 -4.8; 6775 -1.3; 7249 0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.0; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.8978499088585249dB` and instead set Global volume in the UI for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Wooduo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.36 | -12.7 dB |
| Peaking | 107 Hz  | 0.28 | -12.0 dB |
| Peaking | 211 Hz  | 1.13 | -0.7 dB  |
| Peaking | 854 Hz  | 1.52 | 2.3 dB   |
| Peaking | 5467 Hz | 3.62 | -10.3 dB |
| Peaking | 1245 Hz | 2.11 | 0.9 dB   |
| Peaking | 1698 Hz | 1.17 | -1.1 dB  |
| Peaking | 3566 Hz | 2.84 | 0.9 dB   |
| Peaking | 4416 Hz | 6.17 | -1.9 dB  |
| Peaking | 7330 Hz | 6.32 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Wooduo/HiSoundAudio%20Wooduo.png)