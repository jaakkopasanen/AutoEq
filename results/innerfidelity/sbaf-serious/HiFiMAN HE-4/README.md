# HiFiMAN HE-4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 3.7; 22 3.4; 23 3.2; 25 3.0; 26 2.9; 28 2.7; 30 2.6; 32 2.5; 35 2.4; 37 2.3; 40 2.2; 42 2.2; 45 2.2; 49 2.2; 52 2.2; 56 2.2; 59 2.1; 64 2.1; 68 2.0; 73 2.0; 78 1.8; 83 1.6; 89 1.3; 95 1.2; 102 0.6; 109 0.3; 117 0.1; 125 -0.3; 134 -0.6; 143 -0.8; 153 -1.1; 164 -1.3; 175 -1.3; 188 -1.6; 201 -1.8; 215 -1.9; 230 -2.0; 246 -2.1; 263 -2.1; 282 -1.9; 301 -1.6; 323 -0.9; 345 -0.4; 369 -0.2; 395 -0.2; 423 -0.3; 452 -0.6; 484 -0.8; 518 -0.7; 554 -0.3; 593 -0.2; 635 -0.2; 679 1.2; 726 2.4; 777 2.5; 832 1.8; 890 1.3; 952 0.7; 1019 0.2; 1090 1.5; 1167 2.1; 1248 1.5; 1336 1.4; 1429 1.6; 1529 1.8; 1636 2.2; 1751 2.9; 1873 3.0; 2004 2.9; 2145 2.1; 2295 2.0; 2455 2.3; 2627 1.5; 2811 0.8; 3008 0.1; 3219 -1.0; 3444 -1.5; 3685 -2.0; 3943 -2.9; 4219 -4.5; 4514 -5.0; 4830 -4.2; 5168 1.8; 5530 3.3; 5917 -1.4; 6331 -5.4; 6775 -5.3; 7249 -5.1; 7756 -5.2; 8299 -6.8; 8880 -8.6; 9502 -8.1; 10167 -5.0; 10879 -2.3; 11640 -2.3; 12455 -4.2; 13327 -5.6; 14260 -5.2; 15258 -3.7; 16326 -2.9; 17469 -4.5; 18692 -8.1; 20000 -12.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.68 | 3.1 dB   |
| Peaking | 1827 Hz  | 1.11 | 2.8 dB   |
| Peaking | 4271 Hz  | 4.86 | -5.0 dB  |
| Peaking | 8754 Hz  | 2.11 | -7.7 dB  |
| Peaking | 27324 Hz | 0.73 | -13.3 dB |
| Peaking | 234 Hz   | 1.44 | -2.4 dB  |
| Peaking | 761 Hz   | 6.74 | 2.5 dB   |
| Peaking | 5479 Hz  | 9.52 | 6.6 dB   |
| Peaking | 6394 Hz  | 6.61 | -3.6 dB  |
| Peaking | 13590 Hz | 7.2  | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-4/HiFiMAN%20HE-4.png)