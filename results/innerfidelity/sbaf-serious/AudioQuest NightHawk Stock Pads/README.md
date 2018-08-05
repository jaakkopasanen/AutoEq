# AudioQuest NightHawk Stock Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 -6.7; 22 -6.7; 23 -6.7; 25 -6.6; 26 -6.6; 28 -6.6; 30 -6.6; 32 -6.5; 35 -6.5; 37 -6.4; 40 -6.3; 42 -6.3; 45 -6.3; 49 -6.2; 52 -6.1; 56 -6.0; 59 -6.0; 64 -5.9; 68 -5.9; 73 -5.9; 78 -6.1; 83 -6.4; 89 -6.8; 95 -7.5; 102 -8.4; 109 -8.7; 117 -8.6; 125 -9.2; 134 -9.9; 143 -10.2; 153 -10.2; 164 -9.6; 175 -10.0; 188 -10.3; 201 -10.3; 215 -10.1; 230 -10.0; 246 -10.0; 263 -9.8; 282 -9.6; 301 -9.5; 323 -9.2; 345 -8.9; 369 -8.6; 395 -8.2; 423 -7.7; 452 -7.2; 484 -6.8; 518 -6.3; 554 -5.6; 593 -4.7; 635 -4.1; 679 -3.5; 726 -2.8; 777 -2.2; 832 -1.7; 890 -1.0; 952 -0.3; 1019 -0.1; 1090 -0.6; 1167 -0.9; 1248 -1.1; 1336 -2.2; 1429 -3.3; 1529 -4.1; 1636 -4.5; 1751 -4.4; 1873 -3.9; 2004 -3.2; 2145 -2.5; 2295 -1.8; 2455 -0.2; 2627 1.8; 2811 2.4; 3008 2.3; 3219 0.7; 3444 -0.4; 3685 0.4; 3943 2.1; 4219 2.0; 4514 2.1; 4830 2.4; 5168 2.4; 5530 0.8; 5917 -0.6; 6331 -0.8; 6775 -1.3; 7249 -2.5; 7756 -3.6; 8299 -4.6; 8880 -5.2; 9502 -4.8; 10167 -2.4; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.3; 16326 -0.9; 17469 -2.5; 18692 -4.7; 20000 -6.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightHawk Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.45 | -6.3 dB |
| Peaking | 166 Hz   | 0.66 | -8.8 dB |
| Peaking | 380 Hz   | 1.12 | -5.1 dB |
| Peaking | 1701 Hz  | 3.81 | -4.7 dB |
| Peaking | 8791 Hz  | 3.64 | -5.9 dB |
| Peaking | 1009 Hz  | 3.8  | 1.9 dB  |
| Peaking | 3418 Hz  | 0.82 | -3.0 dB |
| Peaking | 2839 Hz  | 4.02 | 5.1 dB  |
| Peaking | 4477 Hz  | 2.14 | 5.1 dB  |
| Peaking | 19503 Hz | 1.89 | -6.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightHawk%20Stock%20Pads/AudioQuest%20NightHawk%20Stock%20Pads.png)