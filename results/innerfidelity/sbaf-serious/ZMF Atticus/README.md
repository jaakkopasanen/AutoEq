# ZMF Atticus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.8; 22 2.0; 23 1.7; 25 1.2; 26 1.0; 28 0.8; 30 0.5; 32 0.3; 35 -0.1; 37 -0.3; 40 -0.6; 42 -0.8; 45 -1.1; 49 -1.5; 52 -1.6; 56 -1.7; 59 -1.7; 64 -2.0; 68 -2.5; 73 -3.1; 78 -3.5; 83 -4.0; 89 -4.6; 95 -5.2; 102 -5.8; 109 -6.0; 117 -6.6; 125 -7.0; 134 -7.3; 143 -7.3; 153 -7.0; 164 -6.2; 175 -6.7; 188 -6.3; 201 -5.7; 215 -5.2; 230 -4.5; 246 -4.0; 263 -3.5; 282 -3.1; 301 -2.9; 323 -2.8; 345 -2.7; 369 -2.6; 395 -2.5; 423 -2.1; 452 -2.1; 484 -2.3; 518 -2.1; 554 -1.9; 593 -1.8; 635 -1.7; 679 -1.7; 726 -1.6; 777 -1.1; 832 -0.9; 890 -0.8; 952 -0.3; 1019 0.2; 1090 0.2; 1167 0.5; 1248 0.6; 1336 0.8; 1429 1.1; 1529 3.3; 1636 3.3; 1751 0.8; 1873 0.3; 2004 0.6; 2145 -0.2; 2295 -0.7; 2455 -0.3; 2627 0.2; 2811 0.6; 3008 1.1; 3219 1.1; 3444 2.0; 3685 3.7; 3943 4.9; 4219 4.9; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.8; 7249 0.3; 7756 -1.5; 8299 -2.3; 8880 -2.8; 9502 -2.2; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Atticus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 0.4  | 3.9 dB  |
| Peaking | 145 Hz  | 0.63 | -7.0 dB |
| Peaking | 1579 Hz | 8.8  | 4.0 dB  |
| Peaking | 5412 Hz | 1.44 | 7.5 dB  |
| Peaking | 8358 Hz | 2.65 | -5.3 dB |
| Peaking | 270 Hz  | 3.47 | 0.8 dB  |
| Peaking | 598 Hz  | 2.04 | -1.0 dB |
| Peaking | 2346 Hz | 5.8  | -1.5 dB |
| Peaking | 3813 Hz | 5.27 | 2.1 dB  |
| Peaking | 3362 Hz | 3.67 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Atticus/ZMF%20Atticus.png)