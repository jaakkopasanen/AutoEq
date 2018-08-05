# Shure SE530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.0; 22 2.9; 23 2.9; 25 2.8; 26 2.8; 28 2.7; 30 2.7; 32 2.6; 35 2.6; 37 2.6; 40 2.5; 42 2.5; 45 2.4; 49 2.4; 52 2.3; 56 2.1; 59 2.1; 64 2.0; 68 1.9; 73 1.8; 78 1.6; 83 1.3; 89 1.0; 95 0.6; 102 0.1; 109 -0.4; 117 -0.9; 125 -1.6; 134 -2.0; 143 -2.4; 153 -2.6; 164 -2.8; 175 -2.9; 188 -2.9; 201 -3.0; 215 -2.9; 230 -2.9; 246 -2.9; 263 -2.9; 282 -2.7; 301 -2.5; 323 -2.3; 345 -2.1; 369 -1.9; 395 -1.7; 423 -1.6; 452 -1.5; 484 -1.6; 518 -1.3; 554 -1.0; 593 -0.6; 635 -0.4; 679 -0.3; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.4; 1529 -1.9; 1636 -2.3; 1751 -2.7; 1873 -2.9; 2004 -3.1; 2145 -2.9; 2295 -2.2; 2455 -0.9; 2627 0.3; 2811 1.4; 3008 2.7; 3219 3.8; 3444 4.8; 3685 5.5; 3943 5.7; 4219 4.6; 4514 3.9; 4830 4.3; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.21 | 3.3 dB  |
| Peaking | 187 Hz  | 0.67 | -5.4 dB |
| Peaking | 2008 Hz | 2.1  | -4.1 dB |
| Peaking | 5819 Hz | 3.29 | 5.7 dB  |
| Peaking | 3667 Hz | 2.05 | 5.6 dB  |
| Peaking | 216 Hz  | 4.68 | 0.4 dB  |
| Peaking | 548 Hz  | 1.05 | -1.0 dB |
| Peaking | 761 Hz  | 1.27 | 1.4 dB  |
| Peaking | 1503 Hz | 4.53 | -0.6 dB |
| Peaking | 8266 Hz | 4.52 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE530/Shure%20SE530.png)