# AudioFly AF140

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.2; 22 -3.5; 23 -3.6; 25 -3.8; 26 -3.9; 28 -4.1; 30 -4.2; 32 -4.4; 35 -4.6; 37 -4.7; 40 -4.9; 42 -5.0; 45 -5.2; 49 -5.4; 52 -5.5; 56 -5.7; 59 -5.9; 64 -6.0; 68 -6.3; 73 -6.5; 78 -6.8; 83 -6.9; 89 -7.2; 95 -7.4; 102 -7.6; 109 -7.6; 117 -7.7; 125 -7.8; 134 -7.9; 143 -8.0; 153 -8.0; 164 -7.9; 175 -7.8; 188 -7.7; 201 -7.5; 215 -7.3; 230 -7.1; 246 -6.8; 263 -6.5; 282 -6.2; 301 -5.8; 323 -5.4; 345 -5.0; 369 -4.6; 395 -4.2; 423 -3.5; 452 -3.0; 484 -2.9; 518 -2.4; 554 -1.8; 593 -1.0; 635 -0.4; 679 -0.1; 726 1.1; 777 1.5; 832 1.4; 890 1.1; 952 0.8; 1019 0.0; 1090 -0.5; 1167 -1.1; 1248 -1.7; 1336 -2.5; 1429 -3.3; 1529 -4.0; 1636 -4.6; 1751 -5.1; 1873 -5.4; 2004 -5.3; 2145 -5.1; 2295 -5.0; 2455 -4.0; 2627 -2.6; 2811 -1.0; 3008 1.3; 3219 3.2; 3444 4.6; 3685 4.9; 3943 5.9; 4219 6.0; 4514 6.0; 4830 4.4; 5168 0.6; 5530 -1.1; 5917 2.3; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -2.5; 10879 -2.8; 11640 -1.0; 12455 -0.0; 13327 -0.8; 14260 -3.1; 15258 -4.0; 16326 -1.8; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099997742310093dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF140 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 71 Hz    | 0.37 | -5.8 dB |
| Peaking | 209 Hz   | 0.84 | -4.8 dB |
| Peaking | 2093 Hz  | 1.74 | -6.9 dB |
| Peaking | 3686 Hz  | 1.88 | 6.0 dB  |
| Peaking | 4431 Hz  | 4.85 | 3.0 dB  |
| Peaking | 807 Hz   | 0.7  | -2.7 dB |
| Peaking | 813 Hz   | 1.62 | 5.5 dB  |
| Peaking | 6480 Hz  | 9.51 | 5.1 dB  |
| Peaking | 10594 Hz | 6.21 | -3.3 dB |
| Peaking | 15049 Hz | 3.86 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF140/AudioFly%20AF140.png)