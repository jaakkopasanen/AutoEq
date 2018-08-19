# AudioQuest NightOwl Stock Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.1; 22 -1.1; 23 -1.1; 25 -1.0; 26 -1.0; 28 -0.9; 30 -0.9; 32 -0.8; 35 -0.7; 37 -0.7; 40 -0.6; 42 -0.6; 45 -0.5; 49 -0.4; 52 -0.3; 56 -0.2; 59 -0.1; 64 -0.1; 68 -0.1; 73 -0.4; 78 -0.7; 83 -1.1; 89 -1.8; 95 -2.7; 102 -3.1; 109 -2.6; 117 -3.0; 125 -3.6; 134 -3.8; 143 -3.9; 153 -3.5; 164 -2.8; 175 -3.5; 188 -3.6; 201 -3.4; 215 -3.2; 230 -2.9; 246 -2.7; 263 -2.5; 282 -2.2; 301 -2.0; 323 -1.7; 345 -1.4; 369 -1.2; 395 -1.0; 423 -0.7; 452 -0.6; 484 -0.7; 518 -0.7; 554 -0.5; 593 -0.2; 635 -0.1; 679 0.1; 726 0.4; 777 0.5; 832 0.2; 890 -0.0; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.6; 1248 0.9; 1336 1.1; 1429 1.3; 1529 1.8; 1636 2.7; 1751 3.7; 1873 4.9; 2004 5.9; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 5.9; 3444 5.0; 3685 5.8; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.4; 6331 2.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999984dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightOwl Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.04 | -0.8 dB |
| Peaking | 67 Hz   | 1.58 | 2.2 dB  |
| Peaking | 136 Hz  | 0.79 | -2.2 dB |
| Peaking | 147 Hz  | 0.34 | -1.8 dB |
| Peaking | 3256 Hz | 0.74 | 6.8 dB  |
| Peaking | 1301 Hz | 1.85 | -1.2 dB |
| Peaking | 2018 Hz | 3.87 | 2.1 dB  |
| Peaking | 3421 Hz | 4.53 | -1.6 dB |
| Peaking | 5411 Hz | 2.88 | 2.5 dB  |
| Peaking | 8539 Hz | 1.59 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightOwl%20Stock%20Pads/AudioQuest%20NightOwl%20Stock%20Pads.png)