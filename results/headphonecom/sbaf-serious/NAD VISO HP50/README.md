# NAD VISO HP50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -6.5; 22 -6.4; 23 -6.4; 25 -6.3; 26 -6.3; 28 -6.2; 30 -6.1; 32 -6.0; 35 -5.8; 37 -5.7; 40 -5.6; 42 -5.5; 45 -5.3; 49 -5.1; 52 -4.9; 56 -4.7; 59 -4.5; 64 -4.2; 68 -4.0; 73 -3.7; 78 -3.4; 83 -3.3; 89 -2.9; 95 -2.7; 102 -2.6; 109 -2.7; 117 -3.4; 125 -5.0; 134 -6.3; 143 -6.5; 153 -5.9; 164 -4.9; 175 -4.6; 188 -5.6; 201 -5.8; 215 -5.6; 230 -5.2; 246 -4.8; 263 -4.4; 282 -3.8; 301 -3.2; 323 -2.4; 345 -1.9; 369 -2.2; 395 -1.8; 423 -1.4; 452 -1.3; 484 -1.3; 518 -1.1; 554 -0.7; 593 -0.3; 635 -0.1; 679 -0.1; 726 -0.1; 777 -0.4; 832 -0.8; 890 -0.8; 952 -0.5; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.7; 1336 -2.7; 1429 -3.4; 1529 -3.8; 1636 -3.7; 1751 -3.3; 1873 -2.1; 2004 -1.7; 2145 -1.0; 2295 -0.1; 2455 0.9; 2627 1.7; 2811 2.6; 3008 2.9; 3219 2.7; 3444 2.3; 3685 1.7; 3943 1.0; 4219 -1.0; 4514 -2.6; 4830 -2.7; 5168 -0.2; 5530 2.0; 5917 2.6; 6331 3.3; 6775 2.8; 7249 1.3; 7756 0.2; 8299 -1.1; 8880 -1.8; 9502 -1.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.8  | -3.9 dB |
| Peaking | 22 Hz   | 0.97 | -5.0 dB |
| Peaking | 138 Hz  | 4    | -3.9 dB |
| Peaking | 220 Hz  | 1.35 | -5.0 dB |
| Peaking | 1558 Hz | 3.62 | -4.3 dB |
| Peaking | 2083 Hz | 2.11 | -2.0 dB |
| Peaking | 3011 Hz | 1.55 | 3.7 dB  |
| Peaking | 4676 Hz | 4.05 | -5.4 dB |
| Peaking | 6151 Hz | 2.21 | 3.9 dB  |
| Peaking | 8697 Hz | 3.73 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)