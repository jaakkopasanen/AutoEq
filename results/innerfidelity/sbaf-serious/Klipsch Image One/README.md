# Klipsch Image One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.6; 45 5.1; 49 4.5; 52 4.1; 56 3.6; 59 3.3; 64 2.9; 68 2.5; 73 2.0; 78 1.4; 83 0.8; 89 0.3; 95 -0.2; 102 -0.7; 109 -0.9; 117 -1.2; 125 -1.7; 134 -1.9; 143 -2.0; 153 -2.2; 164 -2.2; 175 -2.2; 188 -2.4; 201 -2.3; 215 -2.2; 230 -1.9; 246 -1.7; 263 -1.7; 282 -1.6; 301 -1.5; 323 -1.5; 345 -1.2; 369 -1.0; 395 -0.9; 423 -0.7; 452 -0.5; 484 -0.4; 518 -0.1; 554 0.5; 593 1.2; 635 1.7; 679 1.7; 726 1.3; 777 1.5; 832 1.1; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -1.8; 1429 -2.2; 1529 -2.4; 1636 -2.8; 1751 -3.2; 1873 -3.5; 2004 -3.7; 2145 -4.0; 2295 -4.1; 2455 -4.3; 2627 -4.8; 2811 -5.3; 3008 -4.9; 3219 -4.2; 3444 -2.9; 3685 -1.0; 3943 0.9; 4219 2.4; 4514 2.6; 4830 3.1; 5168 3.8; 5530 2.6; 5917 1.0; 6331 -0.8; 6775 -2.8; 7249 -1.9; 7756 -0.3; 8299 -0.2; 8880 -1.2; 9502 -1.4; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.53 | 6.5 dB  |
| Peaking | 153 Hz  | 0.88 | -3.2 dB |
| Peaking | 2821 Hz | 1.16 | -6.5 dB |
| Peaking | 4719 Hz | 1.72 | 6.3 dB  |
| Peaking | 6817 Hz | 4.51 | -4.0 dB |
| Peaking | 451 Hz  | 1.03 | -1.0 dB |
| Peaking | 681 Hz  | 1.63 | 2.8 dB  |
| Peaking | 1508 Hz | 2.48 | -1.0 dB |
| Peaking | 8358 Hz | 3.33 | 0.9 dB  |
| Peaking | 9153 Hz | 5.72 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)