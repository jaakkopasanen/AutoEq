# Shure SRH1440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.7; 78 5.1; 83 4.7; 89 4.3; 95 3.9; 102 3.5; 109 3.2; 117 2.9; 125 2.5; 134 2.1; 143 1.8; 153 1.4; 164 1.3; 175 1.1; 188 0.9; 201 0.8; 215 0.6; 230 0.6; 246 0.4; 263 0.4; 282 0.3; 301 0.2; 323 0.2; 345 0.4; 369 0.5; 395 0.5; 423 0.6; 452 0.6; 484 0.7; 518 0.7; 554 0.7; 593 0.7; 635 1.2; 679 1.6; 726 1.2; 777 1.0; 832 0.8; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.4; 1429 -2.2; 1529 -3.1; 1636 -4.1; 1751 -4.9; 1873 -5.4; 2004 -5.7; 2145 -6.1; 2295 -6.4; 2455 -6.3; 2627 -6.1; 2811 -6.6; 3008 -6.7; 3219 -6.5; 3444 -6.6; 3685 -6.5; 3943 -6.4; 4219 -6.0; 4514 -5.3; 4830 -3.8; 5168 -2.9; 5530 -1.3; 5917 -1.1; 6331 -2.0; 6775 -0.5; 7249 -0.4; 7756 -1.0; 8299 -2.8; 8880 -5.6; 9502 -7.6; 10167 -6.6; 10879 -2.5; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.45 | 6.7 dB   |
| Peaking | 937 Hz  | 0.9  | 3.3 dB   |
| Peaking | 3327 Hz | 0.46 | -9.3 dB  |
| Peaking | 7480 Hz | 0.69 | 6.6 dB   |
| Peaking | 9551 Hz | 3.19 | -10.4 dB |
| Peaking | 42 Hz   | 2.1  | -0.9 dB  |
| Peaking | 69 Hz   | 3.48 | 1.0 dB   |
| Peaking | 1908 Hz | 3.51 | -1.0 dB  |
| Peaking | 2816 Hz | 0.7  | 0.5 dB   |
| Peaking | 4162 Hz | 4.96 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)