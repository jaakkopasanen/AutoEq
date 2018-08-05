# Apple In-Ear 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.2; 22 1.3; 23 1.3; 25 1.3; 26 1.3; 28 1.4; 30 1.4; 32 1.4; 35 1.4; 37 1.5; 40 1.5; 42 1.5; 45 1.4; 49 1.4; 52 1.5; 56 1.5; 59 1.6; 64 1.5; 68 1.4; 73 1.4; 78 1.2; 83 0.9; 89 0.6; 95 0.1; 102 -0.4; 109 -0.9; 117 -1.4; 125 -2.0; 134 -2.5; 143 -2.8; 153 -3.0; 164 -3.1; 175 -3.2; 188 -3.3; 201 -3.2; 215 -3.1; 230 -3.1; 246 -3.0; 263 -2.9; 282 -2.8; 301 -2.7; 323 -2.6; 345 -2.4; 369 -2.3; 395 -2.1; 423 -1.8; 452 -1.7; 484 -1.6; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.2; 679 -0.2; 726 -0.1; 777 0.2; 832 0.2; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.2; 1336 -0.4; 1429 -0.6; 1529 -0.8; 1636 -0.8; 1751 -0.7; 1873 -0.4; 2004 -0.1; 2145 0.1; 2295 0.2; 2455 0.5; 2627 0.4; 2811 0.4; 3008 1.6; 3219 3.7; 3444 5.8; 3685 6.0; 3943 5.5; 4219 3.6; 4514 2.7; 4830 3.2; 5168 4.7; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple In-Ear 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.49 | 4.0 dB  |
| Peaking | 162 Hz  | 0.59 | -5.7 dB |
| Peaking | 7707 Hz | 1.95 | -1.9 dB |
| Peaking | 3638 Hz | 4.26 | 6.0 dB  |
| Peaking | 6003 Hz | 2.48 | 6.9 dB  |
| Peaking | 18 Hz   | 1.26 | 0.6 dB  |
| Peaking | 795 Hz  | 3.02 | 0.8 dB  |
| Peaking | 1625 Hz | 3.15 | -0.9 dB |
| Peaking | 2826 Hz | 6.85 | -0.9 dB |
| Peaking | 3276 Hz | 9.77 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20In-Ear%202013/Apple%20In-Ear%202013.png)