# Skullcandy Crusher

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.6; 22 5.1; 23 4.5; 25 3.2; 26 2.6; 28 1.5; 30 0.5; 32 -0.3; 35 -1.4; 37 -2.1; 40 -2.8; 42 -3.2; 45 -3.7; 49 -4.0; 52 -4.1; 56 -4.2; 59 -4.4; 64 -4.4; 68 -4.3; 73 -4.1; 78 -3.8; 83 -3.5; 89 -2.8; 95 -2.0; 102 -2.3; 109 -3.1; 117 -3.4; 125 -4.0; 134 -4.1; 143 -3.8; 153 -4.1; 164 -3.8; 175 -3.9; 188 -4.2; 201 -4.2; 215 -4.3; 230 -4.4; 246 -4.5; 263 -4.5; 282 -4.5; 301 -4.5; 323 -4.2; 345 -3.9; 369 -3.7; 395 -3.6; 423 -3.4; 452 -3.5; 484 -3.5; 518 -3.8; 554 -3.8; 593 -3.5; 635 -3.5; 679 -3.6; 726 -3.4; 777 -3.0; 832 -2.7; 890 -2.4; 952 -1.2; 1019 -0.2; 1090 1.0; 1167 2.0; 1248 1.1; 1336 1.0; 1429 -0.1; 1529 -1.4; 1636 -2.4; 1751 -2.4; 1873 -2.4; 2004 -2.8; 2145 -2.1; 2295 -2.0; 2455 -1.8; 2627 -0.9; 2811 -0.8; 3008 -0.3; 3219 -0.8; 3444 -0.7; 3685 -0.1; 3943 -1.1; 4219 -3.1; 4514 -0.2; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7237051549078615dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.58 | 7.3 dB  |
| Peaking | 51 Hz   | 1.12 | -4.2 dB |
| Peaking | 254 Hz  | 0.48 | -4.3 dB |
| Peaking | 672 Hz  | 2.82 | -1.8 dB |
| Peaking | 5757 Hz | 3.74 | 7.2 dB  |
| Peaking | 1223 Hz | 3.25 | 4.0 dB  |
| Peaking | 1810 Hz | 1.35 | -2.7 dB |
| Peaking | 4233 Hz | 7.93 | -4.3 dB |
| Peaking | 4927 Hz | 8.94 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher/Skullcandy%20Crusher.png)