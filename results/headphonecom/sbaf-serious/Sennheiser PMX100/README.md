# Sennheiser PMX100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.6; 22 1.9; 23 1.6; 25 1.0; 26 0.7; 28 0.2; 30 -0.2; 32 -0.5; 35 -1.0; 37 -1.3; 40 -1.7; 42 -1.9; 45 -2.1; 49 -2.5; 52 -2.8; 56 -3.0; 59 -3.2; 64 -3.5; 68 -3.8; 73 -3.9; 78 -4.1; 83 -4.4; 89 -4.6; 95 -4.8; 102 -4.9; 109 -4.8; 117 -4.9; 125 -5.1; 134 -5.1; 143 -5.2; 153 -5.1; 164 -5.1; 175 -4.8; 188 -4.6; 201 -4.5; 215 -4.3; 230 -4.1; 246 -3.7; 263 -3.2; 282 -3.0; 301 -2.7; 323 -2.3; 345 -2.1; 369 -1.9; 395 -1.7; 423 -1.4; 452 -1.2; 484 -1.0; 518 -0.8; 554 -0.5; 593 -0.4; 635 -0.2; 679 -0.1; 726 0.1; 777 0.2; 832 0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.3; 1636 -2.9; 1751 -3.2; 1873 -3.4; 2004 -3.3; 2145 -2.3; 2295 -1.0; 2455 0.2; 2627 1.1; 2811 3.3; 3008 5.2; 3219 6.0; 3444 6.0; 3685 5.5; 3943 0.6; 4219 -5.9; 4514 -6.5; 4830 -2.1; 5168 2.3; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999997036209dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 128 Hz  | 0.56 | -5.4 dB  |
| Peaking | 1915 Hz | 2.36 | -4.6 dB  |
| Peaking | 3481 Hz | 2.21 | 9.3 dB   |
| Peaking | 4372 Hz | 4.51 | -13.1 dB |
| Peaking | 5848 Hz | 3.52 | 7.2 dB   |
| Peaking | 17 Hz   | 1.32 | 3.4 dB   |
| Peaking | 50 Hz   | 1.62 | -0.8 dB  |
| Peaking | 229 Hz  | 4.02 | -0.5 dB  |
| Peaking | 776 Hz  | 1.98 | 0.8 dB   |
| Peaking | 8295 Hz | 4.78 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX100/Sennheiser%20PMX100.png)