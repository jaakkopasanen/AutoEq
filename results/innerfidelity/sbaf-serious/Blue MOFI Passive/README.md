# Blue MOFI Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.6; 22 1.5; 23 1.5; 25 1.4; 26 1.3; 28 1.3; 30 1.2; 32 1.2; 35 1.1; 37 1.1; 40 1.1; 42 1.1; 45 1.1; 49 1.1; 52 1.0; 56 1.0; 59 1.0; 64 1.0; 68 0.9; 73 0.8; 78 0.7; 83 0.6; 89 0.4; 95 0.0; 102 -0.4; 109 -0.5; 117 -0.6; 125 -0.9; 134 -1.3; 143 -1.9; 153 -2.2; 164 -1.7; 175 -1.3; 188 -1.9; 201 -1.9; 215 -1.7; 230 -1.2; 246 -0.7; 263 -0.1; 282 0.8; 301 1.5; 323 1.8; 345 1.5; 369 1.4; 395 1.3; 423 2.3; 452 3.1; 484 3.3; 518 2.9; 554 2.6; 593 2.6; 635 2.5; 679 2.1; 726 1.6; 777 1.4; 832 1.2; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.1; 1248 -0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.6; 1751 -0.4; 1873 0.1; 2004 1.1; 2145 1.8; 2295 2.2; 2455 2.5; 2627 3.5; 2811 4.1; 3008 4.4; 3219 4.5; 3444 5.6; 3685 6.0; 3943 4.5; 4219 0.2; 4514 3.1; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.09 | 1.3 dB  |
| Peaking | 165 Hz  | 1.19 | -3.3 dB |
| Peaking | 494 Hz  | 1.55 | 3.1 dB  |
| Peaking | 3269 Hz | 2.32 | 5.0 dB  |
| Peaking | 5668 Hz | 2.96 | 6.3 dB  |
| Peaking | 221 Hz  | 5.79 | -0.6 dB |
| Peaking | 307 Hz  | 7    | 1.2 dB  |
| Peaking | 1750 Hz | 1.74 | -2.0 dB |
| Peaking | 2164 Hz | 2.45 | 1.9 dB  |
| Peaking | 8284 Hz | 4.72 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Passive/Blue%20MOFI%20Passive.png)