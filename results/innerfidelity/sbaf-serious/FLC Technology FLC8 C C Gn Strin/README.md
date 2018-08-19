# FLC Technology FLC8 C C Gn Strin

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.8; 49 5.5; 52 5.3; 56 5.1; 59 4.9; 64 4.6; 68 4.3; 73 4.0; 78 3.7; 83 3.4; 89 3.0; 95 2.6; 102 2.3; 109 2.1; 117 1.9; 125 1.6; 134 1.3; 143 1.1; 153 1.0; 164 0.8; 175 0.7; 188 0.6; 201 0.5; 215 0.5; 230 0.5; 246 0.4; 263 0.5; 282 0.6; 301 0.6; 323 0.7; 345 0.8; 369 0.9; 395 0.9; 423 1.2; 452 1.3; 484 1.3; 518 1.4; 554 1.6; 593 1.9; 635 1.9; 679 1.8; 726 1.6; 777 1.7; 832 1.7; 890 1.2; 952 0.6; 1019 -0.2; 1090 -0.9; 1167 -1.3; 1248 -1.5; 1336 -1.6; 1429 -1.4; 1529 -0.7; 1636 0.0; 1751 0.9; 1873 1.8; 2004 2.2; 2145 2.4; 2295 2.3; 2455 2.0; 2627 1.5; 2811 1.4; 3008 4.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.7; 4514 3.2; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.0; 6331 1.2; 6775 -4.4; 7249 -7.3; 7756 -6.7; 8299 -4.9; 8880 -4.1; 9502 -5.0; 10167 -6.1; 10879 -5.2; 11640 -2.4; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Gn Strin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.43 | 6.3 dB   |
| Peaking | 3523 Hz  | 2.19 | 6.0 dB   |
| Peaking | 5746 Hz  | 2.7  | 8.6 dB   |
| Peaking | 7238 Hz  | 2.85 | -10.5 dB |
| Peaking | 10303 Hz | 4.08 | -5.7 dB  |
| Peaking | 739 Hz   | 1.14 | 2.5 dB   |
| Peaking | 1326 Hz  | 1.44 | -3.5 dB  |
| Peaking | 1965 Hz  | 1.88 | 2.5 dB   |
| Peaking | 2732 Hz  | 8.95 | -2.3 dB  |
| Peaking | 12736 Hz | 6.16 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin.png)