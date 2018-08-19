# Audeze LCD-2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.7; 22 3.6; 23 3.6; 25 3.5; 26 3.5; 28 3.5; 30 3.5; 32 3.5; 35 3.5; 37 3.5; 40 3.4; 42 3.3; 45 3.1; 49 2.9; 52 2.8; 56 2.6; 59 2.5; 64 2.1; 68 1.9; 73 1.7; 78 1.6; 83 1.4; 89 1.2; 95 0.9; 102 0.7; 109 0.6; 117 0.4; 125 0.2; 134 0.0; 143 -0.1; 153 -0.3; 164 -0.4; 175 -0.5; 188 -0.5; 201 -0.7; 215 -0.7; 230 -0.8; 246 -0.9; 263 -1.0; 282 -0.9; 301 -0.9; 323 -0.9; 345 -0.9; 369 -0.9; 395 -0.9; 423 -0.7; 452 -0.7; 484 -0.7; 518 -0.5; 554 -0.5; 593 -0.5; 635 -0.8; 679 -1.0; 726 -1.1; 777 -1.0; 832 -1.2; 890 -1.0; 952 -0.5; 1019 0.2; 1090 0.9; 1167 1.3; 1248 1.4; 1336 1.3; 1429 0.7; 1529 0.4; 1636 0.8; 1751 1.4; 1873 2.2; 2004 2.4; 2145 2.1; 2295 2.2; 2455 2.6; 2627 2.8; 2811 2.9; 3008 3.5; 3219 3.9; 3444 4.6; 3685 5.8; 3943 6.0; 4219 6.0; 4514 5.2; 4830 4.3; 5168 4.1; 5530 4.1; 5917 4.8; 6331 5.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.3; 18692 -2.9; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999994318308834dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.95 | 3.5 dB  |
| Peaking | 49 Hz    | 1.45 | 2.1 dB  |
| Peaking | 2149 Hz  | 1.95 | 1.6 dB  |
| Peaking | 3988 Hz  | 1.95 | 5.9 dB  |
| Peaking | 6195 Hz  | 4.46 | 4.0 dB  |
| Peaking | 47 Hz    | 1.52 | -0.5 dB |
| Peaking | 84 Hz    | 1.13 | 0.9 dB  |
| Peaking | 364 Hz   | 0.31 | -1.0 dB |
| Peaking | 1213 Hz  | 4.73 | 1.7 dB  |
| Peaking | 19244 Hz | 1.97 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2/Audeze%20LCD-2.png)