# Beats Mixr 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.5; 22 -1.1; 23 -1.4; 25 -1.8; 26 -1.9; 28 -2.2; 30 -2.4; 32 -2.5; 35 -2.7; 37 -2.8; 40 -2.9; 42 -3.0; 45 -3.0; 49 -3.1; 52 -3.2; 56 -3.3; 59 -3.3; 64 -3.3; 68 -3.4; 73 -3.5; 78 -3.5; 83 -3.5; 89 -3.8; 95 -4.1; 102 -4.6; 109 -4.8; 117 -4.7; 125 -4.8; 134 -5.2; 143 -5.5; 153 -5.9; 164 -5.7; 175 -5.5; 188 -5.8; 201 -5.7; 215 -5.6; 230 -5.3; 246 -4.7; 263 -3.6; 282 -2.4; 301 -1.3; 323 -0.9; 345 0.6; 369 2.2; 395 3.0; 423 4.2; 452 4.1; 484 3.4; 518 3.1; 554 2.5; 593 2.2; 635 1.7; 679 1.2; 726 0.8; 777 0.6; 832 0.4; 890 0.1; 952 0.1; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.6; 1429 0.4; 1529 0.2; 1636 -0.1; 1751 -0.2; 1873 -0.2; 2004 -0.4; 2145 -0.7; 2295 -1.0; 2455 -1.1; 2627 -1.5; 2811 -1.6; 3008 -1.0; 3219 -0.4; 3444 0.8; 3685 2.2; 3943 3.1; 4219 4.2; 4514 2.6; 4830 0.5; 5168 3.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Mixr 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.88 | -2.0 dB |
| Peaking | 249 Hz  | 0.47 | -9.1 dB |
| Peaking | 423 Hz  | 1.03 | 10.9 dB |
| Peaking | 4125 Hz | 6.98 | 3.6 dB  |
| Peaking | 5929 Hz | 3.91 | 6.7 dB  |
| Peaking | 1315 Hz | 4.26 | 0.9 dB  |
| Peaking | 2743 Hz | 2.58 | -1.8 dB |
| Peaking | 3649 Hz | 6.85 | 1.3 dB  |
| Peaking | 8231 Hz | 5.48 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Mixr%202014/Beats%20Mixr%202014.png)