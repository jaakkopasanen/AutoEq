# Sony MDR-7509HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.3; 68 4.4; 73 3.4; 78 2.5; 83 1.7; 89 0.9; 95 0.6; 102 0.7; 109 0.6; 117 0.4; 125 -0.1; 134 -0.9; 143 -1.5; 153 -2.2; 164 -1.8; 175 -1.7; 188 -2.2; 201 -1.8; 215 -1.7; 230 -1.5; 246 -1.3; 263 -1.0; 282 -0.5; 301 -0.2; 323 -0.2; 345 -0.8; 369 -1.6; 395 -2.5; 423 -2.9; 452 -3.7; 484 -3.6; 518 -3.4; 554 -2.7; 593 -1.4; 635 0.1; 679 -0.9; 726 -1.1; 777 -0.5; 832 -0.2; 890 -0.0; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -3.1; 1529 -4.3; 1636 -5.4; 1751 -6.1; 1873 -6.3; 2004 -7.2; 2145 -7.1; 2295 -6.2; 2455 -4.3; 2627 -1.8; 2811 -0.7; 3008 0.8; 3219 1.9; 3444 3.0; 3685 5.1; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.4; 5530 1.9; 5917 5.2; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -3.4; 8880 -5.2; 9502 -4.5; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.91 | 7.2 dB  |
| Peaking | 2048 Hz | 1.71 | -8.6 dB |
| Peaking | 4152 Hz | 1.51 | 7.4 dB  |
| Peaking | 6403 Hz | 5.84 | 4.3 dB  |
| Peaking | 8934 Hz | 4.31 | -6.7 dB |
| Peaking | 36 Hz   | 3.37 | -1.2 dB |
| Peaking | 60 Hz   | 3.04 | 2.7 dB  |
| Peaking | 170 Hz  | 1.59 | -2.5 dB |
| Peaking | 473 Hz  | 3.07 | -3.8 dB |
| Peaking | 1049 Hz | 2.85 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7509HD/Sony%20MDR-7509HD.png)