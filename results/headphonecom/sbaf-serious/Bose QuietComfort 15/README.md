# Bose QuietComfort 15

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -5.6; 22 -8.1; 23 -9.0; 25 -10.3; 26 -10.6; 28 -10.8; 30 -10.3; 32 -9.6; 35 -8.5; 37 -7.9; 40 -7.4; 42 -7.1; 45 -6.9; 49 -6.6; 52 -6.4; 56 -6.2; 59 -6.0; 64 -6.0; 68 -6.1; 73 -6.2; 78 -6.3; 83 -6.2; 89 -6.2; 95 -6.2; 102 -6.1; 109 -5.9; 117 -5.8; 125 -5.7; 134 -5.7; 143 -5.5; 153 -5.4; 164 -5.1; 175 -5.0; 188 -4.9; 201 -4.7; 215 -4.6; 230 -4.4; 246 -4.4; 263 -4.3; 282 -4.1; 301 -3.8; 323 -3.6; 345 -3.2; 369 -2.9; 395 -2.6; 423 -2.2; 452 -2.0; 484 -1.8; 518 -1.7; 554 -1.2; 593 -0.8; 635 -0.2; 679 -0.2; 726 -0.0; 777 0.5; 832 0.8; 890 0.7; 952 0.4; 1019 -0.0; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -1.9; 1429 -2.0; 1529 -2.1; 1636 -3.4; 1751 -5.0; 1873 -6.6; 2004 -8.3; 2145 -9.6; 2295 -9.7; 2455 -9.3; 2627 -8.0; 2811 -6.1; 3008 -3.7; 3219 -2.4; 3444 -3.1; 3685 -3.5; 3943 -6.6; 4219 -9.6; 4514 -9.6; 4830 -6.5; 5168 -4.1; 5530 -3.7; 5917 -7.5; 6331 -3.8; 6775 -2.2; 7249 -1.5; 7756 0.3; 8299 -0.3; 8880 -3.0; 9502 -5.8; 10167 -6.6; 10879 -5.1; 11640 -2.9; 12455 -1.4; 13327 -0.9; 14260 -1.2; 15258 -1.6; 16326 -2.2; 17469 -3.7; 18692 -5.9; 20000 -8.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.23 | -9.0 dB  |
| Peaking | 115 Hz   | 0.41 | -5.6 dB  |
| Peaking | 2242 Hz  | 2.55 | -10.1 dB |
| Peaking | 4472 Hz  | 3.18 | -8.8 dB  |
| Peaking | 841 Hz   | 1.61 | 2.5 dB   |
| Peaking | 1481 Hz  | 0.2  | -0.8 dB  |
| Peaking | 3368 Hz  | 4.67 | 2.3 dB   |
| Peaking | 10191 Hz | 4.31 | -6.4 dB  |
| Peaking | 19733 Hz | 1.28 | -8.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)