# Koss UR 29

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.0; 52 4.2; 56 3.4; 59 3.5; 64 4.0; 68 3.8; 73 3.3; 78 2.7; 83 2.4; 89 2.3; 95 2.1; 102 2.1; 109 2.1; 117 2.1; 125 2.2; 134 2.1; 143 2.0; 153 2.0; 164 2.4; 175 2.3; 188 2.4; 201 2.3; 215 2.2; 230 2.0; 246 1.9; 263 1.7; 282 1.8; 301 1.9; 323 2.0; 345 2.2; 369 2.2; 395 2.1; 423 2.3; 452 2.3; 484 2.0; 518 1.6; 554 1.6; 593 1.1; 635 0.4; 679 0.1; 726 0.2; 777 0.5; 832 0.1; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.4; 1167 0.7; 1248 0.9; 1336 0.8; 1429 0.4; 1529 0.3; 1636 -0.2; 1751 -1.2; 1873 -2.3; 2004 -2.3; 2145 -2.3; 2295 -1.4; 2455 0.4; 2627 1.9; 2811 3.4; 3008 4.8; 3219 5.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.1; 8880 -2.9; 9502 -1.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.51 | 6.3 dB  |
| Peaking | 277 Hz  | 0.69 | 2.0 dB  |
| Peaking | 2075 Hz | 2.44 | -5.8 dB |
| Peaking | 4408 Hz | 0.7  | 7.2 dB  |
| Peaking | 8786 Hz | 2.8  | -5.5 dB |
| Peaking | 458 Hz  | 4.25 | 1.0 dB  |
| Peaking | 843 Hz  | 2.56 | -0.9 dB |
| Peaking | 3181 Hz | 4.1  | 1.2 dB  |
| Peaking | 5249 Hz | 1.04 | -1.0 dB |
| Peaking | 6116 Hz | 4.38 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2029/Koss%20UR%2029.png)