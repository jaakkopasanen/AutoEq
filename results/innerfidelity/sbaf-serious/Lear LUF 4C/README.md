# Lear LUF 4C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.5; 22 0.3; 23 0.3; 25 0.2; 26 0.1; 28 0.0; 30 -0.1; 32 -0.2; 35 -0.3; 37 -0.3; 40 -0.4; 42 -0.4; 45 -0.5; 49 -0.5; 52 -0.6; 56 -0.6; 59 -0.7; 64 -0.7; 68 -0.7; 73 -0.8; 78 -1.0; 83 -1.1; 89 -1.4; 95 -1.8; 102 -2.2; 109 -2.5; 117 -2.8; 125 -3.1; 134 -3.3; 143 -3.3; 153 -3.2; 164 -2.9; 175 -2.4; 188 -2.0; 201 -1.6; 215 -1.1; 230 -0.5; 246 -0.1; 263 0.3; 282 0.7; 301 1.0; 323 1.2; 345 1.5; 369 1.5; 395 1.6; 423 1.7; 452 1.8; 484 1.7; 518 1.7; 554 1.9; 593 2.0; 635 1.9; 679 1.7; 726 1.6; 777 1.6; 832 1.2; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -3.0; 1429 -4.0; 1529 -5.2; 1636 -6.0; 1751 -6.7; 1873 -7.2; 2004 -7.9; 2145 -8.5; 2295 -8.6; 2455 -7.7; 2627 -6.2; 2811 -4.3; 3008 -1.9; 3219 -0.4; 3444 0.4; 3685 1.0; 3943 1.5; 4219 3.4; 4514 6.0; 4830 3.8; 5168 -0.8; 5530 -4.2; 5917 -4.5; 6331 -2.2; 6775 -0.0; 7249 0.2; 7756 -1.1; 8299 -3.8; 8880 -6.2; 9502 -6.1; 10167 -3.8; 10879 -1.1; 11640 -0.0; 12455 0.0; 13327 -0.3; 14260 -0.1; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF 4C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 133 Hz  |  1.91 | -3.7 dB |
| Peaking | 2150 Hz |  1.83 | -9.7 dB |
| Peaking | 4681 Hz |  2.22 | 8.3 dB  |
| Peaking | 5566 Hz |  4.46 | -9.1 dB |
| Peaking | 9214 Hz |  4.43 | -7.3 dB |
| Peaking | 188 Hz  |  2.45 | -1.4 dB |
| Peaking | 557 Hz  |  0.64 | 2.4 dB  |
| Peaking | 1501 Hz |  3.15 | -2.4 dB |
| Peaking | 3283 Hz |  8.2  | 0.8 dB  |
| Peaking | 4050 Hz | 13.16 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF%204C/Lear%20LUF%204C.png)