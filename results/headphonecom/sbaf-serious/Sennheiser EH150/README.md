# Sennheiser EH150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 5.7; 484 4.2; 518 2.8; 554 1.6; 593 1.0; 635 0.6; 679 0.6; 726 0.5; 777 0.2; 832 0.0; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.2; 1336 0.0; 1429 0.1; 1529 0.0; 1636 0.2; 1751 0.7; 1873 1.4; 2004 2.0; 2145 2.7; 2295 3.8; 2455 4.7; 2627 5.5; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.0; 4514 0.4; 4830 2.8; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.23 | 6.2 dB  |
| Peaking | 229 Hz  | 1.07 | 3.4 dB  |
| Peaking | 401 Hz  | 2.76 | 4.0 dB  |
| Peaking | 3126 Hz | 1.81 | 6.6 dB  |
| Peaking | 5889 Hz | 3.83 | 5.8 dB  |
| Peaking | 2480 Hz | 1.6  | 4.1 dB  |
| Peaking | 3356 Hz | 0.52 | -4.1 dB |
| Peaking | 3894 Hz | 6.73 | 4.0 dB  |
| Peaking | 6262 Hz | 1.38 | 3.2 dB  |
| Peaking | 7808 Hz | 4.2  | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH150/Sennheiser%20EH150.png)