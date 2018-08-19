# Sennheiser CX500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.1; 22 -7.1; 23 -7.1; 25 -7.2; 26 -7.2; 28 -7.2; 30 -7.2; 32 -7.2; 35 -7.3; 37 -7.3; 40 -7.4; 42 -7.4; 45 -7.5; 49 -7.7; 52 -7.8; 56 -8.0; 59 -8.1; 64 -8.2; 68 -8.4; 73 -8.6; 78 -8.8; 83 -8.9; 89 -9.0; 95 -9.2; 102 -9.2; 109 -9.4; 117 -9.3; 125 -9.4; 134 -9.5; 143 -9.5; 153 -9.5; 164 -9.5; 175 -9.3; 188 -9.2; 201 -9.0; 215 -8.8; 230 -8.5; 246 -8.3; 263 -8.0; 282 -7.6; 301 -7.2; 323 -6.8; 345 -6.3; 369 -5.7; 395 -5.3; 423 -4.9; 452 -4.6; 484 -4.2; 518 -3.6; 554 -3.1; 593 -2.6; 635 -2.0; 679 -1.6; 726 -1.1; 777 -0.7; 832 -0.4; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.2; 1336 0.2; 1429 0.0; 1529 -0.3; 1636 -0.4; 1751 -0.3; 1873 -0.1; 2004 0.3; 2145 0.7; 2295 1.4; 2455 2.1; 2627 3.0; 2811 3.9; 3008 4.9; 3219 5.8; 3444 6.0; 3685 6.0; 3943 5.2; 4219 3.3; 4514 1.6; 4830 0.2; 5168 -1.1; 5530 -3.9; 5917 -7.5; 6331 -5.2; 6775 -1.0; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -1.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230117dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.18 | -6.7 dB |
| Peaking | 147 Hz  | 0.64 | -5.0 dB |
| Peaking | 307 Hz  | 0.96 | -3.5 dB |
| Peaking | 3448 Hz | 2.09 | 6.7 dB  |
| Peaking | 5931 Hz | 5.97 | -9.0 dB |
| Peaking | 518 Hz  | 2.41 | -1.0 dB |
| Peaking | 1419 Hz | 0.5  | 1.3 dB  |
| Peaking | 1747 Hz | 1.8  | -1.9 dB |
| Peaking | 6249 Hz | 0.86 | -0.7 dB |
| Peaking | 7221 Hz | 6.15 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX500/Sennheiser%20CX500.png)