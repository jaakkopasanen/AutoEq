# Sony MDR-V6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 5.3; 42 4.9; 45 4.4; 49 3.9; 52 3.6; 56 3.0; 59 2.7; 64 2.5; 68 2.6; 73 2.9; 78 2.7; 83 2.2; 89 1.9; 95 1.6; 102 1.4; 109 1.4; 117 1.3; 125 1.3; 134 1.3; 143 1.3; 153 1.3; 164 1.5; 175 1.7; 188 1.9; 201 2.0; 215 1.9; 230 1.2; 246 0.3; 263 0.4; 282 0.6; 301 0.9; 323 0.9; 345 0.5; 369 0.0; 395 -0.5; 423 -0.8; 452 -0.9; 484 -1.0; 518 -1.2; 554 -1.1; 593 -0.9; 635 -0.8; 679 -0.7; 726 -0.5; 777 -0.4; 832 -0.4; 890 -0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.8; 1336 -0.9; 1429 -1.2; 1529 -2.0; 1636 -2.4; 1751 -2.6; 1873 -2.7; 2004 -2.7; 2145 -3.0; 2295 -3.2; 2455 -3.2; 2627 -3.9; 2811 -4.8; 3008 -5.1; 3219 -5.0; 3444 -4.7; 3685 -3.8; 3943 -3.1; 4219 -4.6; 4514 -5.9; 4830 -4.7; 5168 -1.3; 5530 2.2; 5917 4.5; 6331 4.1; 6775 1.8; 7249 -0.1; 7756 -1.3; 8299 -3.0; 8880 -5.5; 9502 -7.5; 10167 -6.8; 10879 -2.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.21 | 6.6 dB  |
| Peaking | 2962 Hz  | 1    | -4.6 dB |
| Peaking | 4673 Hz  | 4.8  | -4.9 dB |
| Peaking | 5979 Hz  | 3.47 | 7.2 dB  |
| Peaking | 9543 Hz  | 4.01 | -8.2 dB |
| Peaking | 59 Hz    | 3.71 | -0.8 dB |
| Peaking | 200 Hz   | 3.16 | 1.5 dB  |
| Peaking | 518 Hz   | 2.47 | -1.3 dB |
| Peaking | 1024 Hz  | 4.24 | 0.8 dB  |
| Peaking | 11771 Hz | 7.01 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)