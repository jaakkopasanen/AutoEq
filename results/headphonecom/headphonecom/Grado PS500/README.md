# Grado PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.7; 22 3.7; 23 3.3; 25 2.5; 26 2.1; 28 1.4; 30 0.7; 32 0.0; 35 -0.9; 37 -1.5; 40 -2.2; 42 -2.7; 45 -3.5; 49 -4.3; 52 -4.9; 56 -5.6; 59 -6.0; 64 -6.6; 68 -7.0; 73 -7.3; 78 -7.4; 83 -7.4; 89 -7.5; 95 -7.6; 102 -7.5; 109 -7.4; 117 -7.2; 125 -6.8; 134 -6.4; 143 -6.1; 153 -5.8; 164 -5.3; 175 -4.9; 188 -4.7; 201 -4.4; 215 -4.1; 230 -3.8; 246 -3.5; 263 -3.2; 282 -2.8; 301 -2.5; 323 -2.2; 345 -1.9; 369 -1.6; 395 -1.2; 423 -1.0; 452 -0.7; 484 -0.3; 518 0.0; 554 0.3; 593 0.6; 635 0.8; 679 0.8; 726 0.8; 777 0.8; 832 0.6; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.5; 1429 -0.6; 1529 -0.8; 1636 -0.8; 1751 0.1; 1873 0.2; 2004 -1.4; 2145 -2.2; 2295 1.4; 2455 3.5; 2627 5.3; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.29 | 7.3 dB  |
| Peaking | 64 Hz   | 0.54 | -4.0 dB |
| Peaking | 85 Hz   | 0.4  | -6.1 dB |
| Peaking | 619 Hz  | 2.48 | 1.6 dB  |
| Peaking | 4198 Hz | 1.19 | 7.1 dB  |
| Peaking | 2905 Hz | 0.81 | -3.7 dB |
| Peaking | 2131 Hz | 8.16 | -4.2 dB |
| Peaking | 2810 Hz | 2.1  | 6.5 dB  |
| Peaking | 6140 Hz | 2.76 | 4.5 dB  |
| Peaking | 8080 Hz | 1.64 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Grado%20PS500/Grado%20PS500.png)