# Pioneer HDJ-2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.7; 28 5.1; 30 4.4; 32 3.6; 35 2.4; 37 1.8; 40 0.8; 42 0.3; 45 -0.5; 49 -1.3; 52 -1.9; 56 -2.6; 59 -3.0; 64 -3.6; 68 -3.8; 73 -4.1; 78 -4.4; 83 -4.7; 89 -5.0; 95 -5.3; 102 -5.3; 109 -5.2; 117 -5.2; 125 -5.2; 134 -5.3; 143 -5.5; 153 -5.5; 164 -5.4; 175 -5.1; 188 -5.3; 201 -5.3; 215 -5.3; 230 -5.3; 246 -5.3; 263 -5.3; 282 -5.1; 301 -4.7; 323 -4.4; 345 -3.9; 369 -3.2; 395 -2.4; 423 -1.3; 452 -0.7; 484 -0.2; 518 -0.2; 554 -0.1; 593 0.2; 635 0.2; 679 -0.0; 726 -0.4; 777 -0.7; 832 -0.7; 890 -0.5; 952 -0.1; 1019 -0.1; 1090 -1.0; 1167 -1.3; 1248 -1.5; 1336 -1.8; 1429 -2.3; 1529 -2.7; 1636 -2.6; 1751 -2.3; 1873 -1.6; 2004 -0.6; 2145 1.3; 2295 3.3; 2455 5.4; 2627 6.0; 2811 6.0; 3008 6.0; 3219 5.9; 3444 4.4; 3685 2.0; 3943 0.6; 4219 1.8; 4514 4.7; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -1.2; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.02 | 7.3 dB  |
| Peaking | 102 Hz  | 0.5  | -5.6 dB |
| Peaking | 265 Hz  | 1.73 | -3.1 dB |
| Peaking | 2848 Hz | 3.54 | 6.8 dB  |
| Peaking | 5507 Hz | 2.69 | 6.7 dB  |
| Peaking | 549 Hz  | 2.99 | 1.3 dB  |
| Peaking | 1636 Hz | 1.74 | -5.0 dB |
| Peaking | 2264 Hz | 0.76 | 2.3 dB  |
| Peaking | 3959 Hz | 8.98 | -3.0 dB |
| Peaking | 9113 Hz | 3.49 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)