# Massdrop x EMu Purpleheart

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.5; 23 -2.6; 25 -3.0; 26 -3.1; 28 -3.3; 30 -3.5; 32 -3.7; 35 -3.9; 37 -4.1; 40 -4.2; 42 -4.3; 45 -4.4; 49 -4.6; 52 -4.6; 56 -4.7; 59 -4.7; 64 -4.8; 68 -4.8; 73 -4.8; 78 -4.9; 83 -5.0; 89 -5.2; 95 -5.5; 102 -5.8; 109 -6.0; 117 -6.3; 125 -6.5; 134 -6.7; 143 -6.7; 153 -6.7; 164 -6.6; 175 -6.4; 188 -6.3; 201 -6.0; 215 -5.7; 230 -5.4; 246 -5.1; 263 -4.8; 282 -4.4; 301 -4.2; 323 -4.0; 345 -3.6; 369 -3.3; 395 -2.9; 423 -2.5; 452 -2.4; 484 -2.4; 518 -2.2; 554 -1.8; 593 -1.4; 635 -1.3; 679 -1.3; 726 -1.1; 777 -0.9; 832 -1.1; 890 -0.6; 952 0.0; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.9; 1429 -1.2; 1529 -1.3; 1636 -1.3; 1751 -1.0; 1873 -0.6; 2004 -0.2; 2145 0.4; 2295 0.9; 2455 1.5; 2627 1.3; 2811 -0.0; 3008 -0.9; 3219 -1.1; 3444 -0.3; 3685 1.5; 3943 1.7; 4219 -1.5; 4514 -1.0; 4830 1.0; 5168 2.4; 5530 4.7; 5917 5.6; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.0; 8880 -2.4; 9502 -2.6; 10167 -1.8; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x EMu Purpleheart ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 4 Hz    | 1.75 | -1.4 dB |
| Peaking | 36 Hz   | 0.7  | -3.0 dB |
| Peaking | 158 Hz  | 0.51 | -6.3 dB |
| Peaking | 6071 Hz | 3.65 | 6.3 dB  |
| Peaking | 9213 Hz | 3.84 | -3.4 dB |
| Peaking | 974 Hz  | 3.92 | 1.2 dB  |
| Peaking | 1592 Hz | 2.42 | -1.3 dB |
| Peaking | 2512 Hz | 3.6  | 2.1 dB  |
| Peaking | 871 Hz  | 3.67 | -0.5 dB |
| Peaking | 3051 Hz | 5.54 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20EMu%20Purpleheart/Massdrop%20x%20EMu%20Purpleheart.png)