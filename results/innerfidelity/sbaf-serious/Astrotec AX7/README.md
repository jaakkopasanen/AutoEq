# Astrotec AX7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.8; 73 5.6; 78 5.3; 83 5.0; 89 4.6; 95 4.0; 102 3.4; 109 2.8; 117 2.2; 125 1.4; 134 0.9; 143 0.4; 153 0.1; 164 -0.1; 175 -0.2; 188 -0.4; 201 -0.5; 215 -0.6; 230 -0.5; 246 -0.7; 263 -0.7; 282 -0.6; 301 -0.6; 323 -0.6; 345 -0.5; 369 -0.5; 395 -0.5; 423 -0.2; 452 -0.1; 484 -0.1; 518 -0.0; 554 0.2; 593 0.5; 635 0.5; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.7; 1636 -1.8; 1751 -1.9; 1873 -1.8; 2004 -1.7; 2145 -1.4; 2295 -0.9; 2455 0.2; 2627 1.8; 2811 4.0; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.1; 4514 1.2; 4830 1.6; 5168 3.0; 5530 4.0; 5917 4.6; 6331 5.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.32 | 7.7 dB  |
| Peaking | 698 Hz  | 0.5  | 7.6 dB  |
| Peaking | 712 Hz  | 0.15 | -7.4 dB |
| Peaking | 3356 Hz | 1.9  | 10.3 dB |
| Peaking | 6144 Hz | 3    | 6.2 dB  |
| Peaking | 15 Hz   | 0.94 | 1.6 dB  |
| Peaking | 39 Hz   | 1.08 | -1.3 dB |
| Peaking | 104 Hz  | 0.65 | 1.3 dB  |
| Peaking | 138 Hz  | 1.61 | -1.8 dB |
| Peaking | 2159 Hz | 5.57 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX7/Astrotec%20AX7.png)