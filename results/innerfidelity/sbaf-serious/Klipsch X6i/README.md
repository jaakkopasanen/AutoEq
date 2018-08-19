# Klipsch X6i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 2.0; 22 1.9; 23 1.8; 25 1.6; 26 1.6; 28 1.4; 30 1.3; 32 1.2; 35 1.0; 37 1.0; 40 0.8; 42 0.7; 45 0.6; 49 0.3; 52 0.2; 56 -0.0; 59 -0.2; 64 -0.4; 68 -0.6; 73 -0.9; 78 -1.2; 83 -1.4; 89 -1.7; 95 -2.0; 102 -2.3; 109 -2.4; 117 -2.5; 125 -2.8; 134 -3.0; 143 -3.1; 153 -3.2; 164 -3.3; 175 -3.3; 188 -3.4; 201 -3.4; 215 -3.4; 230 -3.2; 246 -3.2; 263 -3.1; 282 -2.9; 301 -2.8; 323 -2.6; 345 -2.4; 369 -2.2; 395 -2.0; 423 -1.6; 452 -1.5; 484 -1.3; 518 -1.2; 554 -0.8; 593 -0.4; 635 -0.2; 679 -0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.8; 1751 -1.8; 1873 -1.6; 2004 -1.5; 2145 -1.3; 2295 -1.1; 2455 -0.7; 2627 -0.2; 2811 0.5; 3008 1.8; 3219 3.4; 3444 4.8; 3685 5.3; 3943 5.0; 4219 3.5; 4514 2.1; 4830 1.4; 5168 1.3; 5530 1.2; 5917 2.1; 6331 3.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.415647430524324dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X6i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.58 | 2.0 dB  |
| Peaking | 181 Hz  | 0.63 | -3.6 dB |
| Peaking | 1959 Hz | 1.78 | -2.1 dB |
| Peaking | 3670 Hz | 3    | 5.9 dB  |
| Peaking | 6610 Hz | 6.16 | 4.0 dB  |
| Peaking | 369 Hz  | 2.13 | -0.4 dB |
| Peaking | 803 Hz  | 2.17 | 1.1 dB  |
| Peaking | 1500 Hz | 5.14 | -0.6 dB |
| Peaking | 8065 Hz | 4.57 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X6i/Klipsch%20X6i.png)