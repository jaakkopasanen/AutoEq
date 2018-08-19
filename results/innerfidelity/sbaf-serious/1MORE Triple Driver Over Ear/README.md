# 1MORE Triple Driver Over Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.8; 23 -1.0; 25 -1.4; 26 -1.7; 28 -2.0; 30 -2.4; 32 -2.7; 35 -3.0; 37 -3.2; 40 -3.4; 42 -3.5; 45 -3.6; 49 -3.7; 52 -3.8; 56 -3.8; 59 -3.6; 64 -3.3; 68 -3.1; 73 -3.1; 78 -3.6; 83 -4.2; 89 -4.2; 95 -3.9; 102 -3.5; 109 -3.6; 117 -3.7; 125 -3.7; 134 -3.5; 143 -3.1; 153 -2.6; 164 -1.9; 175 -1.6; 188 -1.0; 201 -0.6; 215 0.0; 230 0.7; 246 1.3; 263 1.8; 282 2.3; 301 2.6; 323 2.9; 345 3.0; 369 2.9; 395 2.6; 423 2.3; 452 1.6; 484 0.7; 518 -0.0; 554 -0.3; 593 -0.3; 635 -0.4; 679 -0.7; 726 -0.8; 777 -0.7; 832 -0.8; 890 -0.7; 952 -0.4; 1019 0.0; 1090 0.0; 1167 -0.0; 1248 0.2; 1336 0.2; 1429 0.1; 1529 0.2; 1636 0.4; 1751 1.0; 1873 1.3; 2004 1.7; 2145 1.9; 2295 2.3; 2455 3.0; 2627 3.3; 2811 3.2; 3008 2.8; 3219 2.6; 3444 2.4; 3685 0.9; 3943 -1.3; 4219 -1.4; 4514 -0.9; 4830 0.2; 5168 1.5; 5530 1.8; 5917 1.2; 6331 0.7; 6775 1.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.426501976879981dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver Over Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 160 Hz  | 0.21 | -5.0 dB |
| Peaking | 320 Hz  | 0.94 | 7.6 dB  |
| Peaking | 3000 Hz | 1.06 | 4.1 dB  |
| Peaking | 4190 Hz | 3.26 | -4.5 dB |
| Peaking | 5414 Hz | 3.55 | 1.5 dB  |
| Peaking | 18 Hz   | 0.93 | 1.4 dB  |
| Peaking | 36 Hz   | 0.83 | -0.8 dB |
| Peaking | 70 Hz   | 4.43 | 1.1 dB  |
| Peaking | 1012 Hz | 1.35 | -0.9 dB |
| Peaking | 1064 Hz | 2.65 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver%20Over%20Ear/1MORE%20Triple%20Driver%20Over%20Ear.png)