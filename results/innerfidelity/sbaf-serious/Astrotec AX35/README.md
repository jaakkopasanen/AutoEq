# Astrotec AX35

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.6; 45 5.0; 49 4.3; 52 3.9; 56 3.3; 59 2.8; 64 2.1; 68 1.6; 73 1.0; 78 0.4; 83 -0.1; 89 -0.7; 95 -1.3; 102 -1.8; 109 -2.1; 117 -2.5; 125 -2.9; 134 -3.3; 143 -3.6; 153 -3.9; 164 -4.2; 175 -4.2; 188 -4.4; 201 -4.6; 215 -4.6; 230 -4.6; 246 -4.6; 263 -4.6; 282 -4.5; 301 -4.4; 323 -4.2; 345 -4.0; 369 -3.8; 395 -3.6; 423 -3.2; 452 -2.9; 484 -2.7; 518 -2.4; 554 -2.0; 593 -1.4; 635 -1.1; 679 -0.8; 726 -0.5; 777 -0.1; 832 -0.0; 890 -0.0; 952 0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.3; 1529 -2.8; 1636 -3.0; 1751 -2.9; 1873 -2.5; 2004 -2.1; 2145 -1.6; 2295 -1.0; 2455 0.0; 2627 0.9; 2811 2.1; 3008 4.2; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 4.8; 4830 4.5; 5168 4.6; 5530 3.9; 5917 2.0; 6331 -0.2; 6775 1.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.6  | 6.9 dB  |
| Peaking | 201 Hz  | 0.56 | -5.3 dB |
| Peaking | 1884 Hz | 1.87 | -4.0 dB |
| Peaking | 3768 Hz | 1.49 | 7.0 dB  |
| Peaking | 891 Hz  | 2.5  | 1.2 dB  |
| Peaking | 1495 Hz | 6.68 | -1.0 dB |
| Peaking | 4353 Hz | 3.33 | -0.5 dB |
| Peaking | 5353 Hz | 5.08 | 1.9 dB  |
| Peaking | 6309 Hz | 8.48 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX35/Astrotec%20AX35.png)