# Beyerdynamic DT X 350 m

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.7; 22 4.3; 23 4.1; 25 3.7; 26 3.6; 28 3.3; 30 3.0; 32 2.8; 35 2.6; 37 2.4; 40 2.3; 42 2.3; 45 2.3; 49 1.9; 52 1.5; 56 1.1; 59 0.9; 64 0.9; 68 0.8; 73 0.9; 78 1.4; 83 1.8; 89 1.8; 95 1.2; 102 0.2; 109 -0.6; 117 -1.6; 125 -2.4; 134 -2.6; 143 -2.3; 153 -1.6; 164 -0.0; 175 0.6; 188 1.5; 201 2.7; 215 4.2; 230 5.1; 246 5.3; 263 5.3; 282 5.0; 301 4.6; 323 4.0; 345 3.0; 369 2.1; 395 1.8; 423 1.6; 452 1.4; 484 1.2; 518 0.9; 554 0.9; 593 1.0; 635 0.8; 679 0.5; 726 0.4; 777 0.4; 832 0.2; 890 0.1; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.2; 1336 0.1; 1429 0.0; 1529 0.0; 1636 -0.2; 1751 -0.6; 1873 -0.6; 2004 -1.2; 2145 -1.3; 2295 -0.8; 2455 -0.2; 2627 0.5; 2811 0.9; 3008 1.7; 3219 2.6; 3444 4.7; 3685 6.0; 3943 3.2; 4219 -1.9; 4514 -1.5; 4830 0.7; 5168 3.1; 5530 3.4; 5917 1.6; 6331 0.3; 6775 -0.4; 7249 -0.5; 7756 -0.3; 8299 -0.9; 8880 -1.6; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999857591355dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X 350 m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 137 Hz   | 2.75 | -4.3 dB |
| Peaking | 259 Hz   | 1.58 | 5.7 dB  |
| Peaking | 3602 Hz  | 6.68 | 6.5 dB  |
| Peaking | 24000 Hz | 2.35 | 0.8 dB  |
| Peaking | 17 Hz    | 0.57 | 4.6 dB  |
| Peaking | 88 Hz    | 5.15 | 1.8 dB  |
| Peaking | 4369 Hz  | 9.34 | -3.8 dB |
| Peaking | 5386 Hz  | 6.13 | 3.9 dB  |
| Peaking | 8779 Hz  | 4.5  | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X%20350%20m/Beyerdynamic%20DT%20X%20350%20m.png)