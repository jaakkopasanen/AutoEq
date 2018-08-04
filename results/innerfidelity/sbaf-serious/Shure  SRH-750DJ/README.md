# Shure  SRH-750DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.6; 40 5.1; 42 4.8; 45 4.4; 49 3.9; 52 3.7; 56 3.5; 59 3.3; 64 2.9; 68 2.5; 73 2.1; 78 1.6; 83 1.4; 89 1.2; 95 1.1; 102 1.3; 109 1.3; 117 0.9; 125 0.2; 134 -0.4; 143 -1.0; 153 -1.3; 164 -1.3; 175 -0.8; 188 -1.1; 201 -1.4; 215 -1.3; 230 -1.3; 246 -2.4; 263 -2.8; 282 -2.5; 301 -2.3; 323 -1.9; 345 -1.6; 369 -1.6; 395 -1.6; 423 -1.8; 452 -1.9; 484 -2.1; 518 -2.1; 554 -2.0; 593 -1.6; 635 -1.4; 679 -1.2; 726 -0.7; 777 -0.2; 832 0.1; 890 0.4; 952 0.4; 1019 -0.1; 1090 -0.3; 1167 -0.2; 1248 -0.0; 1336 -0.3; 1429 -1.1; 1529 -2.0; 1636 -2.9; 1751 -4.4; 1873 -5.8; 2004 -7.0; 2145 -7.8; 2295 -7.6; 2455 -6.0; 2627 -4.6; 2811 -2.4; 3008 -0.6; 3219 0.6; 3444 2.0; 3685 2.4; 3943 2.0; 4219 -0.2; 4514 -0.9; 4830 2.2; 5168 4.7; 5530 4.9; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -3.3; 8880 -6.0; 9502 -5.0; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure  SRH-750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.51 | 6.2 dB  |
| Peaking | 282 Hz  | 0.73 | -2.5 dB |
| Peaking | 2160 Hz | 2.93 | -8.7 dB |
| Peaking | 6003 Hz | 2.13 | 6.5 dB  |
| Peaking | 8921 Hz | 4.47 | -7.8 dB |
| Peaking | 560 Hz  | 3.33 | -1.0 dB |
| Peaking | 922 Hz  | 2.57 | 1.1 dB  |
| Peaking | 2621 Hz | 5.36 | -1.8 dB |
| Peaking | 3659 Hz | 2.54 | 2.8 dB  |
| Peaking | 4414 Hz | 7.85 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20%20SRH-750DJ/Shure%20%20SRH-750DJ.png)