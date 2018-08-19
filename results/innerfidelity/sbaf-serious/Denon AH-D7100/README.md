# Denon AH-D7100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.6; 22 -4.7; 23 -4.7; 25 -4.7; 26 -4.7; 28 -4.6; 30 -4.6; 32 -4.5; 35 -4.4; 37 -4.3; 40 -4.1; 42 -4.0; 45 -3.7; 49 -3.3; 52 -3.0; 56 -2.6; 59 -2.6; 64 -2.9; 68 -3.3; 73 -3.7; 78 -4.0; 83 -4.2; 89 -4.8; 95 -5.4; 102 -5.6; 109 -5.6; 117 -5.5; 125 -5.5; 134 -5.4; 143 -5.3; 153 -4.9; 164 -3.6; 175 -3.7; 188 -3.2; 201 -2.2; 215 -0.9; 230 0.8; 246 2.4; 263 4.1; 282 5.8; 301 6.0; 323 6.0; 345 6.0; 369 5.9; 395 5.4; 423 5.1; 452 4.6; 484 4.1; 518 3.7; 554 3.4; 593 3.1; 635 2.5; 679 1.9; 726 1.4; 777 1.2; 832 0.8; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.1; 1529 -2.9; 1636 -3.6; 1751 -3.7; 1873 -3.6; 2004 -3.2; 2145 -2.2; 2295 -0.7; 2455 1.6; 2627 2.3; 2811 2.0; 3008 1.8; 3219 2.4; 3444 4.2; 3685 5.9; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.3; 5917 3.0; 6331 2.6; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -3.6; 9502 -3.5; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.9; 17469 -5.4; 18692 -4.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.94 | -4.5 dB |
| Peaking | 141 Hz   | 0.69 | -7.0 dB |
| Peaking | 323 Hz   | 1.2  | 9.4 dB  |
| Peaking | 4518 Hz  | 2.07 | 7.1 dB  |
| Peaking | 17859 Hz | 2.7  | -6.3 dB |
| Peaking | 578 Hz   | 2.82 | 1.3 dB  |
| Peaking | 1889 Hz  | 1.68 | -5.5 dB |
| Peaking | 2564 Hz  | 2.43 | 3.2 dB  |
| Peaking | 8233 Hz  | 0.9  | 1.6 dB  |
| Peaking | 9152 Hz  | 4.63 | -6.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)