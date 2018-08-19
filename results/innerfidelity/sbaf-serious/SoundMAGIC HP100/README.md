# SoundMAGIC HP100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.2; 22 0.3; 23 -0.1; 25 -0.8; 26 -1.1; 28 -1.6; 30 -2.0; 32 -2.3; 35 -2.5; 37 -2.7; 40 -2.8; 42 -2.9; 45 -2.9; 49 -3.0; 52 -2.9; 56 -2.8; 59 -2.7; 64 -2.3; 68 -1.8; 73 -1.4; 78 -1.4; 83 -0.8; 89 0.6; 95 1.6; 102 2.3; 109 2.4; 117 2.0; 125 1.3; 134 0.5; 143 0.4; 153 1.7; 164 4.7; 175 4.1; 188 1.6; 201 0.5; 215 -0.5; 230 -1.0; 246 -1.3; 263 -1.5; 282 -1.4; 301 -1.3; 323 -1.2; 345 -1.2; 369 -1.1; 395 -1.1; 423 -0.9; 452 -0.9; 484 -1.0; 518 -1.0; 554 -0.9; 593 -0.6; 635 -0.5; 679 -0.6; 726 -0.5; 777 -0.2; 832 -0.3; 890 -0.1; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.3; 1248 -0.3; 1336 -0.5; 1429 -0.8; 1529 -1.1; 1636 -1.4; 1751 -1.2; 1873 -1.3; 2004 -1.5; 2145 -1.7; 2295 -1.8; 2455 -1.5; 2627 -1.1; 2811 -1.0; 3008 0.4; 3219 1.0; 3444 1.0; 3685 0.1; 3943 -0.8; 4219 -1.4; 4514 -0.5; 4830 3.2; 5168 4.2; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.3; 8299 -4.9; 8880 -6.5; 9502 -5.9; 10167 -3.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.063866194336636dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC HP100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 94 Hz   | 0.36 | -4.1 dB |
| Peaking | 105 Hz  | 2    | 6.2 dB  |
| Peaking | 170 Hz  | 4.36 | 7.0 dB  |
| Peaking | 6047 Hz | 3.18 | 7.3 dB  |
| Peaking | 8931 Hz | 3.78 | -8.1 dB |
| Peaking | 148 Hz  | 8.95 | -0.6 dB |
| Peaking | 2238 Hz | 1.61 | -1.9 dB |
| Peaking | 3315 Hz | 4.57 | 1.9 dB  |
| Peaking | 4408 Hz | 4.33 | -3.4 dB |
| Peaking | 4918 Hz | 6.1  | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP100/SoundMAGIC%20HP100.png)