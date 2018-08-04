# beyerdynamic DT 880 32ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 10 -84; 20 1.6; 22 1.0; 23 0.7; 25 0.2; 26 0.0; 28 -0.3; 30 -0.6; 32 -0.8; 35 -1.1; 37 -1.3; 40 -1.5; 42 -1.6; 45 -1.9; 49 -2.3; 52 -2.5; 56 -2.7; 59 -2.8; 64 -2.8; 68 -2.3; 73 -2.1; 78 -2.7; 83 -3.3; 89 -3.4; 95 -3.4; 102 -3.4; 109 -3.4; 117 -3.3; 125 -3.5; 134 -3.5; 143 -3.5; 153 -3.5; 164 -3.4; 175 -3.6; 188 -3.6; 201 -3.5; 215 -3.4; 230 -3.1; 246 -3.1; 263 -3.1; 282 -3.0; 301 -2.9; 323 -2.8; 345 -2.6; 369 -2.3; 395 -2.0; 423 -1.5; 452 -1.6; 484 -1.8; 518 -1.7; 554 -1.3; 593 -0.9; 635 -0.6; 679 -0.6; 726 -0.5; 777 -0.2; 832 -0.1; 890 -0.1; 952 0.1; 1019 0.0; 1090 0.4; 1167 0.5; 1248 0.9; 1336 0.8; 1429 0.5; 1529 0.0; 1636 -0.5; 1751 -0.8; 1873 -1.0; 2004 -1.4; 2145 -1.3; 2295 -0.9; 2455 -0.2; 2627 -0.0; 2811 -0.1; 3008 -0.3; 3219 -1.0; 3444 -1.5; 3685 -1.9; 3943 -1.9; 4219 -2.3; 4514 -2.5; 4830 -1.9; 5168 -2.4; 5530 -5.4; 5917 -6.9; 6331 -6.8; 6775 -5.6; 7249 -5.4; 7756 -7.2; 8299 -9.4; 8880 -10.1; 9502 -8.2; 10167 -4.1; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.6; 18692 -2.5; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.2dB` and instead set Global volume in the UI for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `beyerdynamic DT 880 32ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 106 Hz   | 0.52 | -3.1 dB |
| Peaking | 279 Hz   | 0.95 | -1.8 dB |
| Peaking | 8780 Hz  | 3.92 | -9.9 dB |
| Peaking | 6120 Hz  | 2.35 | -5.9 dB |
| Peaking | 27355 Hz | 2.22 | -7.2 dB |
| Peaking | 18 Hz    | 2.2  | 2.0 dB  |
| Peaking | 1271 Hz  | 2.8  | 1.2 dB  |
| Peaking | 1969 Hz  | 4.27 | -1.4 dB |
| Peaking | 3732 Hz  | 5.88 | -1.0 dB |
| Peaking | 11459 Hz | 4.89 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/beyerdynamic%20DT%20880%2032ohm/beyerdynamic%20DT%20880%2032ohm.png)