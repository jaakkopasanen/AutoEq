# Audeze LCD-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.8; 22 1.3; 23 1.5; 25 1.4; 26 1.3; 28 0.9; 30 0.6; 32 0.6; 35 0.8; 37 0.7; 40 0.2; 42 0.0; 45 -0.3; 49 -0.9; 52 -1.0; 56 -0.8; 59 -0.8; 64 -0.9; 68 -1.0; 73 -1.2; 78 -1.3; 83 -1.5; 89 -1.6; 95 -1.8; 102 -1.9; 109 -2.0; 117 -2.2; 125 -2.4; 134 -2.5; 143 -2.7; 153 -2.8; 164 -2.9; 175 -3.2; 188 -3.3; 201 -3.5; 215 -3.5; 230 -3.6; 246 -3.7; 263 -3.7; 282 -3.4; 301 -2.8; 323 -2.2; 345 -2.1; 369 -2.0; 395 -2.3; 423 -2.8; 452 -3.1; 484 -3.0; 518 -2.7; 554 -2.6; 593 -2.4; 635 -2.5; 679 -2.3; 726 -2.0; 777 -2.3; 832 -2.5; 890 -1.7; 952 -0.6; 1019 0.2; 1090 0.9; 1167 0.9; 1248 -0.2; 1336 -0.3; 1429 -0.5; 1529 -0.8; 1636 -0.3; 1751 0.4; 1873 1.4; 2004 2.4; 2145 1.9; 2295 0.7; 2455 1.7; 2627 1.6; 2811 1.6; 3008 1.2; 3219 1.8; 3444 3.5; 3685 5.8; 3943 6.0; 4219 6.0; 4514 5.6; 4830 3.8; 5168 2.1; 5530 0.7; 5917 1.4; 6331 2.3; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -2.3; 16326 -5.6; 17469 -7.8; 18692 -7.8; 20000 -5.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999752452863dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 201 Hz   | 0.66 | -3.3 dB |
| Peaking | 606 Hz   | 1.46 | -2.0 dB |
| Peaking | 2029 Hz  | 6    | 2.1 dB  |
| Peaking | 4115 Hz  | 2.27 | 6.4 dB  |
| Peaking | 18283 Hz | 1.6  | -9.1 dB |
| Peaking | 24 Hz    | 1.89 | 1.5 dB  |
| Peaking | 1098 Hz  | 1.81 | -1.8 dB |
| Peaking | 1101 Hz  | 4.23 | 3.6 dB  |
| Peaking | 13611 Hz | 3    | 1.6 dB  |
| Peaking | 21198 Hz | 1.28 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)