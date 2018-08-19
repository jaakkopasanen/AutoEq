# Sennheiser HD 424

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.8; 95 4.9; 102 3.8; 109 3.0; 117 2.1; 125 1.1; 134 0.2; 143 -0.5; 153 -1.0; 164 -1.4; 175 -1.6; 188 -1.6; 201 -1.6; 215 -1.4; 230 -1.2; 246 -1.0; 263 -0.7; 282 -0.4; 301 -0.1; 323 0.1; 345 0.4; 369 0.6; 395 0.8; 423 1.1; 452 1.3; 484 1.3; 518 1.3; 554 1.4; 593 1.5; 635 1.5; 679 1.3; 726 1.2; 777 1.3; 832 1.0; 890 0.7; 952 0.4; 1019 0.1; 1090 -0.2; 1167 -0.6; 1248 -1.0; 1336 -1.9; 1429 -2.9; 1529 -3.6; 1636 -4.5; 1751 -4.9; 1873 -5.4; 2004 -5.1; 2145 -4.3; 2295 -3.4; 2455 -2.2; 2627 -1.2; 2811 -0.8; 3008 -0.3; 3219 -0.3; 3444 -0.7; 3685 -0.7; 3943 -0.7; 4219 -0.4; 4514 0.5; 4830 2.6; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -1.3; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 424 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.27 | 7.3 dB  |
| Peaking | 175 Hz   | 1    | -6.7 dB |
| Peaking | 688 Hz   | 1.02 | 1.5 dB  |
| Peaking | 1835 Hz  | 1.78 | -5.8 dB |
| Peaking | 5781 Hz  | 3.46 | 7.1 dB  |
| Peaking | 17 Hz    | 1.12 | 1.8 dB  |
| Peaking | 41 Hz    | 0.53 | -0.9 dB |
| Peaking | 85 Hz    | 3.7  | 1.5 dB  |
| Peaking | 8956 Hz  | 5.97 | -1.8 dB |
| Peaking | 23904 Hz | 1.91 | 0.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20424/Sennheiser%20HD%20424.png)