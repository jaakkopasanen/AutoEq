# Denon AH-D400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.7; 30 5.3; 32 4.8; 35 4.3; 37 4.0; 40 3.7; 42 3.4; 45 3.2; 49 2.8; 52 2.7; 56 2.4; 59 2.3; 64 2.0; 68 1.9; 73 1.6; 78 1.4; 83 1.2; 89 1.0; 95 0.6; 102 0.2; 109 -0.1; 117 -0.4; 125 -0.7; 134 -0.9; 143 -1.1; 153 -1.3; 164 -1.4; 175 -1.3; 188 -1.4; 201 -1.5; 215 -1.6; 230 -1.5; 246 -1.5; 263 -1.5; 282 -1.5; 301 -1.1; 323 -0.6; 345 -0.0; 369 0.8; 395 1.8; 423 2.9; 452 3.9; 484 4.6; 518 5.2; 554 5.7; 593 5.7; 635 5.2; 679 4.2; 726 3.3; 777 2.7; 832 1.8; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.3; 1167 -0.2; 1248 0.3; 1336 0.2; 1429 0.2; 1529 0.7; 1636 0.8; 1751 -0.1; 1873 0.2; 2004 0.9; 2145 1.3; 2295 1.6; 2455 1.8; 2627 2.1; 2811 2.0; 3008 2.7; 3219 3.4; 3444 5.7; 3685 6.0; 3943 5.4; 4219 4.8; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.7  | 6.1 dB  |
| Peaking | 73 Hz   | 1.11 | 1.2 dB  |
| Peaking | 400 Hz  | 0.36 | -3.9 dB |
| Peaking | 552 Hz  | 1.28 | 9.5 dB  |
| Peaking | 4539 Hz | 1.2  | 6.7 dB  |
| Peaking | 1038 Hz | 7.68 | -0.7 dB |
| Peaking | 3609 Hz | 6.78 | 2.0 dB  |
| Peaking | 4139 Hz | 6.66 | -1.7 dB |
| Peaking | 6318 Hz | 3.22 | 4.5 dB  |
| Peaking | 7385 Hz | 1.62 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D400/Denon%20AH-D400.png)