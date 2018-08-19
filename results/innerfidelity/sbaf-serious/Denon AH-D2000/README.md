# Denon AH-D2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.7; 45 5.6; 49 5.5; 52 5.5; 56 5.6; 59 5.6; 64 5.4; 68 5.2; 73 5.0; 78 4.9; 83 4.7; 89 4.5; 95 4.3; 102 4.2; 109 4.2; 117 4.1; 125 3.9; 134 3.7; 143 3.6; 153 3.5; 164 3.4; 175 3.6; 188 3.6; 201 3.5; 215 3.3; 230 3.3; 246 3.4; 263 3.4; 282 3.3; 301 3.3; 323 3.1; 345 3.0; 369 2.8; 395 2.6; 423 2.4; 452 2.0; 484 1.5; 518 1.0; 554 0.8; 593 0.7; 635 0.4; 679 -0.1; 726 0.0; 777 1.3; 832 0.7; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.6; 1429 0.6; 1529 0.6; 1636 0.7; 1751 1.0; 1873 1.3; 2004 1.8; 2145 2.1; 2295 2.3; 2455 2.8; 2627 3.1; 2811 3.8; 3008 5.7; 3219 5.5; 3444 3.5; 3685 2.5; 3943 2.1; 4219 2.1; 4514 2.5; 4830 2.7; 5168 3.1; 5530 3.0; 5917 1.9; 6331 1.4; 6775 1.1; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.17 | 6.0 dB  |
| Peaking | 283 Hz  | 2.81 | -1.5 dB |
| Peaking | 291 Hz  | 1.43 | 3.5 dB  |
| Peaking | 3025 Hz | 2.26 | 5.0 dB  |
| Peaking | 5314 Hz | 3.39 | 2.7 dB  |
| Peaking | 678 Hz  | 7.49 | -0.8 dB |
| Peaking | 2039 Hz | 6.47 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)