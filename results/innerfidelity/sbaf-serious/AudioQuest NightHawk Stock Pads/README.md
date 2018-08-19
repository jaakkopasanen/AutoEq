# AudioQuest NightHawk Stock Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -6.7; 22 -6.7; 23 -6.7; 25 -6.7; 26 -6.7; 28 -6.6; 30 -6.6; 32 -6.6; 35 -6.5; 37 -6.5; 40 -6.5; 42 -6.4; 45 -6.4; 49 -6.4; 52 -6.4; 56 -6.4; 59 -6.4; 64 -6.4; 68 -6.5; 73 -6.6; 78 -6.8; 83 -7.2; 89 -7.6; 95 -8.3; 102 -9.0; 109 -9.1; 117 -8.8; 125 -9.2; 134 -9.8; 143 -10.0; 153 -10.0; 164 -9.4; 175 -9.8; 188 -10.1; 201 -10.1; 215 -10.0; 230 -9.9; 246 -9.9; 263 -9.8; 282 -9.6; 301 -9.4; 323 -9.2; 345 -8.9; 369 -8.6; 395 -8.2; 423 -7.7; 452 -7.2; 484 -6.8; 518 -6.3; 554 -5.6; 593 -4.7; 635 -4.1; 679 -3.5; 726 -2.8; 777 -2.2; 832 -1.7; 890 -1.0; 952 -0.3; 1019 -0.1; 1090 -0.6; 1167 -0.9; 1248 -1.1; 1336 -2.2; 1429 -3.3; 1529 -4.1; 1636 -4.5; 1751 -4.4; 1873 -3.9; 2004 -3.2; 2145 -2.5; 2295 -1.8; 2455 -0.2; 2627 1.8; 2811 2.4; 3008 2.3; 3219 0.7; 3444 -0.4; 3685 0.4; 3943 2.1; 4219 2.0; 4514 2.1; 4830 2.4; 5168 2.4; 5530 0.8; 5917 -0.6; 6331 -0.8; 6775 -1.3; 7249 -2.5; 7756 -3.6; 8299 -4.6; 8880 -5.2; 9502 -4.8; 10167 -2.4; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.3; 16326 -0.9; 17469 -2.5; 18692 -4.7; 20000 -6.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6015564877323993dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightHawk Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.08 | -5.7 dB  |
| Peaking | 364 Hz  | 0.38 | -8.3 dB  |
| Peaking | 1363 Hz | 0.39 | 8.0 dB   |
| Peaking | 1738 Hz | 1.43 | -10.0 dB |
| Peaking | 8533 Hz | 2.47 | -6.1 dB  |
| Peaking | 27 Hz   | 0.2  | -0.8 dB  |
| Peaking | 65 Hz   | 1.71 | 1.5 dB   |
| Peaking | 2867 Hz | 4.11 | 4.1 dB   |
| Peaking | 3463 Hz | 1.88 | -4.5 dB  |
| Peaking | 4243 Hz | 2.48 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightHawk%20Stock%20Pads/AudioQuest%20NightHawk%20Stock%20Pads.png)