# Shure SRH1840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.6; 52 5.4; 56 5.2; 59 5.0; 64 4.6; 68 4.4; 73 4.4; 78 4.5; 83 4.4; 89 3.7; 95 3.1; 102 2.5; 109 2.2; 117 1.9; 125 1.5; 134 1.2; 143 0.9; 153 0.6; 164 0.5; 175 0.3; 188 0.1; 201 -0.1; 215 -0.1; 230 -0.1; 246 -0.2; 263 -0.2; 282 -0.2; 301 -0.2; 323 -0.2; 345 -0.1; 369 0.0; 395 -0.1; 423 -0.1; 452 0.2; 484 0.3; 518 0.4; 554 0.6; 593 0.7; 635 0.7; 679 0.8; 726 0.9; 777 1.4; 832 0.9; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -2.1; 1636 -2.6; 1751 -3.2; 1873 -4.1; 2004 -4.6; 2145 -5.0; 2295 -5.1; 2455 -4.9; 2627 -4.9; 2811 -4.8; 3008 -4.7; 3219 -4.4; 3444 -4.0; 3685 -3.8; 3943 -3.4; 4219 -2.4; 4514 -2.2; 4830 -0.8; 5168 0.7; 5530 1.1; 5917 -0.3; 6331 -1.4; 6775 -0.3; 7249 0.7; 7756 -0.4; 8299 -2.7; 8880 -4.7; 9502 -3.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -0.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.51 | 6.5 dB  |
| Peaking | 976 Hz  | 1.09 | 2.1 dB  |
| Peaking | 2708 Hz | 0.7  | -6.3 dB |
| Peaking | 6041 Hz | 0.81 | 2.6 dB  |
| Peaking | 8932 Hz | 5.47 | -5.7 dB |
| Peaking | 37 Hz   | 2.28 | -0.4 dB |
| Peaking | 83 Hz   | 3.85 | 1.3 dB  |
| Peaking | 213 Hz  | 1.22 | -0.9 dB |
| Peaking | 5384 Hz | 7.46 | 1.9 dB  |
| Peaking | 6258 Hz | 9.37 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)