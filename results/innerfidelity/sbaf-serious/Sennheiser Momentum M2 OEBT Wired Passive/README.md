# Sennheiser Momentum M2 OEBT Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.8; 23 -2.0; 25 -2.3; 26 -2.5; 28 -2.8; 30 -3.0; 32 -3.2; 35 -3.5; 37 -3.6; 40 -3.9; 42 -4.0; 45 -4.3; 49 -4.6; 52 -4.8; 56 -5.0; 59 -5.2; 64 -5.2; 68 -5.0; 73 -4.9; 78 -5.7; 83 -6.5; 89 -6.5; 95 -6.1; 102 -5.6; 109 -5.8; 117 -6.8; 125 -7.6; 134 -7.9; 143 -8.0; 153 -7.7; 164 -6.9; 175 -7.0; 188 -6.5; 201 -5.6; 215 -4.4; 230 -3.0; 246 -1.7; 263 -0.6; 282 0.4; 301 1.0; 323 1.3; 345 1.2; 369 0.7; 395 0.2; 423 0.1; 452 0.3; 484 0.3; 518 0.4; 554 0.6; 593 0.7; 635 0.7; 679 0.6; 726 0.5; 777 0.6; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.9; 1429 -1.5; 1529 -2.1; 1636 -2.7; 1751 -3.0; 1873 -3.4; 2004 -3.5; 2145 -3.4; 2295 -3.4; 2455 -2.8; 2627 -1.9; 2811 -1.3; 3008 0.0; 3219 1.3; 3444 2.8; 3685 3.9; 3943 5.8; 4219 6.0; 4514 4.8; 4830 1.6; 5168 0.3; 5530 2.2; 5917 3.3; 6331 2.2; 6775 -0.2; 7249 -1.0; 7756 -1.7; 8299 -3.0; 8880 -4.9; 9502 -5.1; 10167 -1.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099997742310093dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 1.16 | -4.2 dB |
| Peaking | 67 Hz   | 0.75 | -5.1 dB |
| Peaking | 151 Hz  | 1.86 | -6.6 dB |
| Peaking | 4109 Hz | 4.46 | 6.9 dB  |
| Peaking | 9039 Hz | 5.01 | -5.9 dB |
| Peaking | 203 Hz  | 4.73 | -2.1 dB |
| Peaking | 308 Hz  | 2.95 | 2.4 dB  |
| Peaking | 798 Hz  | 0.72 | 1.0 dB  |
| Peaking | 2129 Hz | 1.2  | -6.1 dB |
| Peaking | 2991 Hz | 0.72 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Passive.png)