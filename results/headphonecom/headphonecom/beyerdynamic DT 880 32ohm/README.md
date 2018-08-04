# beyerdynamic DT 880 32ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 1.1; 22 0.4; 23 0.2; 25 -0.3; 26 -0.5; 28 -0.8; 30 -1.1; 32 -1.4; 35 -1.7; 37 -1.9; 40 -2.1; 42 -2.2; 45 -2.5; 49 -2.9; 52 -3.0; 56 -3.2; 59 -3.4; 64 -3.3; 68 -2.9; 73 -2.7; 78 -3.4; 83 -4.0; 89 -4.2; 95 -4.3; 102 -4.4; 109 -4.6; 117 -4.6; 125 -4.8; 134 -4.8; 143 -4.8; 153 -4.8; 164 -4.8; 175 -4.9; 188 -4.9; 201 -4.9; 215 -4.8; 230 -4.6; 246 -4.5; 263 -4.4; 282 -4.4; 301 -4.3; 323 -4.2; 345 -4.0; 369 -3.6; 395 -3.2; 423 -2.8; 452 -2.7; 484 -2.5; 518 -2.2; 554 -1.8; 593 -1.4; 635 -0.9; 679 -0.7; 726 -0.5; 777 -0.3; 832 -0.2; 890 -0.1; 952 0.0; 1019 0.0; 1090 0.5; 1167 0.8; 1248 1.5; 1336 2.2; 1429 2.7; 1529 2.7; 1636 2.6; 1751 2.2; 1873 1.9; 2004 1.6; 2145 1.7; 2295 2.1; 2455 2.8; 2627 3.0; 2811 2.9; 3008 2.3; 3219 1.3; 3444 0.6; 3685 0.2; 3943 0.5; 4219 1.3; 4514 2.3; 4830 3.6; 5168 3.0; 5530 -0.7; 5917 -3.4; 6331 -4.5; 6775 -4.2; 7249 -4.4; 7756 -6.2; 8299 -7.9; 8880 -8.2; 9502 -5.6; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `beyerdynamic DT 880 32ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 80 Hz    | 0.54 | -2.3 dB |
| Peaking | 235 Hz   | 0.5  | -4.0 dB |
| Peaking | 1895 Hz  | 0.74 | 2.9 dB  |
| Peaking | 4912 Hz  | 7.86 | 4.7 dB  |
| Peaking | 8164 Hz  | 2.27 | -8.3 dB |
| Peaking | 17 Hz    | 2.44 | 1.6 dB  |
| Peaking | 2051 Hz  | 6.59 | -1.2 dB |
| Peaking | 2701 Hz  | 5.94 | 1.3 dB  |
| Peaking | 6144 Hz  | 8.77 | -2.8 dB |
| Peaking | 10974 Hz | 5.09 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/beyerdynamic%20DT%20880%2032ohm/beyerdynamic%20DT%20880%2032ohm.png)