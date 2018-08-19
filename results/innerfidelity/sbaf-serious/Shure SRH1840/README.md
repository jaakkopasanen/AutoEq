# Shure SRH1840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.6; 59 5.3; 64 4.9; 68 4.7; 73 4.8; 78 4.6; 83 4.1; 89 3.4; 95 2.8; 102 2.3; 109 2.1; 117 1.7; 125 1.4; 134 1.0; 143 0.8; 153 0.5; 164 0.4; 175 0.2; 188 0.0; 201 -0.2; 215 -0.2; 230 -0.2; 246 -0.2; 263 -0.2; 282 -0.2; 301 -0.3; 323 -0.3; 345 -0.1; 369 -0.1; 395 0.0; 423 0.3; 452 0.5; 484 0.5; 518 0.6; 554 0.8; 593 1.0; 635 0.9; 679 0.9; 726 0.9; 777 1.4; 832 0.9; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.9; 1636 -2.6; 1751 -3.2; 1873 -3.7; 2004 -4.1; 2145 -4.5; 2295 -4.7; 2455 -4.2; 2627 -4.4; 2811 -4.2; 3008 -4.2; 3219 -4.0; 3444 -3.9; 3685 -3.9; 3943 -3.5; 4219 -3.0; 4514 -2.6; 4830 -1.3; 5168 0.2; 5530 0.8; 5917 -0.0; 6331 0.2; 6775 0.4; 7249 0.7; 7756 -1.3; 8299 -4.2; 8880 -5.9; 9502 -4.2; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.56 | 6.7 dB  |
| Peaking | 952 Hz   | 0.98 | 2.4 dB  |
| Peaking | 3053 Hz  | 0.51 | -6.1 dB |
| Peaking | 6536 Hz  | 0.83 | 4.9 dB  |
| Peaking | 8848 Hz  | 4.13 | -8.0 dB |
| Peaking | 35 Hz    | 3.14 | -0.6 dB |
| Peaking | 77 Hz    | 2.91 | 1.2 dB  |
| Peaking | 202 Hz   | 1.23 | -0.9 dB |
| Peaking | 1396 Hz  | 7.3  | 0.6 dB  |
| Peaking | 10255 Hz | 9.25 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)