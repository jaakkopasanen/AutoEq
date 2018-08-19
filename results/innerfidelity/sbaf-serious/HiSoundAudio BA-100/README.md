# HiSoundAudio BA-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 3.6; 22 3.5; 23 3.5; 25 3.4; 26 3.4; 28 3.3; 30 3.2; 32 3.2; 35 3.0; 37 3.0; 40 2.9; 42 2.8; 45 2.6; 49 2.4; 52 2.3; 56 2.1; 59 1.9; 64 1.6; 68 1.4; 73 1.2; 78 0.9; 83 0.6; 89 0.3; 95 -0.0; 102 -0.3; 109 -0.4; 117 -0.6; 125 -0.9; 134 -1.1; 143 -1.3; 153 -1.5; 164 -1.6; 175 -1.7; 188 -1.7; 201 -1.9; 215 -1.9; 230 -1.8; 246 -1.8; 263 -1.9; 282 -1.7; 301 -1.7; 323 -1.6; 345 -1.4; 369 -1.4; 395 -1.2; 423 -1.0; 452 -0.8; 484 -0.8; 518 -0.6; 554 -0.3; 593 0.1; 635 0.2; 679 0.1; 726 0.3; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.9; 1751 -1.8; 1873 -1.3; 2004 -0.2; 2145 1.4; 2295 2.9; 2455 4.0; 2627 4.0; 2811 3.0; 3008 1.4; 3219 -0.3; 3444 -0.5; 3685 0.4; 3943 0.7; 4219 -0.6; 4514 -2.2; 4830 -3.4; 5168 -2.6; 5530 -0.1; 5917 3.0; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.163783347819043dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio BA-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.02 | 3.8 dB  |
| Peaking | 1701 Hz | 2.51 | -2.5 dB |
| Peaking | 2502 Hz | 3.67 | 5.0 dB  |
| Peaking | 4951 Hz | 4.79 | -4.4 dB |
| Peaking | 6378 Hz | 5.14 | 5.8 dB  |
| Peaking | 63 Hz   | 1.5  | 1.2 dB  |
| Peaking | 224 Hz  | 0.63 | -2.0 dB |
| Peaking | 611 Hz  | 4.2  | 0.5 dB  |
| Peaking | 818 Hz  | 2.51 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20BA-100/HiSoundAudio%20BA-100.png)