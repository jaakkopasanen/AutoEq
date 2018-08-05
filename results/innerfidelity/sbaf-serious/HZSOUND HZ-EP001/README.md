# HZSOUND HZ-EP001

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.5; 22 -2.5; 23 -2.5; 25 -2.5; 26 -2.5; 28 -2.5; 30 -2.4; 32 -2.4; 35 -2.3; 37 -2.2; 40 -2.1; 42 -2.0; 45 -2.0; 49 -1.9; 52 -1.7; 56 -1.6; 59 -1.5; 64 -1.5; 68 -1.4; 73 -1.4; 78 -1.4; 83 -1.6; 89 -1.8; 95 -2.1; 102 -2.6; 109 -2.9; 117 -3.3; 125 -3.8; 134 -4.2; 143 -4.4; 153 -4.6; 164 -4.7; 175 -4.6; 188 -4.6; 201 -4.5; 215 -4.4; 230 -4.3; 246 -4.2; 263 -4.1; 282 -3.9; 301 -3.9; 323 -3.8; 345 -3.7; 369 -3.9; 395 -4.0; 423 -1.1; 452 -1.3; 484 -1.7; 518 -1.7; 554 -1.4; 593 -1.0; 635 -0.9; 679 -0.7; 726 -0.3; 777 -0.1; 832 0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.3; 1336 0.1; 1429 0.1; 1529 -0.0; 1636 0.0; 1751 0.3; 1873 0.8; 2004 1.2; 2145 1.5; 2295 2.0; 2455 2.9; 2627 3.0; 2811 3.2; 3008 3.2; 3219 3.4; 3444 2.8; 3685 1.2; 3943 0.7; 4219 0.1; 4514 2.4; 4830 3.2; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ-EP001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.81 | -2.5 dB |
| Peaking | 170 Hz  | 0.94 | -4.5 dB |
| Peaking | 342 Hz  | 1.85 | -2.5 dB |
| Peaking | 2779 Hz | 2.35 | 3.3 dB  |
| Peaking | 5760 Hz | 3.24 | 6.6 dB  |
| Peaking | 250 Hz  | 4.3  | -0.8 dB |
| Peaking | 260 Hz  | 2.14 | 0.5 dB  |
| Peaking | 4335 Hz | 2.12 | 1.6 dB  |
| Peaking | 4138 Hz | 5.96 | -3.3 dB |
| Peaking | 8266 Hz | 3.76 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ-EP001/HZSOUND%20HZ-EP001.png)