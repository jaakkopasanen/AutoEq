# Koss Pro4AA 1975

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.7; 64 4.6; 68 3.8; 73 2.8; 78 1.9; 83 1.2; 89 0.5; 95 0.0; 102 -0.6; 109 -1.1; 117 -1.7; 125 -2.4; 134 -2.9; 143 -3.3; 153 -3.8; 164 -4.2; 175 -4.0; 188 -4.6; 201 -5.2; 215 -5.7; 230 -6.4; 246 -7.1; 263 -7.7; 282 -8.2; 301 -8.8; 323 -9.1; 345 -9.0; 369 -8.4; 395 -7.6; 423 -6.2; 452 -4.6; 484 -3.0; 518 -2.1; 554 -1.3; 593 -0.1; 635 1.3; 679 2.7; 726 2.7; 777 3.3; 832 2.5; 890 1.6; 952 0.9; 1019 -0.1; 1090 -0.3; 1167 -1.0; 1248 -1.9; 1336 -2.9; 1429 -3.9; 1529 -5.0; 1636 -5.9; 1751 -6.5; 1873 -6.7; 2004 -6.6; 2145 -6.4; 2295 -6.0; 2455 -4.9; 2627 -4.4; 2811 -3.7; 3008 -2.4; 3219 -1.0; 3444 1.3; 3685 3.0; 3943 5.5; 4219 5.9; 4514 5.6; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA 1975 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.54 | 7.8 dB   |
| Peaking | 352 Hz  | 0.5  | -19.0 dB |
| Peaking | 731 Hz  | 0.44 | 20.4 dB  |
| Peaking | 2059 Hz | 0.47 | -16.2 dB |
| Peaking | 4572 Hz | 1.06 | 13.0 dB  |
| Peaking | 56 Hz   | 1.13 | -1.7 dB  |
| Peaking | 58 Hz   | 2.53 | 2.9 dB   |
| Peaking | 4783 Hz | 7.16 | -1.5 dB  |
| Peaking | 6471 Hz | 3.11 | 3.4 dB   |
| Peaking | 7504 Hz | 2.66 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA%201975/Koss%20Pro4AA%201975.png)