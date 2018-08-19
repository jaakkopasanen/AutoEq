# Plantronics BackBeat 500 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.7; 22 -1.8; 23 -1.9; 25 -2.0; 26 -2.0; 28 -2.1; 30 -2.2; 32 -2.2; 35 -2.3; 37 -2.3; 40 -2.3; 42 -2.2; 45 -2.1; 49 -2.2; 52 -2.5; 56 -2.8; 59 -2.9; 64 -3.0; 68 -3.1; 73 -3.1; 78 -3.1; 83 -3.0; 89 -2.8; 95 -2.8; 102 -3.0; 109 -3.3; 117 -3.8; 125 -4.4; 134 -4.7; 143 -4.6; 153 -4.3; 164 -3.8; 175 -3.9; 188 -3.7; 201 -3.4; 215 -2.9; 230 -2.3; 246 -2.2; 263 -2.1; 282 -2.2; 301 -2.2; 323 -1.9; 345 -1.5; 369 -1.0; 395 -0.3; 423 0.0; 452 -0.0; 484 -0.1; 518 -0.2; 554 -0.0; 593 0.1; 635 -0.1; 679 -0.4; 726 -0.6; 777 -0.8; 832 -0.8; 890 -0.5; 952 -0.1; 1019 0.0; 1090 -0.2; 1167 0.1; 1248 0.2; 1336 -0.2; 1429 -0.8; 1529 -1.6; 1636 -2.2; 1751 -2.6; 1873 -2.3; 2004 -1.6; 2145 -1.0; 2295 -0.2; 2455 1.3; 2627 2.6; 2811 2.6; 3008 3.5; 3219 3.9; 3444 4.2; 3685 4.6; 3943 5.6; 4219 5.8; 4514 6.0; 4830 5.8; 5168 5.6; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099964035426115dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat 500 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.41 | -2.3 dB |
| Peaking | 152 Hz  | 1.24 | -3.5 dB |
| Peaking | 299 Hz  | 3.66 | -1.1 dB |
| Peaking | 1807 Hz | 2.95 | -3.7 dB |
| Peaking | 4531 Hz | 1.2  | 6.6 dB  |
| Peaking | 2272 Hz | 5.52 | -1.6 dB |
| Peaking | 2565 Hz | 2.59 | 1.4 dB  |
| Peaking | 4759 Hz | 2.99 | -0.6 dB |
| Peaking | 6336 Hz | 3.16 | 4.7 dB  |
| Peaking | 7305 Hz | 1.59 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plantronics%20BackBeat%20500%20Wired/Plantronics%20BackBeat%20500%20Wired.png)