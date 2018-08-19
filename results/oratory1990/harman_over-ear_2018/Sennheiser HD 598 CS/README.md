# Sennheiser HD 598 CS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.3; 23 -1.4; 25 -1.6; 26 -1.6; 28 -1.8; 30 -1.9; 32 -2.0; 35 -2.1; 37 -2.1; 40 -2.1; 42 -2.1; 45 -2.1; 49 -2.0; 52 -1.9; 56 -1.8; 59 -1.7; 64 -1.6; 68 -1.7; 73 -1.6; 78 -1.3; 83 -1.2; 89 -1.2; 95 -1.2; 102 -1.1; 109 -0.9; 117 -0.9; 125 -1.1; 134 -1.3; 143 -1.6; 153 -1.8; 164 -1.9; 175 -1.6; 188 -0.8; 201 0.1; 215 0.7; 230 1.7; 246 2.7; 263 3.5; 282 4.3; 301 4.5; 323 4.4; 345 4.1; 369 3.7; 395 3.2; 423 2.5; 452 1.7; 484 1.4; 518 1.4; 554 1.4; 593 1.3; 635 1.3; 679 1.0; 726 0.8; 777 0.6; 832 0.3; 890 0.0; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.5; 1336 0.7; 1429 0.9; 1529 1.0; 1636 1.1; 1751 1.1; 1873 1.1; 2004 1.3; 2145 1.5; 2295 2.0; 2455 2.8; 2627 3.9; 2811 4.7; 3008 4.5; 3219 3.1; 3444 1.5; 3685 2.9; 3943 4.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.3; 18692 -2.3; 20000 -4.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099988076550725dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 CS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.58 | -2.1 dB |
| Peaking | 169 Hz  | 2    | -2.8 dB |
| Peaking | 305 Hz  | 1.39 | 5.0 dB  |
| Peaking | 2752 Hz | 3.49 | 3.6 dB  |
| Peaking | 5080 Hz | 1.81 | 6.7 dB  |
| Peaking | 1779 Hz | 1.93 | 0.6 dB  |
| Peaking | 4188 Hz | 7    | 2.5 dB  |
| Peaking | 5962 Hz | 0.82 | -1.8 dB |
| Peaking | 6391 Hz | 3.68 | 4.0 dB  |
| Peaking | 7467 Hz | 3.85 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20CS/Sennheiser%20HD%20598%20CS.png)