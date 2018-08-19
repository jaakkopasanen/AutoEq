# Syun Mix1 Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -2.7; 22 -3.2; 23 -3.5; 25 -3.9; 26 -4.1; 28 -4.5; 30 -4.8; 32 -5.1; 35 -5.5; 37 -5.7; 40 -6.0; 42 -6.2; 45 -6.5; 49 -6.8; 52 -7.0; 56 -7.3; 59 -7.5; 64 -7.8; 68 -8.0; 73 -8.3; 78 -8.5; 83 -8.7; 89 -9.0; 95 -9.3; 102 -9.5; 109 -9.5; 117 -9.5; 125 -9.7; 134 -9.7; 143 -9.8; 153 -9.8; 164 -9.7; 175 -9.6; 188 -9.4; 201 -9.3; 215 -9.0; 230 -8.7; 246 -8.4; 263 -8.2; 282 -7.8; 301 -7.5; 323 -7.0; 345 -6.5; 369 -6.1; 395 -5.7; 423 -5.1; 452 -4.6; 484 -4.2; 518 -3.7; 554 -3.1; 593 -2.4; 635 -2.0; 679 -1.7; 726 -1.2; 777 -0.8; 832 -0.6; 890 -0.5; 952 -0.3; 1019 0.2; 1090 0.6; 1167 0.9; 1248 0.6; 1336 0.1; 1429 -0.4; 1529 -0.7; 1636 -0.8; 1751 -0.9; 1873 -0.8; 2004 -0.5; 2145 -0.2; 2295 0.1; 2455 0.7; 2627 1.4; 2811 1.9; 3008 2.8; 3219 3.3; 3444 3.5; 3685 2.8; 3943 1.5; 4219 -0.7; 4514 -1.6; 4830 -0.6; 5168 2.3; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.037405458276395dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun Mix1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 69 Hz    | 0.38 | -6.6 dB |
| Peaking | 170 Hz   | 0.75 | -5.1 dB |
| Peaking | 339 Hz   | 1.22 | -3.1 dB |
| Peaking | 3245 Hz  | 4.36 | 3.8 dB  |
| Peaking | 6074 Hz  | 4.83 | 6.7 dB  |
| Peaking | 1151 Hz  | 2.75 | 1.6 dB  |
| Peaking | 1699 Hz  | 2.5  | -1.2 dB |
| Peaking | 4495 Hz  | 5.26 | -5.4 dB |
| Peaking | 4522 Hz  | 2.12 | 2.4 dB  |
| Peaking | 24000 Hz | 1.74 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20Mix1%20Gold/Syun%20Mix1%20Gold.png)