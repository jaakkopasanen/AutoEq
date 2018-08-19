# Bowers & Wilkins P5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 4.6; 22 4.4; 23 4.2; 25 4.0; 26 3.8; 28 3.6; 30 3.3; 32 3.1; 35 2.8; 37 2.6; 40 2.4; 42 2.2; 45 1.9; 49 1.6; 52 1.3; 56 1.0; 59 0.8; 64 0.3; 68 -0.1; 73 -0.6; 78 -1.0; 83 -1.5; 89 -2.0; 95 -2.5; 102 -3.0; 109 -3.3; 117 -3.6; 125 -4.1; 134 -4.5; 143 -4.7; 153 -5.0; 164 -5.2; 175 -5.1; 188 -5.4; 201 -5.5; 215 -5.5; 230 -5.2; 246 -4.9; 263 -4.5; 282 -3.8; 301 -3.0; 323 -2.3; 345 -1.7; 369 -1.1; 395 -0.6; 423 0.1; 452 0.4; 484 0.5; 518 0.4; 554 0.5; 593 0.6; 635 0.4; 679 0.2; 726 0.1; 777 0.2; 832 0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.5; 1429 -0.9; 1529 -1.4; 1636 -1.8; 1751 -2.0; 1873 -2.3; 2004 -2.3; 2145 -2.6; 2295 -3.2; 2455 -2.8; 2627 -2.2; 2811 -1.8; 3008 -1.5; 3219 -1.0; 3444 -0.1; 3685 0.3; 3943 1.5; 4219 1.7; 4514 1.8; 4830 2.1; 5168 2.8; 5530 2.7; 5917 3.3; 6331 3.7; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -0.2; 18692 -0.7; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.728873914251751dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.1  | 4.3 dB  |
| Peaking | 42 Hz   | 1.8  | 1.4 dB  |
| Peaking | 175 Hz  | 1    | -5.9 dB |
| Peaking | 2278 Hz | 1.95 | -3.3 dB |
| Peaking | 5710 Hz | 1.9  | 3.7 dB  |
| Peaking | 175 Hz  | 2.19 | 2.4 dB  |
| Peaking | 238 Hz  | 0.79 | -2.5 dB |
| Peaking | 445 Hz  | 1.15 | 2.5 dB  |
| Peaking | 4042 Hz | 9.8  | 1.0 dB  |
| Peaking | 8401 Hz | 4.47 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5/Bowers%20&%20Wilkins%20P5.png)