# MrSpeakers Ether C 2 Black Filters

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.6; 22 2.5; 23 2.4; 25 2.4; 26 2.4; 28 2.4; 30 2.4; 32 2.5; 35 2.8; 37 3.0; 40 3.4; 42 3.7; 45 4.1; 49 4.1; 52 3.8; 56 3.0; 59 2.7; 64 3.0; 68 3.3; 73 3.4; 78 3.2; 83 3.0; 89 2.8; 95 2.2; 102 1.5; 109 1.3; 117 1.8; 125 1.8; 134 2.1; 143 2.6; 153 3.2; 164 3.2; 175 1.9; 188 1.6; 201 1.2; 215 0.9; 230 0.7; 246 0.4; 263 0.3; 282 0.4; 301 0.3; 323 0.3; 345 0.5; 369 0.6; 395 0.9; 423 1.4; 452 1.5; 484 1.5; 518 1.5; 554 1.5; 593 1.4; 635 1.3; 679 1.0; 726 0.9; 777 0.9; 832 0.7; 890 0.0; 952 0.0; 1019 0.2; 1090 0.7; 1167 0.9; 1248 0.7; 1336 0.4; 1429 0.2; 1529 -0.0; 1636 -0.3; 1751 -0.3; 1873 0.4; 2004 0.8; 2145 1.0; 2295 1.7; 2455 1.7; 2627 2.0; 2811 2.3; 3008 2.6; 3219 2.3; 3444 2.2; 3685 2.4; 3943 2.4; 4219 2.1; 4514 2.6; 4830 3.9; 5168 5.6; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09476586581956dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 2 Black Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.98 | 2.1 dB  |
| Peaking | 50 Hz   | 0.45 | 3.4 dB  |
| Peaking | 160 Hz  | 5.23 | 2.2 dB  |
| Peaking | 3003 Hz | 1.67 | 2.1 dB  |
| Peaking | 5703 Hz | 2.92 | 6.4 dB  |
| Peaking | 355 Hz  | 1.07 | -1.3 dB |
| Peaking | 472 Hz  | 1.19 | 2.3 dB  |
| Peaking | 1686 Hz | 6.64 | -1.1 dB |
| Peaking | 8242 Hz | 4.71 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%202%20Black%20Filters/MrSpeakers%20Ether%20C%202%20Black%20Filters.png)