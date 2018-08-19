# MrSpeakers Aeon Flow Closed PreProduction

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 1.3; 22 1.2; 23 1.1; 25 1.0; 26 0.9; 28 0.9; 30 0.8; 32 0.8; 35 0.7; 37 0.7; 40 0.7; 42 0.7; 45 0.6; 49 0.6; 52 0.5; 56 0.4; 59 0.4; 64 0.5; 68 0.5; 73 0.4; 78 0.3; 83 -0.2; 89 -0.6; 95 -1.3; 102 -2.0; 109 -2.2; 117 -2.3; 125 -2.2; 134 -1.7; 143 -1.1; 153 -0.3; 164 0.6; 175 -0.2; 188 0.1; 201 0.3; 215 0.4; 230 0.4; 246 0.3; 263 0.2; 282 0.2; 301 0.1; 323 -0.0; 345 -0.1; 369 -0.2; 395 -0.2; 423 0.0; 452 0.1; 484 0.1; 518 0.2; 554 0.3; 593 0.4; 635 0.4; 679 0.3; 726 0.5; 777 0.6; 832 1.0; 890 0.4; 952 -0.0; 1019 -0.2; 1090 -0.6; 1167 -0.7; 1248 -0.8; 1336 -1.1; 1429 -1.4; 1529 -1.7; 1636 -2.0; 1751 -2.0; 1873 -1.4; 2004 -0.5; 2145 -0.3; 2295 0.4; 2455 0.7; 2627 1.7; 2811 3.0; 3008 3.0; 3219 2.7; 3444 2.2; 3685 1.3; 3943 0.9; 4219 0.9; 4514 0.9; 4830 1.5; 5168 3.0; 5530 3.9; 5917 3.8; 6331 3.6; 6775 3.4; 7249 1.3; 7756 0.2; 8299 -1.7; 8880 -3.3; 9502 -2.8; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.292061336718834dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed PreProduction ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 115 Hz  | 3.7  | -2.6 dB |
| Peaking | 1661 Hz | 2.75 | -2.4 dB |
| Peaking | 2970 Hz | 3.42 | 3.2 dB  |
| Peaking | 6064 Hz | 2.48 | 4.3 dB  |
| Peaking | 8949 Hz | 4.57 | -4.3 dB |
| Peaking | 22 Hz   | 0.93 | 1.1 dB  |
| Peaking | 64 Hz   | 3.49 | 0.4 dB  |
| Peaking | 218 Hz  | 3.34 | 0.5 dB  |
| Peaking | 846 Hz  | 2.25 | 1.3 dB  |
| Peaking | 1040 Hz | 2.34 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20PreProduction/MrSpeakers%20Aeon%20Flow%20Closed%20PreProduction.png)