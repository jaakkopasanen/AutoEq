# Bang Olufsen H6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.3; 22 2.0; 23 1.9; 25 1.7; 26 1.6; 28 1.5; 30 1.4; 32 1.3; 35 1.3; 37 1.3; 40 1.3; 42 1.4; 45 1.5; 49 1.8; 52 2.0; 56 2.4; 59 2.8; 64 3.2; 68 3.5; 73 3.7; 78 3.9; 83 4.2; 89 4.6; 95 4.9; 102 5.0; 109 4.6; 117 3.5; 125 2.1; 134 1.9; 143 3.0; 153 4.1; 164 5.8; 175 5.4; 188 3.5; 201 3.3; 215 3.6; 230 4.3; 246 4.8; 263 5.2; 282 5.5; 301 5.8; 323 5.8; 345 5.7; 369 5.7; 395 5.5; 423 5.4; 452 5.0; 484 4.5; 518 4.1; 554 3.9; 593 3.7; 635 3.1; 679 2.6; 726 2.1; 777 1.8; 832 1.1; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.2; 1336 -0.4; 1429 -0.6; 1529 -0.7; 1636 -0.8; 1751 -0.8; 1873 -0.3; 2004 0.1; 2145 1.0; 2295 2.2; 2455 4.2; 2627 4.8; 2811 4.2; 3008 5.0; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.1; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang Olufsen H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.57 | 2.0 dB  |
| Peaking | 90 Hz   |  0.93 | 4.0 dB  |
| Peaking | 296 Hz  |  1.13 | 4.6 dB  |
| Peaking | 479 Hz  |  1.86 | 2.7 dB  |
| Peaking | 4266 Hz |  1.21 | 7.0 dB  |
| Peaking | 168 Hz  | 11.53 | 3.0 dB  |
| Peaking | 1909 Hz |  1.35 | -3.1 dB |
| Peaking | 2579 Hz |  2.02 | 3.9 dB  |
| Peaking | 6224 Hz |  2.65 | 7.2 dB  |
| Peaking | 6660 Hz |  1.19 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20Olufsen%20H6/Bang%20Olufsen%20H6.png)