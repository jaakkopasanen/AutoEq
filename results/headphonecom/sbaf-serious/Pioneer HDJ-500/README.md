# Pioneer HDJ-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 4.9; 32 3.9; 35 2.3; 37 1.4; 40 0.2; 42 -0.4; 45 -1.2; 49 -1.9; 52 -2.3; 56 -2.7; 59 -2.8; 64 -3.0; 68 -2.9; 73 -2.8; 78 -2.7; 83 -2.8; 89 -3.0; 95 -3.2; 102 -3.3; 109 -3.2; 117 -3.3; 125 -3.6; 134 -3.9; 143 -4.1; 153 -4.2; 164 -4.3; 175 -4.4; 188 -4.6; 201 -4.6; 215 -4.7; 230 -4.8; 246 -4.6; 263 -4.4; 282 -4.4; 301 -4.6; 323 -4.6; 345 -4.8; 369 -5.4; 395 -5.6; 423 -5.0; 452 -4.6; 484 -4.4; 518 -3.7; 554 -2.9; 593 -2.2; 635 -1.6; 679 -1.2; 726 -1.1; 777 -1.0; 832 -0.7; 890 -0.4; 952 -0.4; 1019 0.1; 1090 0.7; 1167 1.2; 1248 1.6; 1336 1.8; 1429 2.2; 1529 2.7; 1636 3.1; 1751 3.6; 1873 4.6; 2004 5.7; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 1.1; 5168 -1.6; 5530 -3.2; 5917 1.8; 6331 5.4; 6775 1.3; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -1.7; 17469 -2.5; 18692 -1.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.27 | 8.6 dB  |
| Peaking | 103 Hz   | 0.25 | -3.9 dB |
| Peaking | 393 Hz   | 1.28 | -3.2 dB |
| Peaking | 2366 Hz  | 1.14 | 6.4 dB  |
| Peaking | 3956 Hz  | 3.86 | 4.2 dB  |
| Peaking | 202 Hz   | 4.23 | -0.7 dB |
| Peaking | 4524 Hz  | 9.22 | 4.2 dB  |
| Peaking | 5472 Hz  | 3.77 | -6.4 dB |
| Peaking | 6210 Hz  | 7.81 | 7.8 dB  |
| Peaking | 17519 Hz | 2.67 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)