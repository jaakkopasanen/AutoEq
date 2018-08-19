# Life Acoustics PreKickstarter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.0; 22 0.8; 23 0.8; 25 0.6; 26 0.5; 28 0.4; 30 0.3; 32 0.2; 35 0.0; 37 -0.1; 40 -0.2; 42 -0.2; 45 -0.4; 49 -0.7; 52 -0.8; 56 -1.0; 59 -1.1; 64 -1.4; 68 -1.6; 73 -2.0; 78 -2.2; 83 -2.5; 89 -2.8; 95 -3.0; 102 -3.3; 109 -3.4; 117 -3.5; 125 -3.8; 134 -4.0; 143 -4.2; 153 -4.2; 164 -4.4; 175 -4.4; 188 -4.4; 201 -4.5; 215 -4.4; 230 -4.3; 246 -4.2; 263 -4.1; 282 -4.0; 301 -3.9; 323 -3.7; 345 -3.4; 369 -3.3; 395 -3.1; 423 -2.7; 452 -2.5; 484 -2.4; 518 -2.1; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.7; 726 -0.4; 777 -0.0; 832 -0.0; 890 -0.0; 952 -0.0; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 0.1; 1429 0.1; 1529 0.0; 1636 0.0; 1751 0.1; 1873 0.2; 2004 0.3; 2145 0.3; 2295 0.6; 2455 1.6; 2627 2.8; 2811 3.9; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.3; 4219 3.1; 4514 2.2; 4830 2.8; 5168 4.1; 5530 4.9; 5917 5.5; 6331 4.9; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999996093441dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Life Acoustics PreKickstarter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.57 | 1.2 dB  |
| Peaking | 152 Hz  | 0.62 | -4.0 dB |
| Peaking | 332 Hz  | 1.19 | -1.9 dB |
| Peaking | 3390 Hz | 2.48 | 6.5 dB  |
| Peaking | 5940 Hz | 3.76 | 5.3 dB  |
| Peaking | 832 Hz  | 3.11 | 0.6 dB  |
| Peaking | 2254 Hz | 3.14 | -1.0 dB |
| Peaking | 2703 Hz | 4.45 | 1.0 dB  |
| Peaking | 8875 Hz | 3.83 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Life%20Acoustics%20PreKickstarter/Life%20Acoustics%20PreKickstarter.png)