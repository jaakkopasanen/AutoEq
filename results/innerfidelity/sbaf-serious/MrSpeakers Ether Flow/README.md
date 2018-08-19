# MrSpeakers Ether Flow

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 1.9; 22 1.8; 23 1.8; 25 1.9; 26 2.1; 28 2.4; 30 2.7; 32 3.0; 35 3.2; 37 3.1; 40 2.7; 42 2.3; 45 1.5; 49 0.8; 52 0.9; 56 1.0; 59 0.6; 64 -0.1; 68 -0.4; 73 -0.9; 78 -1.0; 83 -1.5; 89 -2.2; 95 -2.5; 102 -2.8; 109 -2.9; 117 -2.9; 125 -3.1; 134 -3.1; 143 -3.2; 153 -3.0; 164 -2.8; 175 -3.4; 188 -3.3; 201 -3.2; 215 -3.1; 230 -2.9; 246 -2.7; 263 -2.4; 282 -1.9; 301 -1.5; 323 -1.2; 345 -0.8; 369 -0.4; 395 0.1; 423 0.5; 452 0.8; 484 1.0; 518 1.2; 554 1.4; 593 1.8; 635 2.0; 679 1.8; 726 1.4; 777 1.5; 832 1.2; 890 1.1; 952 0.9; 1019 -0.1; 1090 0.9; 1167 2.8; 1248 2.7; 1336 2.3; 1429 1.7; 1529 0.7; 1636 0.1; 1751 -0.2; 1873 -0.6; 2004 -0.5; 2145 0.1; 2295 0.4; 2455 1.0; 2627 1.9; 2811 1.4; 3008 0.9; 3219 0.6; 3444 0.3; 3685 0.4; 3943 0.5; 4219 0.1; 4514 -0.3; 4830 0.3; 5168 1.1; 5530 1.2; 5917 0.6; 6331 -1.3; 6775 -0.8; 7249 -0.1; 7756 0.2; 8299 -0.2; 8880 -0.7; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.291980837799393dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.83 | 3.7 dB  |
| Peaking | 156 Hz  | 0.45 | -3.8 dB |
| Peaking | 555 Hz  | 1.12 | 2.8 dB  |
| Peaking | 1252 Hz | 5.38 | 2.7 dB  |
| Peaking | 2729 Hz | 5.36 | 1.8 dB  |
| Peaking | 760 Hz  | 4.41 | 0.2 dB  |
| Peaking | 1896 Hz | 6.49 | -1.0 dB |
| Peaking | 5649 Hz | 5.02 | 1.9 dB  |
| Peaking | 6366 Hz | 6.34 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)