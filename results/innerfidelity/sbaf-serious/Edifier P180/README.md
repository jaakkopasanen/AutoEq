# Edifier P180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.1; 52 4.2; 56 2.9; 59 1.9; 64 0.5; 68 -0.6; 73 -1.8; 78 -3.0; 83 -4.1; 89 -5.1; 95 -6.0; 102 -6.6; 109 -6.9; 117 -7.1; 125 -7.0; 134 -6.7; 143 -6.6; 153 -6.4; 164 -5.8; 175 -5.5; 188 -5.2; 201 -4.9; 215 -4.4; 230 -4.0; 246 -3.9; 263 -3.6; 282 -3.3; 301 -3.1; 323 -2.9; 345 -3.1; 369 -2.7; 395 -2.1; 423 -2.0; 452 -1.4; 484 -1.0; 518 -0.8; 554 -0.5; 593 0.0; 635 -0.0; 679 0.1; 726 0.2; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.4; 1167 -1.1; 1248 -2.2; 1336 -3.8; 1429 -5.9; 1529 -8.2; 1636 -10.3; 1751 -12.4; 1873 -13.8; 2004 -14.9; 2145 -15.3; 2295 -14.7; 2455 -13.1; 2627 -11.5; 2811 -9.5; 3008 -6.9; 3219 -4.7; 3444 -2.9; 3685 -2.3; 3943 -2.7; 4219 -4.2; 4514 -5.6; 4830 -6.4; 5168 -7.1; 5530 -8.6; 5917 -10.1; 6331 -10.7; 6775 -9.7; 7249 -9.1; 7756 -9.1; 8299 -8.9; 8880 -7.8; 9502 -5.7; 10167 -3.1; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.2; 15258 -2.1; 16326 -0.9; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Edifier P180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.54 | 9.4 dB   |
| Peaking | 109 Hz   | 0.68 | -10.7 dB |
| Peaking | 2103 Hz  | 2.13 | -16.3 dB |
| Peaking | 6846 Hz  | 1.5  | -10.4 dB |
| Peaking | 24000 Hz | 3.7  | -0.5 dB  |
| Peaking | 972 Hz   | 0.91 | 3.7 dB   |
| Peaking | 1615 Hz  | 4.84 | -3.3 dB  |
| Peaking | 2060 Hz  | 0.13 | -1.3 dB  |
| Peaking | 3693 Hz  | 4.61 | 4.1 dB   |
| Peaking | 11664 Hz | 3.42 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Edifier%20P180/Edifier%20P180.png)