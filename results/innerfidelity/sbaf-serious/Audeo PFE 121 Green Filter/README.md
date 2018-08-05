# Audeo PFE 121 Green Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.6; 22 -1.6; 23 -1.7; 25 -1.7; 26 -1.7; 28 -1.8; 30 -1.8; 32 -1.8; 35 -1.9; 37 -1.9; 40 -2.0; 42 -2.0; 45 -2.1; 49 -2.1; 52 -2.1; 56 -2.1; 59 -2.2; 64 -2.2; 68 -2.2; 73 -2.3; 78 -2.5; 83 -2.7; 89 -3.1; 95 -3.5; 102 -4.0; 109 -4.4; 117 -5.0; 125 -5.5; 134 -5.9; 143 -6.1; 153 -6.3; 164 -6.4; 175 -6.3; 188 -6.2; 201 -6.2; 215 -6.0; 230 -5.7; 246 -5.6; 263 -5.4; 282 -5.1; 301 -4.9; 323 -4.6; 345 -4.3; 369 -4.1; 395 -3.8; 423 -3.4; 452 -3.0; 484 -2.6; 518 -2.3; 554 -1.8; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.4; 777 -0.1; 832 0.1; 890 0.0; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.3; 1336 0.2; 1429 0.2; 1529 0.1; 1636 0.3; 1751 0.7; 1873 1.4; 2004 2.1; 2145 2.8; 2295 3.6; 2455 4.7; 2627 4.8; 2811 4.5; 3008 4.2; 3219 4.6; 3444 5.8; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.2; 8880 -3.9; 9502 -4.8; 10167 -2.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.4; 15258 -1.9; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Green Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.93 | -1.5 dB |
| Peaking | 190 Hz   | 0.6  | -6.4 dB |
| Peaking | 3476 Hz  | 0.99 | 5.1 dB  |
| Peaking | 5781 Hz  | 1.91 | 4.3 dB  |
| Peaking | 9211 Hz  | 3.56 | -6.4 dB |
| Peaking | 804 Hz   | 3.38 | 0.8 dB  |
| Peaking | 1672 Hz  | 2.75 | -1.2 dB |
| Peaking | 2678 Hz  | 2.16 | 1.7 dB  |
| Peaking | 2977 Hz  | 5.07 | -2.2 dB |
| Peaking | 15105 Hz | 7.91 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Green%20Filter/Audeo%20PFE%20121%20Green%20Filter.png)