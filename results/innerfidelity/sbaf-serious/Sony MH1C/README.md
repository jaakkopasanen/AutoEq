# Sony MH1C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -11.0; 22 -10.8; 23 -10.7; 25 -10.6; 26 -10.5; 28 -10.4; 30 -10.3; 32 -10.1; 35 -9.9; 37 -9.8; 40 -9.5; 42 -9.4; 45 -9.2; 49 -9.0; 52 -8.9; 56 -8.7; 59 -8.6; 64 -8.4; 68 -8.3; 73 -8.1; 78 -8.0; 83 -7.9; 89 -7.8; 95 -7.7; 102 -7.5; 109 -7.3; 117 -7.1; 125 -6.9; 134 -6.7; 143 -6.5; 153 -6.2; 164 -6.0; 175 -5.6; 188 -5.3; 201 -5.1; 215 -4.7; 230 -4.3; 246 -4.1; 263 -3.7; 282 -3.3; 301 -3.0; 323 -2.7; 345 -2.3; 369 -2.0; 395 -1.7; 423 -1.2; 452 -1.0; 484 -0.8; 518 -0.5; 554 -0.2; 593 0.2; 635 0.4; 679 0.4; 726 0.5; 777 0.6; 832 0.5; 890 0.3; 952 -0.0; 1019 0.0; 1090 -0.5; 1167 -1.3; 1248 -1.2; 1336 -1.3; 1429 -1.6; 1529 -2.1; 1636 -2.6; 1751 -2.8; 1873 -2.9; 2004 -2.8; 2145 -2.8; 2295 -2.6; 2455 -2.1; 2627 -1.8; 2811 -1.2; 3008 -0.2; 3219 1.1; 3444 2.4; 3685 3.0; 3943 3.2; 4219 2.5; 4514 2.4; 4830 3.4; 5168 4.9; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.4; 15258 -1.5; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.079209687832979dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH1C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -10.6 dB |
| Peaking | 156 Hz   | 0.8  | -3.1 dB  |
| Peaking | 2076 Hz  | 1.57 | -3.4 dB  |
| Peaking | 3720 Hz  | 3.19 | 3.2 dB   |
| Peaking | 5783 Hz  | 3.08 | 6.6 dB   |
| Peaking | 312 Hz   | 1.76 | -0.7 dB  |
| Peaking | 817 Hz   | 0.98 | 1.6 dB   |
| Peaking | 1277 Hz  | 1.63 | -1.2 dB  |
| Peaking | 7340 Hz  | 4.29 | -1.0 dB  |
| Peaking | 15030 Hz | 5.48 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MH1C/Sony%20MH1C.png)