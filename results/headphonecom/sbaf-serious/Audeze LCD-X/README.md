# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.6; 22 2.6; 23 2.6; 25 2.6; 26 2.6; 28 2.6; 30 2.6; 32 2.5; 35 2.2; 37 2.0; 40 1.8; 42 1.6; 45 1.4; 49 1.4; 52 1.4; 56 1.3; 59 1.1; 64 0.9; 68 0.9; 73 0.8; 78 0.5; 83 0.3; 89 0.2; 95 0.0; 102 -0.1; 109 -0.2; 117 -0.4; 125 -0.6; 134 -0.7; 143 -0.9; 153 -1.0; 164 -1.1; 175 -1.2; 188 -1.2; 201 -1.2; 215 -1.2; 230 -1.2; 246 -1.2; 263 -1.3; 282 -1.3; 301 -1.4; 323 -1.4; 345 -1.5; 369 -1.1; 395 -0.8; 423 -1.0; 452 -1.1; 484 -1.0; 518 -0.9; 554 -0.8; 593 -0.5; 635 -0.3; 679 -0.5; 726 -0.5; 777 -0.6; 832 -0.6; 890 -0.2; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.3; 1248 -0.3; 1336 -0.7; 1429 -1.0; 1529 -1.7; 1636 -2.1; 1751 -2.1; 1873 -1.5; 2004 -1.4; 2145 -2.1; 2295 -1.4; 2455 0.4; 2627 1.3; 2811 2.0; 3008 2.5; 3219 5.2; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -1.1; 16326 -3.2; 17469 -4.9; 18692 -4.5; 20000 -0.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230117dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.4  | 2.7 dB  |
| Peaking | 235 Hz   | 0.55 | -1.5 dB |
| Peaking | 2012 Hz  | 1.7  | -3.8 dB |
| Peaking | 4269 Hz  | 1.06 | 7.3 dB  |
| Peaking | 17959 Hz | 1.6  | -5.4 dB |
| Peaking | 1123 Hz  | 6.81 | 0.8 dB  |
| Peaking | 3361 Hz  | 7.92 | 2.0 dB  |
| Peaking | 4435 Hz  | 1.43 | -1.2 dB |
| Peaking | 6335 Hz  | 2.59 | 4.0 dB  |
| Peaking | 7601 Hz  | 2.39 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)