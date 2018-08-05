# MrSpeakers Alpha Prime

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.2; 22 0.0; 23 -0.1; 25 -0.2; 26 -0.3; 28 -0.4; 30 -0.4; 32 -0.4; 35 -0.5; 37 -0.5; 40 -0.5; 42 -0.5; 45 -0.5; 49 -0.4; 52 -0.4; 56 -0.5; 59 -0.4; 64 -0.3; 68 -0.2; 73 -0.2; 78 -0.2; 83 -0.3; 89 -0.4; 95 -0.5; 102 -0.5; 109 -0.5; 117 -0.6; 125 -0.8; 134 -1.4; 143 -1.8; 153 -1.7; 164 -1.0; 175 -0.4; 188 -0.9; 201 -1.0; 215 -1.1; 230 -0.8; 246 -0.9; 263 -1.0; 282 -1.0; 301 -0.9; 323 -0.9; 345 -1.0; 369 -0.9; 395 -0.6; 423 0.0; 452 -0.2; 484 -0.7; 518 -0.8; 554 -0.3; 593 -0.0; 635 0.6; 679 1.1; 726 0.1; 777 -0.2; 832 -0.5; 890 -0.7; 952 -0.5; 1019 0.2; 1090 0.1; 1167 0.2; 1248 0.6; 1336 1.3; 1429 1.1; 1529 1.1; 1636 1.2; 1751 2.2; 1873 3.2; 2004 4.3; 2145 4.8; 2295 4.9; 2455 5.1; 2627 5.1; 2811 5.4; 3008 5.8; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 3.4; 4830 1.6; 5168 1.0; 5530 0.8; 5917 0.6; 6331 0.1; 6775 1.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Prime ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 145 Hz   |  5.32 | -1.3 dB |
| Peaking | 287 Hz   |  0.08 | -0.5 dB |
| Peaking | 272 Hz   |  1.76 | -0.6 dB |
| Peaking | 3253 Hz  |  0.96 | 7.0 dB  |
| Peaking | 41318 Hz |  1.72 | -1.9 dB |
| Peaking | 669 Hz   |  6.17 | 1.8 dB  |
| Peaking | 840 Hz   |  1.43 | -0.8 dB |
| Peaking | 2087 Hz  |  7.12 | 1.5 dB  |
| Peaking | 5054 Hz  |  5.74 | -1.8 dB |
| Peaking | 7014 Hz  | 10.12 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Prime/MrSpeakers%20Alpha%20Prime.png)