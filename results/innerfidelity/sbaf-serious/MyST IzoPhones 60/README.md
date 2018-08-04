# MyST IzoPhones 60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.6; 56 4.5; 59 3.7; 64 2.6; 68 1.9; 73 1.1; 78 0.5; 83 0.2; 89 -0.1; 95 -0.4; 102 -0.6; 109 -0.6; 117 -0.8; 125 -0.9; 134 -0.9; 143 -0.9; 153 -0.9; 164 -0.8; 175 -0.6; 188 -0.4; 201 -0.3; 215 -0.1; 230 0.2; 246 0.4; 263 0.6; 282 1.0; 301 1.3; 323 1.5; 345 1.0; 369 1.1; 395 1.0; 423 1.4; 452 1.2; 484 0.9; 518 1.0; 554 1.3; 593 1.8; 635 1.7; 679 1.3; 726 1.3; 777 1.4; 832 1.0; 890 0.6; 952 -0.1; 1019 0.2; 1090 0.5; 1167 -0.1; 1248 -0.1; 1336 -0.1; 1429 -0.6; 1529 -0.5; 1636 -0.8; 1751 0.8; 1873 1.6; 2004 2.6; 2145 2.8; 2295 3.1; 2455 4.0; 2627 4.3; 2811 3.4; 3008 2.3; 3219 1.8; 3444 1.1; 3685 0.2; 3943 -1.4; 4219 -3.4; 4514 -3.2; 4830 0.3; 5168 3.1; 5530 3.8; 5917 5.3; 6331 1.0; 6775 -3.0; 7249 -4.0; 7756 -4.6; 8299 -6.2; 8880 -7.5; 9502 -5.9; 10167 -1.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -0.8; 18692 -0.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST IzoPhones 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 1.02 | 7.1 dB  |
| Peaking | 2556 Hz  | 2.4  | 4.4 dB  |
| Peaking | 4320 Hz  | 6.54 | -5.0 dB |
| Peaking | 5707 Hz  | 5.06 | 6.7 dB  |
| Peaking | 8455 Hz  | 2.76 | -7.8 dB |
| Peaking | 52 Hz    | 3.29 | 2.7 dB  |
| Peaking | 136 Hz   | 0.62 | -2.4 dB |
| Peaking | 344 Hz   | 0.46 | 1.9 dB  |
| Peaking | 1473 Hz  | 3.05 | -1.6 dB |
| Peaking | 10905 Hz | 6.58 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MyST%20IzoPhones%2060/MyST%20IzoPhones%2060.png)