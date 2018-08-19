# Shure SRH440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.9; 83 4.9; 89 3.7; 95 2.9; 102 2.3; 109 1.9; 117 1.8; 125 1.6; 134 1.4; 143 1.4; 153 1.1; 164 1.5; 175 1.6; 188 1.5; 201 1.5; 215 1.7; 230 1.8; 246 1.6; 263 1.3; 282 0.9; 301 0.7; 323 0.4; 345 0.1; 369 -0.6; 395 -0.6; 423 -0.5; 452 -0.4; 484 -0.4; 518 -0.4; 554 -0.4; 593 -0.4; 635 -0.4; 679 -0.3; 726 -0.4; 777 -0.3; 832 -0.4; 890 -0.3; 952 -0.2; 1019 0.3; 1090 0.9; 1167 -0.0; 1248 -0.3; 1336 -0.6; 1429 -1.3; 1529 -2.0; 1636 -2.5; 1751 -2.7; 1873 -2.4; 2004 -1.5; 2145 -0.7; 2295 0.4; 2455 1.3; 2627 1.8; 2811 2.0; 3008 2.3; 3219 2.1; 3444 1.5; 3685 1.2; 3943 1.7; 4219 1.1; 4514 0.4; 4830 2.0; 5168 5.5; 5530 2.8; 5917 3.3; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.7; 8880 -3.8; 9502 -6.5; 10167 -6.6; 10879 -3.2; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.46 | 6.7 dB  |
| Peaking | 1760 Hz | 2.78 | -3.3 dB |
| Peaking | 2825 Hz | 2.35 | 2.4 dB  |
| Peaking | 6156 Hz | 2.17 | 5.0 dB  |
| Peaking | 9720 Hz | 3.94 | -8.3 dB |
| Peaking | 39 Hz   | 2.54 | -0.7 dB |
| Peaking | 76 Hz   | 2.73 | 2.5 dB  |
| Peaking | 100 Hz  | 1.26 | -1.5 dB |
| Peaking | 238 Hz  | 1.77 | 1.4 dB  |
| Peaking | 400 Hz  | 1.47 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)