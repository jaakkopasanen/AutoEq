# Sony MDR-XB500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.1; 22 -9.3; 23 -9.4; 25 -9.5; 26 -9.6; 28 -9.7; 30 -9.8; 32 -9.9; 35 -10.0; 37 -10.0; 40 -10.0; 42 -10.0; 45 -10.1; 49 -10.2; 52 -10.3; 56 -10.3; 59 -10.3; 64 -10.2; 68 -10.2; 73 -10.3; 78 -10.8; 83 -11.2; 89 -11.7; 95 -11.8; 102 -11.4; 109 -11.5; 117 -12.0; 125 -12.5; 134 -12.9; 143 -13.3; 153 -13.5; 164 -12.8; 175 -12.4; 188 -12.4; 201 -13.0; 215 -13.6; 230 -13.5; 246 -13.2; 263 -12.8; 282 -12.6; 301 -12.4; 323 -12.1; 345 -11.8; 369 -11.4; 395 -10.9; 423 -10.3; 452 -9.8; 484 -9.0; 518 -8.1; 554 -7.0; 593 -5.8; 635 -4.5; 679 -3.1; 726 -1.6; 777 -0.3; 832 0.8; 890 1.1; 952 0.7; 1019 -0.1; 1090 -1.1; 1167 -1.7; 1248 -2.9; 1336 -4.2; 1429 -4.9; 1529 -5.2; 1636 -5.0; 1751 -4.3; 1873 -3.7; 2004 -2.8; 2145 -1.7; 2295 -0.8; 2455 0.5; 2627 2.0; 2811 3.3; 3008 4.4; 3219 5.8; 3444 6.0; 3685 6.0; 3943 4.6; 4219 2.0; 4514 -0.9; 4830 -2.4; 5168 -1.9; 5530 -0.7; 5917 0.3; 6331 0.8; 6775 -0.2; 7249 -2.3; 7756 -1.4; 8299 -0.0; 8880 0.0; 9502 -0.1; 10167 -1.0; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999993210627dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.19 | -9.1 dB  |
| Peaking | 224 Hz  | 0.65 | -8.2 dB  |
| Peaking | 412 Hz  | 1.89 | -4.2 dB  |
| Peaking | 3413 Hz | 4.25 | 7.4 dB   |
| Peaking | 918 Hz  | 1.84 | 7.0 dB   |
| Peaking | 1691 Hz | 0.74 | -10.1 dB |
| Peaking | 2499 Hz | 0.83 | 7.0 dB   |
| Peaking | 4869 Hz | 6.16 | -4.0 dB  |
| Peaking | 7378 Hz | 9.39 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)