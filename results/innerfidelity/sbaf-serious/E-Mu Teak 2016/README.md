# E-Mu Teak 2016

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 -1.5; 22 -2.0; 23 -2.2; 25 -2.6; 26 -2.8; 28 -3.0; 30 -3.2; 32 -3.4; 35 -3.5; 37 -3.5; 40 -3.6; 42 -3.6; 45 -3.6; 49 -3.6; 52 -3.6; 56 -3.5; 59 -3.4; 64 -3.2; 68 -3.0; 73 -2.8; 78 -2.9; 83 -3.2; 89 -3.4; 95 -3.5; 102 -3.7; 109 -3.9; 117 -4.1; 125 -4.4; 134 -4.5; 143 -4.6; 153 -4.6; 164 -4.3; 175 -4.2; 188 -4.1; 201 -3.9; 215 -3.6; 230 -3.2; 246 -2.9; 263 -2.5; 282 -2.1; 301 -1.9; 323 -1.7; 345 -1.6; 369 -1.3; 395 -1.0; 423 -0.6; 452 -0.4; 484 -0.3; 518 -0.2; 554 0.1; 593 0.3; 635 0.2; 679 -0.1; 726 -0.2; 777 -0.2; 832 -0.2; 890 0.3; 952 0.2; 1019 -0.0; 1090 0.1; 1167 0.3; 1248 0.4; 1336 0.5; 1429 0.3; 1529 0.2; 1636 0.3; 1751 0.6; 1873 0.9; 2004 1.4; 2145 1.8; 2295 2.2; 2455 2.8; 2627 3.2; 2811 3.2; 3008 3.7; 3219 3.8; 3444 3.0; 3685 2.7; 3943 2.5; 4219 2.4; 4514 1.7; 4830 0.9; 5168 0.7; 5530 1.1; 5917 1.3; 6331 1.9; 6775 2.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -0.9; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.5dB` and instead set Global volume in the UI for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak 2016 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 3 Hz     | 1.5  | -0.8 dB |
| Peaking | 39 Hz    | 0.69 | -3.3 dB |
| Peaking | 157 Hz   | 0.87 | -4.2 dB |
| Peaking | 3046 Hz  | 1.52 | 3.8 dB  |
| Peaking | 6690 Hz  | 6.5  | 2.3 dB  |
| Peaking | 572 Hz   | 4    | 0.7 dB  |
| Peaking | 1611 Hz  | 7.31 | -0.5 dB |
| Peaking | 10769 Hz | 4.5  | 0.3 dB  |
| Peaking | 9907 Hz  | 5.55 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%202016/E-Mu%20Teak%202016.png)