# MrSpeakers Alpha Dog 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 0.3; 22 0.1; 23 0.1; 25 -0.0; 26 -0.1; 28 -0.2; 30 -0.2; 32 -0.2; 35 -0.1; 37 -0.0; 40 0.1; 42 0.2; 45 0.3; 49 0.4; 52 0.6; 56 1.0; 59 0.8; 64 0.6; 68 1.1; 73 1.7; 78 1.8; 83 1.5; 89 1.1; 95 0.7; 102 0.5; 109 0.5; 117 0.3; 125 -0.0; 134 -0.3; 143 -0.6; 153 -0.5; 164 -0.5; 175 -1.8; 188 -2.2; 201 -2.4; 215 -2.5; 230 -2.8; 246 -2.9; 263 -2.9; 282 -2.9; 301 -2.8; 323 -2.9; 345 -2.6; 369 -1.7; 395 -1.5; 423 -1.7; 452 -1.7; 484 -2.0; 518 -2.3; 554 -1.2; 593 -0.2; 635 0.4; 679 1.4; 726 1.5; 777 1.6; 832 1.2; 890 0.8; 952 0.1; 1019 0.1; 1090 0.9; 1167 2.0; 1248 2.0; 1336 1.7; 1429 1.2; 1529 1.5; 1636 1.9; 1751 1.8; 1873 2.9; 2004 2.8; 2145 3.1; 2295 3.7; 2455 3.8; 2627 4.3; 2811 4.0; 3008 4.0; 3219 4.1; 3444 4.8; 3685 5.5; 3943 5.9; 4219 5.7; 4514 5.4; 4830 4.9; 5168 4.7; 5530 3.5; 5917 2.2; 6331 2.1; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.037607804388462dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 266 Hz  | 1.61 | -3.3 dB |
| Peaking | 509 Hz  | 2.95 | -2.1 dB |
| Peaking | 706 Hz  | 3.08 | 1.9 dB  |
| Peaking | 2433 Hz | 0.98 | 2.8 dB  |
| Peaking | 4338 Hz | 1.69 | 4.8 dB  |
| Peaking | 78 Hz   | 1.92 | 1.8 dB  |
| Peaking | 189 Hz  | 6.71 | -1.0 dB |
| Peaking | 1005 Hz | 7.8  | -1.1 dB |
| Peaking | 1200 Hz | 7.4  | 1.3 dB  |
| Peaking | 8838 Hz | 3.74 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Dog%202014/MrSpeakers%20Alpha%20Dog%202014.png)