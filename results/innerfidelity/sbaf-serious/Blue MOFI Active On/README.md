# Blue MOFI Active On

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.8; 22 2.5; 23 2.4; 25 2.2; 26 2.1; 28 1.9; 30 1.8; 32 1.6; 35 1.5; 37 1.4; 40 1.3; 42 1.3; 45 1.3; 49 1.2; 52 1.2; 56 1.1; 59 1.1; 64 1.0; 68 0.9; 73 0.8; 78 0.7; 83 0.5; 89 0.3; 95 -0.1; 102 -0.5; 109 -0.6; 117 -0.7; 125 -1.0; 134 -1.5; 143 -2.1; 153 -2.4; 164 -1.9; 175 -1.6; 188 -2.2; 201 -2.2; 215 -2.0; 230 -1.5; 246 -1.0; 263 -0.4; 282 0.5; 301 1.0; 323 1.3; 345 1.2; 369 1.2; 395 1.1; 423 2.2; 452 3.3; 484 3.4; 518 3.1; 554 2.8; 593 2.8; 635 2.5; 679 2.1; 726 1.7; 777 1.5; 832 1.2; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.1; 1336 -0.2; 1429 -0.5; 1529 -0.6; 1636 -0.5; 1751 -0.3; 1873 0.3; 2004 1.2; 2145 1.9; 2295 2.3; 2455 2.4; 2627 3.3; 2811 3.7; 3008 4.1; 3219 4.3; 3444 5.0; 3685 5.6; 3943 3.7; 4219 -0.9; 4514 1.7; 4830 5.1; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.17 | 2.3 dB  |
| Peaking | 170 Hz  | 1.32 | -2.8 dB |
| Peaking | 504 Hz  | 1.62 | 3.5 dB  |
| Peaking | 3198 Hz | 2.42 | 4.7 dB  |
| Peaking | 5727 Hz | 3.2  | 6.4 dB  |
| Peaking | 719 Hz  | 4.61 | 0.5 dB  |
| Peaking | 1471 Hz | 2.57 | -1.1 dB |
| Peaking | 4232 Hz | 2.98 | 3.5 dB  |
| Peaking | 4222 Hz | 8.95 | -7.7 dB |
| Peaking | 8317 Hz | 3.7  | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On/Blue%20MOFI%20Active%20On.png)