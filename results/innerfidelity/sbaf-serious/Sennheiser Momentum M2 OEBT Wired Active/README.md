# Sennheiser Momentum M2 OEBT Wired Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.3; 22 4.8; 23 4.5; 25 4.0; 26 3.7; 28 3.2; 30 2.7; 32 2.2; 35 1.5; 37 1.2; 40 0.7; 42 0.3; 45 -0.4; 49 -1.2; 52 -1.9; 56 -2.7; 59 -3.2; 64 -4.0; 68 -4.3; 73 -4.5; 78 -4.8; 83 -5.4; 89 -6.0; 95 -6.1; 102 -5.7; 109 -5.1; 117 -4.4; 125 -3.7; 134 -2.9; 143 -2.2; 153 -1.5; 164 -0.8; 175 -0.3; 188 0.1; 201 0.4; 215 0.8; 230 1.2; 246 1.6; 263 2.1; 282 2.6; 301 3.1; 323 3.7; 345 3.9; 369 3.8; 395 3.7; 423 3.5; 452 3.3; 484 3.1; 518 2.9; 554 2.9; 593 2.8; 635 2.4; 679 1.9; 726 1.6; 777 1.4; 832 0.9; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.2; 1429 -1.9; 1529 -2.7; 1636 -3.3; 1751 -3.8; 1873 -4.3; 2004 -4.7; 2145 -4.7; 2295 -4.9; 2455 -4.1; 2627 -3.2; 2811 -2.5; 3008 -0.8; 3219 0.8; 3444 2.3; 3685 3.7; 3943 5.8; 4219 6.0; 4514 5.6; 4830 3.1; 5168 1.3; 5530 2.9; 5917 4.3; 6331 3.1; 6775 0.9; 7249 0.2; 7756 -0.6; 8299 -2.1; 8880 -3.8; 9502 -3.6; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999977423100935dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.83 | 5.5 dB  |
| Peaking | 91 Hz   | 0.96 | -6.8 dB |
| Peaking | 380 Hz  | 0.67 | 4.3 dB  |
| Peaking | 2219 Hz | 1.13 | -6.1 dB |
| Peaking | 4093 Hz | 2.1  | 7.9 dB  |
| Peaking | 5130 Hz | 9.06 | -2.4 dB |
| Peaking | 5953 Hz | 5.3  | 3.4 dB  |
| Peaking | 8999 Hz | 4.89 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active.png)