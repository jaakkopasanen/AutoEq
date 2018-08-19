# Sony MDR-1000X Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 -1.6; 22 -2.5; 23 -3.0; 25 -3.8; 26 -4.1; 28 -4.8; 30 -5.4; 32 -5.9; 35 -6.6; 37 -7.0; 40 -7.6; 42 -7.9; 45 -8.3; 49 -8.8; 52 -9.2; 56 -9.5; 59 -9.8; 64 -10.0; 68 -10.2; 73 -10.2; 78 -10.1; 83 -9.9; 89 -9.6; 95 -9.4; 102 -9.2; 109 -9.5; 117 -10.1; 125 -10.3; 134 -9.4; 143 -8.5; 153 -8.3; 164 -6.8; 175 -5.7; 188 -6.7; 201 -6.1; 215 -5.3; 230 -4.3; 246 -3.5; 263 -3.0; 282 -2.5; 301 -2.3; 323 -2.1; 345 -2.1; 369 -2.2; 395 -2.3; 423 -2.3; 452 -2.4; 484 -2.9; 518 -3.0; 554 -2.8; 593 -2.6; 635 -3.2; 679 -3.5; 726 -3.1; 777 -2.0; 832 -1.8; 890 -1.8; 952 -0.8; 1019 0.2; 1090 1.2; 1167 2.5; 1248 3.3; 1336 3.6; 1429 3.3; 1529 2.3; 1636 1.3; 1751 0.3; 1873 0.2; 2004 0.7; 2145 2.1; 2295 3.4; 2455 4.2; 2627 3.2; 2811 1.0; 3008 -1.1; 3219 -2.8; 3444 -3.8; 3685 -5.2; 3943 -7.2; 4219 -7.8; 4514 -6.6; 4830 -4.1; 5168 -4.9; 5530 -5.1; 5917 -2.1; 6331 0.3; 6775 2.2; 7249 0.6; 7756 -1.9; 8299 -4.2; 8880 -4.9; 9502 -3.3; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.265603908727188dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.88 | -3.3 dB |
| Peaking | 99 Hz   | 0.47 | -8.8 dB |
| Peaking | 2534 Hz | 1.04 | 4.5 dB  |
| Peaking | 4043 Hz | 2.03 | -9.9 dB |
| Peaking | 8820 Hz | 6.59 | -5.2 dB |
| Peaking | 298 Hz  | 2.18 | 1.8 dB  |
| Peaking | 726 Hz  | 1.12 | -2.9 dB |
| Peaking | 1290 Hz | 2.16 | 4.0 dB  |
| Peaking | 1818 Hz | 5.01 | -3.0 dB |
| Peaking | 6736 Hz | 9.66 | 4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wired%20Passive/Sony%20MDR-1000X%20Wired%20Passive.png)