# Audio Technica ATH-MSR7NC Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.5; 22 5.9; 23 5.6; 25 5.2; 26 5.0; 28 4.6; 30 4.3; 32 4.0; 35 3.6; 37 3.4; 40 3.2; 42 3.0; 45 2.9; 49 2.7; 52 2.5; 56 2.4; 59 2.2; 64 2.0; 68 1.9; 73 1.8; 78 1.7; 83 1.6; 89 1.4; 95 1.3; 102 1.2; 109 1.1; 117 1.1; 125 0.8; 134 0.3; 143 -0.0; 153 -0.2; 164 0.4; 175 0.6; 188 0.1; 201 -0.0; 215 0.0; 230 0.1; 246 0.3; 263 0.7; 282 1.4; 301 2.0; 323 2.7; 345 3.6; 369 4.3; 395 5.0; 423 5.5; 452 5.6; 484 5.4; 518 5.0; 554 4.8; 593 4.4; 635 3.9; 679 3.1; 726 2.6; 777 2.1; 832 1.4; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.7; 1336 -1.3; 1429 -2.2; 1529 -3.0; 1636 -3.5; 1751 -3.7; 1873 -3.7; 2004 -3.6; 2145 -3.0; 2295 -2.0; 2455 -0.4; 2627 1.0; 2811 2.0; 3008 3.1; 3219 3.5; 3444 4.2; 3685 4.5; 3943 3.7; 4219 1.1; 4514 -0.9; 4830 -0.4; 5168 1.3; 5530 4.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.1; 9502 -1.2; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.569324495601718dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.34 | 6.9 dB  |
| Peaking | 483 Hz  | 1.45 | 6.0 dB  |
| Peaking | 1821 Hz | 1.74 | -4.6 dB |
| Peaking | 3324 Hz | 2.84 | 5.1 dB  |
| Peaking | 6096 Hz | 5.19 | 6.6 dB  |
| Peaking | 224 Hz  | 1.87 | -1.1 dB |
| Peaking | 362 Hz  | 4.25 | 1.0 dB  |
| Peaking | 4623 Hz | 5.46 | -5.0 dB |
| Peaking | 4629 Hz | 2.01 | 2.3 dB  |
| Peaking | 9073 Hz | 4.82 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20Passive/Audio%20Technica%20ATH-MSR7NC%20Passive.png)