# Comradz NW-STUDIO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 5.8; 395 5.4; 423 5.1; 452 4.7; 484 3.2; 518 -2.4; 554 0.5; 593 2.7; 635 2.9; 679 2.6; 726 2.3; 777 2.2; 832 1.8; 890 1.2; 952 0.5; 1019 -0.3; 1090 -1.3; 1167 -2.6; 1248 -4.3; 1336 -6.5; 1429 -8.8; 1529 -11.4; 1636 -13.8; 1751 -16.0; 1873 -17.7; 2004 -18.7; 2145 -19.2; 2295 -18.9; 2455 -17.6; 2627 -16.4; 2811 -15.0; 3008 -12.7; 3219 -10.0; 3444 -8.3; 3685 -8.6; 3943 -9.3; 4219 -11.2; 4514 -12.7; 4830 -13.3; 5168 -13.5; 5530 -14.6; 5917 -15.7; 6331 -15.8; 6775 -14.8; 7249 -14.7; 7756 -16.3; 8299 -18.6; 8880 -19.0; 9502 -15.8; 10167 -9.9; 10879 -3.6; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 106 Hz   | 0.06 | 6.3 dB   |
| Peaking | 2083 Hz  | 1.26 | -22.1 dB |
| Peaking | 5916 Hz  | 1.51 | -9.5 dB  |
| Peaking | 8921 Hz  | 2.25 | -17.6 dB |
| Peaking | 11744 Hz | 1.85 | 6.6 dB   |
| Peaking | 527 Hz   | 9.22 | -7.7 dB  |
| Peaking | 974 Hz   | 0.49 | 1.6 dB   |
| Peaking | 1593 Hz  | 4.21 | -3.4 dB  |
| Peaking | 2739 Hz  | 4.51 | -3.0 dB  |
| Peaking | 3442 Hz  | 6.35 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO/Comradz%20NW-STUDIO.png)