# Shure SE535

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.7; 22 4.6; 23 4.6; 25 4.5; 26 4.5; 28 4.4; 30 4.3; 32 4.3; 35 4.2; 37 4.2; 40 4.1; 42 4.1; 45 4.0; 49 4.0; 52 3.9; 56 3.9; 59 3.8; 64 3.7; 68 3.5; 73 3.4; 78 3.2; 83 3.0; 89 2.6; 95 2.1; 102 1.5; 109 1.0; 117 0.5; 125 -0.2; 134 -0.7; 143 -1.0; 153 -1.3; 164 -1.5; 175 -1.6; 188 -1.6; 201 -1.7; 215 -1.7; 230 -1.7; 246 -1.7; 263 -1.6; 282 -1.5; 301 -1.4; 323 -1.4; 345 -1.3; 369 -1.2; 395 -1.0; 423 -0.8; 452 -0.8; 484 -0.7; 518 -0.6; 554 -0.3; 593 0.0; 635 0.1; 679 0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.7; 1529 -0.9; 1636 -0.9; 1751 -0.9; 1873 -0.7; 2004 -0.5; 2145 -0.2; 2295 0.6; 2455 2.1; 2627 3.3; 2811 4.4; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.34 | 4.5 dB  |
| Peaking | 80 Hz   | 0.91 | 2.9 dB  |
| Peaking | 166 Hz  | 0.65 | -3.0 dB |
| Peaking | 1872 Hz | 1.84 | -3.0 dB |
| Peaking | 3972 Hz | 0.96 | 7.1 dB  |
| Peaking | 774 Hz  | 3.66 | 0.6 dB  |
| Peaking | 3063 Hz | 3.83 | 2.2 dB  |
| Peaking | 3601 Hz | 1.41 | -1.4 dB |
| Peaking | 6252 Hz | 2.51 | 5.0 dB  |
| Peaking | 7457 Hz | 1.57 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE535/Shure%20SE535.png)