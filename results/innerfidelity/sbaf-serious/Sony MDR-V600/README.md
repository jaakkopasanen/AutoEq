# Sony MDR-V600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.8; 45 5.2; 49 4.3; 52 3.6; 56 2.9; 59 2.4; 64 1.9; 68 1.7; 73 1.1; 78 0.2; 83 -0.4; 89 -0.9; 95 -1.1; 102 -0.8; 109 -0.2; 117 -0.2; 125 -1.1; 134 -1.8; 143 -2.6; 153 -3.1; 164 -2.8; 175 -2.7; 188 -2.8; 201 -3.3; 215 -3.7; 230 -3.8; 246 -3.9; 263 -3.9; 282 -3.7; 301 -3.6; 323 -3.4; 345 -3.2; 369 -3.0; 395 -3.2; 423 -3.4; 452 -3.5; 484 -2.9; 518 -2.5; 554 -2.5; 593 -1.9; 635 -0.8; 679 -1.0; 726 -1.4; 777 -1.0; 832 -0.9; 890 -0.8; 952 -0.4; 1019 0.2; 1090 0.7; 1167 1.3; 1248 1.9; 1336 2.2; 1429 2.0; 1529 1.4; 1636 1.0; 1751 1.1; 1873 1.7; 2004 2.7; 2145 3.8; 2295 4.7; 2455 5.4; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.3; 3685 4.4; 3943 4.1; 4219 2.1; 4514 2.5; 4830 4.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -2.0; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.75 | 6.9 dB  |
| Peaking | 226 Hz  | 0.63 | -3.8 dB |
| Peaking | 465 Hz  | 2.35 | -1.5 dB |
| Peaking | 2826 Hz | 1.44 | 6.2 dB  |
| Peaking | 5763 Hz | 3.51 | 5.8 dB  |
| Peaking | 90 Hz   | 3.92 | -1.3 dB |
| Peaking | 113 Hz  | 6.81 | 1.5 dB  |
| Peaking | 1313 Hz | 4.56 | 1.8 dB  |
| Peaking | 1741 Hz | 5.52 | -1.1 dB |
| Peaking | 9340 Hz | 5.46 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V600/Sony%20MDR-V600.png)