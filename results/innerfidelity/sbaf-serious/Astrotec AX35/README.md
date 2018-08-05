# Astrotec AX35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.6; 49 5.1; 52 4.7; 56 4.3; 59 3.9; 64 3.4; 68 3.0; 73 2.5; 78 2.1; 83 1.6; 89 0.8; 95 0.1; 102 -0.7; 109 -1.3; 117 -2.2; 125 -2.9; 134 -3.5; 143 -4.0; 153 -4.4; 164 -4.7; 175 -4.8; 188 -4.9; 201 -5.0; 215 -5.0; 230 -4.9; 246 -4.9; 263 -4.8; 282 -4.7; 301 -4.5; 323 -4.3; 345 -4.1; 369 -3.9; 395 -3.6; 423 -3.3; 452 -3.0; 484 -2.8; 518 -2.5; 554 -2.0; 593 -1.4; 635 -1.1; 679 -0.8; 726 -0.6; 777 -0.1; 832 -0.0; 890 -0.0; 952 0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.3; 1529 -2.8; 1636 -3.0; 1751 -2.9; 1873 -2.5; 2004 -2.1; 2145 -1.6; 2295 -1.0; 2455 0.0; 2627 0.9; 2811 2.1; 3008 4.2; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 4.8; 4830 4.5; 5168 4.6; 5530 3.9; 5917 2.0; 6331 -0.2; 6775 1.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.36 | 6.9 dB  |
| Peaking | 186 Hz  | 0.59 | -6.8 dB |
| Peaking | 1883 Hz | 1.86 | -4.0 dB |
| Peaking | 3767 Hz | 1.49 | 7.0 dB  |
| Peaking | 894 Hz  | 2.53 | 1.2 dB  |
| Peaking | 1488 Hz | 6.68 | -1.0 dB |
| Peaking | 4318 Hz | 3.57 | -0.5 dB |
| Peaking | 5373 Hz | 4.85 | 2.0 dB  |
| Peaking | 6278 Hz | 7.49 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX35/Astrotec%20AX35.png)