# Shure SRH240

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 5.7; 282 4.3; 301 2.8; 323 1.7; 345 0.9; 369 0.3; 395 -0.3; 423 -0.9; 452 -1.6; 484 -2.2; 518 -2.5; 554 -2.4; 593 -2.0; 635 -1.7; 679 -1.7; 726 -1.3; 777 -0.9; 832 -0.6; 890 -0.6; 952 -0.2; 1019 0.0; 1090 0.1; 1167 -0.1; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.7; 1751 -1.6; 1873 -1.3; 2004 -1.2; 2145 -1.0; 2295 -1.1; 2455 -1.1; 2627 -1.4; 2811 -1.3; 3008 -0.6; 3219 -0.4; 3444 -0.4; 3685 -0.3; 3943 -0.1; 4219 -0.1; 4514 0.1; 4830 0.5; 5168 1.6; 5530 3.1; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -2.5; 9502 -2.4; 10167 -1.4; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.1  | 6.6 dB  |
| Peaking | 505 Hz  | 1.23 | -7.4 dB |
| Peaking | 1593 Hz | 0.61 | -2.8 dB |
| Peaking | 6158 Hz | 3.82 | 6.7 dB  |
| Peaking | 9100 Hz | 4.26 | -3.2 dB |
| Peaking | 14 Hz   | 1.64 | 0.9 dB  |
| Peaking | 253 Hz  | 3.1  | 1.9 dB  |
| Peaking | 326 Hz  | 3.9  | -1.6 dB |
| Peaking | 1064 Hz | 1.66 | -1.1 dB |
| Peaking | 1090 Hz | 3.39 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH240/Shure%20SRH240.png)