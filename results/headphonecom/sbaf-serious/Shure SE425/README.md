# Shure SE425

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.1; 22 5.8; 23 5.7; 25 5.5; 26 5.4; 28 5.2; 30 5.1; 32 4.9; 35 4.7; 37 4.6; 40 4.5; 42 4.4; 45 4.2; 49 4.0; 52 3.9; 56 3.7; 59 3.6; 64 3.3; 68 3.1; 73 2.9; 78 2.7; 83 2.4; 89 2.0; 95 1.5; 102 0.9; 109 0.3; 117 -0.3; 125 -0.9; 134 -1.5; 143 -1.9; 153 -2.2; 164 -2.3; 175 -2.4; 188 -2.5; 201 -2.5; 215 -2.5; 230 -2.4; 246 -2.4; 263 -2.4; 282 -2.3; 301 -2.0; 323 -2.0; 345 -1.9; 369 -1.6; 395 -1.5; 423 -1.3; 452 -1.1; 484 -1.1; 518 -1.0; 554 -0.5; 593 -0.3; 635 -0.1; 679 0.0; 726 0.2; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -1.0; 1429 -1.4; 1529 -1.7; 1636 -1.9; 1751 -2.1; 1873 -2.1; 2004 -2.1; 2145 -2.2; 2295 -2.0; 2455 -1.4; 2627 -0.8; 2811 0.2; 3008 1.6; 3219 2.8; 3444 3.8; 3685 4.3; 3943 4.5; 4219 3.8; 4514 3.7; 4830 4.6; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.4; 8299 -0.3; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.26 | 6.0 dB  |
| Peaking | 86 Hz   | 0.93 | 3.4 dB  |
| Peaking | 143 Hz  | 0.52 | -4.6 dB |
| Peaking | 3771 Hz | 4.23 | 4.1 dB  |
| Peaking | 5647 Hz | 2.98 | 6.6 dB  |
| Peaking | 807 Hz  | 2.01 | 1.1 dB  |
| Peaking | 2041 Hz | 1.35 | -2.7 dB |
| Peaking | 6628 Hz | 7.14 | 2.2 dB  |
| Peaking | 3180 Hz | 3.66 | 1.9 dB  |
| Peaking | 7827 Hz | 3.87 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE425/Shure%20SE425.png)