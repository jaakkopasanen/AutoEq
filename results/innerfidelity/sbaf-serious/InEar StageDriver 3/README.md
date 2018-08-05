# InEar StageDriver 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.5; 23 -1.6; 25 -1.6; 26 -1.7; 28 -1.7; 30 -1.8; 32 -1.8; 35 -1.9; 37 -1.9; 40 -1.9; 42 -1.9; 45 -2.0; 49 -2.1; 52 -2.1; 56 -2.2; 59 -2.2; 64 -2.3; 68 -2.3; 73 -2.5; 78 -2.7; 83 -2.9; 89 -3.3; 95 -3.8; 102 -4.4; 109 -4.8; 117 -5.3; 125 -5.9; 134 -6.4; 143 -6.8; 153 -6.9; 164 -7.0; 175 -7.0; 188 -6.9; 201 -6.9; 215 -6.7; 230 -6.5; 246 -6.2; 263 -6.0; 282 -5.6; 301 -5.3; 323 -4.9; 345 -4.5; 369 -4.0; 395 -3.6; 423 -3.0; 452 -2.5; 484 -2.2; 518 -1.8; 554 -1.3; 593 -0.8; 635 -0.5; 679 -0.3; 726 -0.0; 777 0.3; 832 0.4; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.6; 1636 -3.2; 1751 -3.8; 1873 -4.2; 2004 -4.5; 2145 -4.7; 2295 -4.0; 2455 -2.0; 2627 0.2; 2811 2.3; 3008 4.6; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.4; 5168 2.9; 5530 4.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDriver 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.71 | -1.4 dB |
| Peaking | 184 Hz  | 0.72 | -7.3 dB |
| Peaking | 2116 Hz | 1.99 | -7.6 dB |
| Peaking | 3540 Hz | 1.33 | 7.9 dB  |
| Peaking | 6103 Hz | 5.31 | 4.4 dB  |
| Peaking | 360 Hz  | 2.45 | -0.9 dB |
| Peaking | 803 Hz  | 1.53 | 1.3 dB  |
| Peaking | 1543 Hz | 4.59 | -1.0 dB |
| Peaking | 6742 Hz | 7.07 | 1.5 dB  |
| Peaking | 7971 Hz | 2.37 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/InEar%20StageDriver%203/InEar%20StageDriver%203.png)