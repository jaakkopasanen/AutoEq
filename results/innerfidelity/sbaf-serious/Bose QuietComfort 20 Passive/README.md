# Bose QuietComfort 20 Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.3; 37 4.7; 40 3.9; 42 3.3; 45 2.6; 49 1.7; 52 1.2; 56 0.5; 59 -0.0; 64 -0.7; 68 -1.2; 73 -1.7; 78 -2.2; 83 -2.6; 89 -3.0; 95 -3.4; 102 -3.7; 109 -3.9; 117 -4.0; 125 -4.1; 134 -4.0; 143 -3.9; 153 -3.5; 164 -3.2; 175 -2.7; 188 -2.5; 201 -2.5; 215 -2.6; 230 -2.9; 246 -3.3; 263 -3.6; 282 -3.8; 301 -3.7; 323 -3.5; 345 -2.9; 369 -2.1; 395 -1.4; 423 -0.4; 452 0.4; 484 1.1; 518 1.8; 554 2.4; 593 2.9; 635 2.9; 679 2.7; 726 2.5; 777 2.2; 832 1.7; 890 1.1; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -1.9; 1336 -2.8; 1429 -3.7; 1529 -4.1; 1636 -3.7; 1751 -1.9; 1873 0.3; 2004 2.8; 2145 5.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.4; 3943 1.2; 4219 -0.4; 4514 2.1; 4830 5.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 0.0; 7756 -1.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.62 | 8.3 dB   |
| Peaking | 104 Hz  | 0.37 | -5.3 dB  |
| Peaking | 1517 Hz | 1.75 | -15.2 dB |
| Peaking | 1826 Hz | 0.61 | 11.1 dB  |
| Peaking | 5783 Hz | 5.01 | 4.5 dB   |
| Peaking | 321 Hz  | 1.93 | -4.2 dB  |
| Peaking | 1165 Hz | 0.28 | 6.3 dB   |
| Peaking | 1280 Hz | 0.6  | -7.0 dB  |
| Peaking | 4173 Hz | 7.92 | -6.6 dB  |
| Peaking | 7996 Hz | 2.93 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Passive/Bose%20QuietComfort%2020%20Passive.png)