# MrSpeakers Alpha Prime

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.2; 22 -0.0; 23 -0.1; 25 -0.3; 26 -0.3; 28 -0.4; 30 -0.4; 32 -0.5; 35 -0.5; 37 -0.6; 40 -0.7; 42 -0.7; 45 -0.6; 49 -0.6; 52 -0.7; 56 -0.8; 59 -0.9; 64 -0.8; 68 -0.8; 73 -0.9; 78 -1.0; 83 -1.1; 89 -1.2; 95 -1.2; 102 -1.1; 109 -0.9; 117 -0.8; 125 -0.8; 134 -1.3; 143 -1.6; 153 -1.5; 164 -0.7; 175 -0.2; 188 -0.7; 201 -0.9; 215 -1.0; 230 -0.6; 246 -0.8; 263 -0.9; 282 -0.9; 301 -0.8; 323 -0.8; 345 -1.0; 369 -0.9; 395 -0.6; 423 0.0; 452 -0.2; 484 -0.7; 518 -0.8; 554 -0.3; 593 -0.0; 635 0.6; 679 1.1; 726 0.1; 777 -0.2; 832 -0.5; 890 -0.7; 952 -0.5; 1019 0.2; 1090 0.1; 1167 0.2; 1248 0.6; 1336 1.3; 1429 1.1; 1529 1.1; 1636 1.2; 1751 2.2; 1873 3.2; 2004 4.3; 2145 4.8; 2295 4.9; 2455 5.1; 2627 5.1; 2811 5.4; 3008 5.8; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 3.4; 4830 1.6; 5168 1.0; 5530 0.8; 5917 0.6; 6331 0.1; 6775 1.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230118dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Prime ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 0.32 | -1.0 dB |
| Peaking | 676 Hz   | 5.4  | 2.0 dB  |
| Peaking | 780 Hz   | 1.47 | -1.2 dB |
| Peaking | 3008 Hz  | 1.13 | 6.5 dB  |
| Peaking | 23211 Hz | 0.21 | -0.8 dB |
| Peaking | 2108 Hz  | 4.32 | 1.9 dB  |
| Peaking | 3346 Hz  | 1.01 | -1.5 dB |
| Peaking | 3615 Hz  | 3.37 | 1.4 dB  |
| Peaking | 4154 Hz  | 4.39 | 3.7 dB  |
| Peaking | 4793 Hz  | 2.4  | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Prime/MrSpeakers%20Alpha%20Prime.png)