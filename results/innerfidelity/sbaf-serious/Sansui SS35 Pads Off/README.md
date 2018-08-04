# Sansui SS35 Pads Off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.6; 59 5.3; 64 4.9; 68 4.7; 73 4.5; 78 4.4; 83 4.2; 89 4.0; 95 3.6; 102 3.5; 109 3.3; 117 3.0; 125 2.8; 134 2.6; 143 2.4; 153 2.3; 164 2.4; 175 2.9; 188 2.8; 201 3.0; 215 3.5; 230 4.1; 246 4.4; 263 4.5; 282 4.6; 301 4.3; 323 3.7; 345 2.9; 369 2.4; 395 1.9; 423 1.7; 452 1.6; 484 1.4; 518 1.5; 554 2.1; 593 2.8; 635 3.2; 679 3.2; 726 3.2; 777 2.9; 832 2.2; 890 1.4; 952 0.6; 1019 -0.2; 1090 -0.6; 1167 -0.8; 1248 -0.6; 1336 -0.3; 1429 0.5; 1529 1.9; 1636 2.9; 1751 3.8; 1873 4.5; 2004 4.0; 2145 2.2; 2295 1.3; 2455 2.6; 2627 5.2; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 Pads Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.35 | 6.2 dB  |
| Peaking | 273 Hz  | 1.8  | 4.0 dB  |
| Peaking | 680 Hz  | 3.38 | 3.1 dB  |
| Peaking | 3356 Hz | 1.2  | 6.0 dB  |
| Peaking | 5648 Hz | 2.91 | 4.5 dB  |
| Peaking | 1252 Hz | 2.78 | -2.8 dB |
| Peaking | 1917 Hz | 1.84 | 3.6 dB  |
| Peaking | 2282 Hz | 5.49 | -4.5 dB |
| Peaking | 6548 Hz | 6.47 | 2.5 dB  |
| Peaking | 7693 Hz | 1.86 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35%20Pads%20Off/Sansui%20SS35%20Pads%20Off.png)