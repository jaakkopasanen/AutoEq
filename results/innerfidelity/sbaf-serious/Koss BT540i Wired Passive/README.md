# Koss BT540i Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.3; 22 1.3; 23 0.8; 25 -0.0; 26 -0.4; 28 -1.2; 30 -1.8; 32 -2.4; 35 -3.1; 37 -3.5; 40 -4.0; 42 -4.3; 45 -4.6; 49 -5.0; 52 -5.3; 56 -5.6; 59 -5.7; 64 -5.9; 68 -6.1; 73 -6.2; 78 -6.3; 83 -6.4; 89 -6.5; 95 -6.7; 102 -7.1; 109 -7.1; 117 -7.1; 125 -7.4; 134 -7.8; 143 -8.3; 153 -8.8; 164 -8.5; 175 -7.6; 188 -8.1; 201 -8.2; 215 -8.0; 230 -7.6; 246 -7.2; 263 -6.7; 282 -5.8; 301 -5.0; 323 -4.7; 345 -4.0; 369 -2.9; 395 -1.7; 423 -0.4; 452 0.2; 484 0.5; 518 0.8; 554 1.3; 593 1.5; 635 1.4; 679 1.0; 726 0.6; 777 0.5; 832 0.2; 890 0.0; 952 -0.0; 1019 0.0; 1090 0.0; 1167 -0.3; 1248 -0.4; 1336 -0.7; 1429 -1.3; 1529 -1.7; 1636 -2.3; 1751 -2.7; 1873 -3.0; 2004 -3.2; 2145 -3.7; 2295 -4.2; 2455 -4.6; 2627 -5.3; 2811 -6.0; 3008 -6.4; 3219 -6.1; 3444 -4.6; 3685 -3.3; 3943 -1.3; 4219 -0.0; 4514 2.7; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.2; 7249 1.2; 7756 -0.1; 8299 -2.5; 8880 -4.7; 9502 -4.6; 10167 -1.8; 10879 -0.0; 11640 0.0; 12455 -0.3; 13327 -1.1; 14260 -1.5; 15258 -1.1; 16326 -0.1; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 83 Hz    | 0.62 | -6.1 dB |
| Peaking | 202 Hz   | 1.33 | -6.3 dB |
| Peaking | 3082 Hz  | 1.4  | -8.3 dB |
| Peaking | 5359 Hz  | 1.64 | 9.2 dB  |
| Peaking | 9008 Hz  | 3.6  | -6.6 dB |
| Peaking | 21 Hz    | 2.79 | 3.0 dB  |
| Peaking | 146 Hz   | 7.57 | -1.2 dB |
| Peaking | 325 Hz   | 2.82 | -2.2 dB |
| Peaking | 536 Hz   | 1.39 | 2.7 dB  |
| Peaking | 33496 Hz | 4.42 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Wired%20Passive/Koss%20BT540i%20Wired%20Passive.png)