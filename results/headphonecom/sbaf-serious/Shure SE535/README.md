# Shure SE535

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.2; 22 3.1; 23 3.1; 25 3.0; 26 2.9; 28 2.9; 30 2.8; 32 2.8; 35 2.7; 37 2.6; 40 2.4; 42 2.3; 45 2.3; 49 2.1; 52 2.0; 56 1.8; 59 1.6; 64 1.4; 68 1.1; 73 0.7; 78 0.5; 83 0.3; 89 0.1; 95 -0.1; 102 -0.3; 109 -0.5; 117 -0.6; 125 -0.9; 134 -1.1; 143 -1.3; 153 -1.4; 164 -1.6; 175 -1.7; 188 -1.8; 201 -1.8; 215 -1.9; 230 -1.9; 246 -1.9; 263 -1.9; 282 -1.9; 301 -1.8; 323 -1.7; 345 -1.5; 369 -1.2; 395 -1.2; 423 -1.1; 452 -1.1; 484 -1.0; 518 -0.7; 554 -0.5; 593 -0.3; 635 -0.2; 679 -0.1; 726 0.1; 777 0.2; 832 0.3; 890 0.1; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.6; 1429 -0.8; 1529 -1.1; 1636 -1.1; 1751 -1.1; 1873 -0.9; 2004 -0.8; 2145 -0.4; 2295 0.6; 2455 1.8; 2627 2.9; 2811 4.0; 3008 5.1; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -0.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999994864746dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.65 | 3.0 dB  |
| Peaking | 51 Hz   | 1.37 | 1.1 dB  |
| Peaking | 221 Hz  | 0.72 | -2.1 dB |
| Peaking | 1861 Hz | 1.86 | -3.0 dB |
| Peaking | 4049 Hz | 1    | 7.1 dB  |
| Peaking | 784 Hz  | 4.1  | 0.6 dB  |
| Peaking | 3154 Hz | 3.61 | 2.1 dB  |
| Peaking | 3730 Hz | 1.55 | -1.5 dB |
| Peaking | 6281 Hz | 2.5  | 5.0 dB  |
| Peaking | 7483 Hz | 1.59 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE535/Shure%20SE535.png)