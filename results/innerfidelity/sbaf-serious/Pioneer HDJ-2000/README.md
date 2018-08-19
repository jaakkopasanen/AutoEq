# Pioneer HDJ-2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.2; 56 3.9; 59 3.0; 64 1.9; 68 1.1; 73 0.2; 78 -0.6; 83 -1.3; 89 -1.9; 95 -2.3; 102 -2.5; 109 -2.5; 117 -2.2; 125 -2.1; 134 -2.1; 143 -2.1; 153 -2.2; 164 -2.1; 175 -1.9; 188 -2.0; 201 -2.0; 215 -2.0; 230 -1.9; 246 -1.9; 263 -1.8; 282 -1.6; 301 -1.4; 323 -1.3; 345 -1.2; 369 -1.1; 395 -1.2; 423 -0.9; 452 -0.8; 484 -0.7; 518 -0.7; 554 -0.7; 593 -0.6; 635 -0.6; 679 -0.8; 726 -1.0; 777 -1.0; 832 -0.8; 890 -0.3; 952 0.0; 1019 -0.2; 1090 -0.8; 1167 -1.1; 1248 -1.0; 1336 -1.2; 1429 -1.5; 1529 -1.6; 1636 -1.5; 1751 -1.1; 1873 -0.5; 2004 0.6; 2145 2.1; 2295 3.8; 2455 5.4; 2627 6.0; 2811 6.0; 3008 6.0; 3219 5.8; 3444 4.9; 3685 2.6; 3943 0.8; 4219 1.3; 4514 4.2; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.4; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.46 | 9.3 dB  |
| Peaking | 91 Hz   |  0.74 | -7.1 dB |
| Peaking | 935 Hz  |  0.06 | -1.2 dB |
| Peaking | 2805 Hz |  2.48 | 7.6 dB  |
| Peaking | 5587 Hz |  2.31 | 7.4 dB  |
| Peaking | 1449 Hz |  0.66 | 2.1 dB  |
| Peaking | 1606 Hz |  1.3  | -3.5 dB |
| Peaking | 2290 Hz |  6.63 | 1.5 dB  |
| Peaking | 4103 Hz |  9.37 | -2.7 dB |
| Peaking | 4736 Hz | 11.34 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)