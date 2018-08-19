# Yuin G2A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.4; 49 4.6; 52 4.1; 56 3.4; 59 3.0; 64 2.3; 68 1.8; 73 1.5; 78 1.3; 83 0.8; 89 0.2; 95 -0.2; 102 -0.5; 109 -0.9; 117 -1.1; 125 -1.5; 134 -1.8; 143 -2.0; 153 -2.1; 164 -2.2; 175 -2.1; 188 -2.1; 201 -1.9; 215 -1.9; 230 -1.9; 246 -1.7; 263 -1.8; 282 -1.8; 301 -1.5; 323 -1.3; 345 -1.2; 369 -1.1; 395 -0.8; 423 -0.7; 452 -0.6; 484 -0.3; 518 -0.2; 554 -0.1; 593 0.1; 635 0.3; 679 0.3; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.5; 1336 -1.0; 1429 -1.5; 1529 -1.9; 1636 -2.7; 1751 -3.4; 1873 -4.1; 2004 -4.6; 2145 -4.6; 2295 -4.3; 2455 -3.2; 2627 -1.6; 2811 0.4; 3008 2.5; 3219 4.4; 3444 5.9; 3685 5.4; 3943 2.1; 4219 -2.7; 4514 -6.3; 4830 -6.4; 5168 -4.6; 5530 -1.0; 5917 4.0; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.6; 8299 -4.4; 8880 -5.9; 9502 -6.0; 10167 -3.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.140816982051657dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G2A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.15 | 7.1 dB   |
| Peaking | 2276 Hz  | 1.1  | -13.7 dB |
| Peaking | 3653 Hz  | 0.7  | 16.1 dB  |
| Peaking | 4648 Hz  | 3.56 | -17.8 dB |
| Peaking | 9070 Hz  | 3.08 | -10.3 dB |
| Peaking | 55 Hz    | 1.66 | 1.6 dB   |
| Peaking | 174 Hz   | 0.81 | -2.5 dB  |
| Peaking | 5358 Hz  | 9.01 | -3.6 dB  |
| Peaking | 6256 Hz  | 6.03 | 4.5 dB   |
| Peaking | 21989 Hz | 0.1  | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G2A/Yuin%20G2A.png)