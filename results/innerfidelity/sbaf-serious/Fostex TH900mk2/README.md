# Fostex TH900mk2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 -2.6; 22 -2.9; 23 -3.0; 25 -3.3; 26 -3.4; 28 -3.5; 30 -3.7; 32 -3.8; 35 -3.9; 37 -4.0; 40 -4.0; 42 -4.0; 45 -4.0; 49 -4.0; 52 -3.9; 56 -3.9; 59 -3.8; 64 -3.5; 68 -3.4; 73 -3.3; 78 -3.4; 83 -3.6; 89 -3.8; 95 -3.9; 102 -4.1; 109 -4.2; 117 -4.3; 125 -4.5; 134 -4.6; 143 -4.6; 153 -4.5; 164 -4.1; 175 -3.9; 188 -3.7; 201 -3.4; 215 -3.0; 230 -2.7; 246 -2.4; 263 -2.0; 282 -1.6; 301 -1.1; 323 -0.6; 345 -0.1; 369 0.4; 395 1.0; 423 1.6; 452 2.0; 484 2.1; 518 2.1; 554 2.0; 593 1.9; 635 1.5; 679 0.7; 726 0.3; 777 1.1; 832 1.0; 890 0.3; 952 0.0; 1019 0.1; 1090 0.3; 1167 0.8; 1248 1.1; 1336 1.4; 1429 1.4; 1529 1.4; 1636 1.4; 1751 1.3; 1873 1.5; 2004 1.6; 2145 1.6; 2295 2.1; 2455 3.2; 2627 3.6; 2811 2.8; 3008 1.6; 3219 0.3; 3444 1.2; 3685 2.0; 3943 1.7; 4219 0.5; 4514 -0.6; 4830 -1.5; 5168 -2.6; 5530 -4.9; 5917 -5.9; 6331 -3.4; 6775 -1.4; 7249 -2.4; 7756 -3.7; 8299 -2.8; 8880 -0.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -1.8; 18692 -4.5; 20000 -7.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 5 Hz     | 1.37 | -2.0 dB |
| Peaking | 37 Hz    | 0.51 | -3.7 dB |
| Peaking | 158 Hz   | 0.82 | -5.0 dB |
| Peaking | 885 Hz   | 0.14 | 1.9 dB  |
| Peaking | 5901 Hz  | 2.67 | -6.3 dB |
| Peaking | 485 Hz   | 3.31 | 1.6 dB  |
| Peaking | 977 Hz   | 2.11 | -1.6 dB |
| Peaking | 2617 Hz  | 5.75 | 2.5 dB  |
| Peaking | 16434 Hz | 1.38 | 2.6 dB  |
| Peaking | 20340 Hz | 0.8  | -7.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2/Fostex%20TH900mk2.png)