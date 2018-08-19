# Sony MDR-EX600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.8; 28 5.5; 30 5.3; 32 5.1; 35 4.9; 37 4.7; 40 4.5; 42 4.3; 45 4.1; 49 3.9; 52 3.7; 56 3.4; 59 3.2; 64 2.9; 68 2.6; 73 2.3; 78 2.1; 83 1.8; 89 1.4; 95 1.0; 102 0.7; 109 0.6; 117 0.4; 125 0.1; 134 -0.1; 143 -0.3; 153 -0.5; 164 -0.7; 175 -0.8; 188 -0.9; 201 -1.0; 215 -1.1; 230 -1.1; 246 -1.1; 263 -1.1; 282 -0.9; 301 -0.9; 323 -0.9; 345 -0.7; 369 -0.6; 395 -0.6; 423 -0.4; 452 -0.2; 484 -0.2; 518 -0.1; 554 0.2; 593 0.6; 635 0.7; 679 0.7; 726 0.9; 777 1.0; 832 0.9; 890 0.7; 952 0.4; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.6; 1429 -2.2; 1529 -2.7; 1636 -3.1; 1751 -3.1; 1873 -2.7; 2004 -2.0; 2145 -1.0; 2295 0.3; 2455 2.1; 2627 3.8; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.3; 4514 2.8; 4830 -0.2; 5168 -3.5; 5530 -3.4; 5917 0.8; 6331 3.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.03 | 6.0 dB  |
| Peaking | 53 Hz    | 1.62 | 2.5 dB  |
| Peaking | 1760 Hz  | 2.24 | -4.4 dB |
| Peaking | 3257 Hz  | 1.99 | 7.4 dB  |
| Peaking | 24000 Hz | 2.35 | 1.1 dB  |
| Peaking | 242 Hz   | 1.1  | -1.3 dB |
| Peaking | 747 Hz   | 2.46 | 1.3 dB  |
| Peaking | 4176 Hz  | 6.32 | 3.2 dB  |
| Peaking | 5309 Hz  | 4.76 | -6.5 dB |
| Peaking | 6433 Hz  | 5.93 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX600/Sony%20MDR-EX600.png)