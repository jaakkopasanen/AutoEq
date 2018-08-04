# Koss UR 29

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.4; 49 4.4; 52 3.6; 56 2.9; 59 3.0; 64 3.4; 68 3.2; 73 2.7; 78 2.1; 83 1.7; 89 1.5; 95 1.3; 102 1.1; 109 0.9; 117 0.9; 125 0.9; 134 0.8; 143 0.7; 153 0.7; 164 1.1; 175 1.0; 188 1.0; 201 1.0; 215 0.8; 230 0.6; 246 0.5; 263 0.4; 282 0.4; 301 0.5; 323 0.6; 345 0.8; 369 0.8; 395 0.9; 423 1.1; 452 1.3; 484 1.3; 518 1.1; 554 1.1; 593 0.7; 635 0.1; 679 -0.0; 726 0.2; 777 0.3; 832 -0.0; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.5; 1167 1.0; 1248 1.5; 1336 2.1; 1429 2.6; 1529 3.0; 1636 2.8; 1751 1.8; 1873 0.6; 2004 0.6; 2145 0.7; 2295 1.7; 2455 3.3; 2627 4.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.0; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.68 | 7.5 dB  |
| Peaking | 29 Hz   | 2.19 | -1.6 dB |
| Peaking | 454 Hz  | 1.99 | 1.1 dB  |
| Peaking | 3410 Hz | 1.34 | 6.1 dB  |
| Peaking | 5658 Hz | 2.96 | 4.7 dB  |
| Peaking | 1013 Hz | 1.62 | -1.9 dB |
| Peaking | 1629 Hz | 1.19 | 3.9 dB  |
| Peaking | 2004 Hz | 2.86 | -4.6 dB |
| Peaking | 6564 Hz | 7.53 | 2.2 dB  |
| Peaking | 8186 Hz | 2.03 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Koss%20UR%2029/Koss%20UR%2029.png)