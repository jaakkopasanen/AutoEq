# Meze 99 Neo with Classic Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.5; 56 5.1; 59 4.9; 64 4.8; 68 4.8; 73 4.8; 78 4.7; 83 4.3; 89 3.8; 95 3.4; 102 3.1; 109 2.7; 117 2.3; 125 1.8; 134 1.5; 143 1.2; 153 0.9; 164 1.0; 175 1.1; 188 1.0; 201 1.0; 215 1.2; 230 1.2; 246 1.8; 263 2.5; 282 2.9; 301 3.2; 323 3.8; 345 4.3; 369 4.5; 395 4.4; 423 4.0; 452 3.3; 484 2.2; 518 1.5; 554 0.8; 593 0.6; 635 0.3; 679 -0.0; 726 -0.2; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.1; 1248 0.1; 1336 0.1; 1429 -0.1; 1529 -0.2; 1636 -0.4; 1751 -0.4; 1873 -0.4; 2004 -0.1; 2145 -0.0; 2295 -0.2; 2455 0.1; 2627 1.1; 2811 1.3; 3008 1.6; 3219 2.2; 3444 3.4; 3685 4.4; 3943 4.4; 4219 1.9; 4514 1.6; 4830 2.3; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Neo with Classic Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.54 | 8.5 dB  |
| Peaking | 34 Hz   | 1.45 | -2.6 dB |
| Peaking | 369 Hz  | 2.23 | 4.6 dB  |
| Peaking | 3682 Hz | 4.47 | 4.1 dB  |
| Peaking | 5815 Hz | 3.4  | 6.6 dB  |
| Peaking | 83 Hz   | 3.96 | 0.5 dB  |
| Peaking | 155 Hz  | 3.37 | -0.8 dB |
| Peaking | 1196 Hz | 0.82 | -0.4 dB |
| Peaking | 8225 Hz | 5.25 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2099%20Neo%20with%20Classic%20Pads/Meze%2099%20Neo%20with%20Classic%20Pads.png)