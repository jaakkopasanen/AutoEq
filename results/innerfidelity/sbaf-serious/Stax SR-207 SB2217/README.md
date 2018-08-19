# Stax SR-207 SB2217

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 10 -84; 20 6.7; 22 5.8; 23 5.4; 25 4.8; 26 4.5; 28 4.1; 30 3.9; 32 3.7; 35 3.7; 37 3.7; 40 3.8; 42 3.8; 45 3.9; 49 4.1; 52 4.1; 56 4.2; 59 4.2; 64 4.2; 68 4.0; 73 3.8; 78 3.6; 83 3.4; 89 3.2; 95 3.0; 102 2.8; 109 2.7; 117 2.6; 125 2.4; 134 2.3; 143 2.2; 153 2.2; 164 2.2; 175 2.1; 188 2.0; 201 1.9; 215 1.9; 230 2.0; 246 2.0; 263 2.0; 282 2.0; 301 2.0; 323 1.8; 345 1.8; 369 1.9; 395 1.8; 423 1.9; 452 1.8; 484 1.7; 518 1.6; 554 1.7; 593 1.9; 635 1.7; 679 1.5; 726 1.3; 777 1.3; 832 1.0; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.8; 1248 -1.3; 1336 -1.9; 1429 -2.5; 1529 -3.1; 1636 -3.4; 1751 -3.2; 1873 -2.3; 2004 -0.5; 2145 0.8; 2295 2.3; 2455 3.0; 2627 2.9; 2811 1.5; 3008 1.7; 3219 1.2; 3444 1.4; 3685 1.7; 3943 2.5; 4219 2.0; 4514 1.1; 4830 1.0; 5168 1.7; 5530 0.9; 5917 -0.0; 6331 1.5; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -2.8; 9502 -3.2; 10167 -1.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -1.6; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.821269236994523dB` and instead set Global volume in the UI for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-207 SB2217 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.11 | 4.7 dB  |
| Peaking | 448 Hz  |  0.61 | 1.5 dB  |
| Peaking | 1651 Hz |  1.52 | -8.5 dB |
| Peaking | 2137 Hz |  0.78 | 5.5 dB  |
| Peaking | 9293 Hz |  6.78 | -4.2 dB |
| Peaking | 37 Hz   |  2.59 | -0.7 dB |
| Peaking | 65 Hz   |  2.86 | 0.5 dB  |
| Peaking | 2501 Hz |  5.35 | 2.2 dB  |
| Peaking | 2822 Hz |  3    | -1.6 dB |
| Peaking | 6827 Hz | 10.35 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-207%20SB2217/Stax%20SR-207%20SB2217.png)