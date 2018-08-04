# Status SM-OB1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.3; 37 4.8; 40 4.3; 42 4.0; 45 3.6; 49 3.1; 52 2.8; 56 2.5; 59 2.3; 64 2.0; 68 1.8; 73 1.6; 78 1.6; 83 1.6; 89 1.3; 95 0.8; 102 0.4; 109 -0.1; 117 -0.6; 125 -1.2; 134 -1.6; 143 -1.8; 153 -1.8; 164 -1.7; 175 -1.7; 188 -1.7; 201 -1.6; 215 -1.4; 230 -1.0; 246 -0.7; 263 -0.4; 282 -1.0; 301 -1.2; 323 -1.0; 345 -0.8; 369 -0.5; 395 -0.5; 423 -0.4; 452 -0.4; 484 -0.5; 518 -0.5; 554 -0.4; 593 -0.2; 635 -0.2; 679 -0.3; 726 -0.1; 777 -0.1; 832 -0.2; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.6; 1167 1.2; 1248 1.3; 1336 1.2; 1429 1.5; 1529 1.7; 1636 2.2; 1751 3.0; 1873 3.4; 2004 3.6; 2145 3.5; 2295 3.5; 2455 3.8; 2627 4.3; 2811 4.9; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-OB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.52 | 6.2 dB  |
| Peaking | 153 Hz  | 1.61 | -2.3 dB |
| Peaking | 334 Hz  | 0.93 | -0.7 dB |
| Peaking | 875 Hz  | 3.64 | -0.6 dB |
| Peaking | 3821 Hz | 0.81 | 6.6 dB  |
| Peaking | 304 Hz  | 6.81 | -0.3 dB |
| Peaking | 1867 Hz | 5.55 | 1.1 dB  |
| Peaking | 3866 Hz | 4.25 | -0.6 dB |
| Peaking | 6184 Hz | 2.39 | 5.5 dB  |
| Peaking | 7412 Hz | 1.44 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-OB1/Status%20SM-OB1.png)