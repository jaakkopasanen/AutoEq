# Denon AH-D2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.9; 45 5.8; 49 5.7; 52 5.7; 56 5.9; 59 6.0; 64 5.9; 68 5.8; 73 5.7; 78 5.6; 83 5.5; 89 5.3; 95 5.0; 102 4.7; 109 4.6; 117 4.3; 125 3.9; 134 3.5; 143 3.4; 153 3.3; 164 3.2; 175 3.4; 188 3.3; 201 3.3; 215 3.2; 230 3.2; 246 3.3; 263 3.3; 282 3.2; 301 3.2; 323 3.1; 345 3.0; 369 2.8; 395 2.6; 423 2.4; 452 2.0; 484 1.5; 518 1.0; 554 0.8; 593 0.7; 635 0.4; 679 -0.1; 726 0.0; 777 1.3; 832 0.7; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.6; 1429 0.6; 1529 0.6; 1636 0.7; 1751 1.0; 1873 1.3; 2004 1.8; 2145 2.1; 2295 2.3; 2455 2.8; 2627 3.1; 2811 3.8; 3008 5.7; 3219 5.5; 3444 3.5; 3685 2.5; 3943 2.1; 4219 2.1; 4514 2.5; 4830 2.7; 5168 3.1; 5530 3.0; 5917 1.9; 6331 1.4; 6775 1.1; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 40 Hz   |  0.2  | 6.2 dB  |
| Peaking | 319 Hz  |  1.03 | 3.3 dB  |
| Peaking | 269 Hz  |  0.5  | -1.9 dB |
| Peaking | 3020 Hz |  2.15 | 5.0 dB  |
| Peaking | 5320 Hz |  3.43 | 2.6 dB  |
| Peaking | 1 Hz    |  1.24 | -0.2 dB |
| Peaking | 310 Hz  |  4.18 | -0.1 dB |
| Peaking | 2712 Hz | 11.46 | -1.1 dB |
| Peaking | 2056 Hz |  2.9  | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)