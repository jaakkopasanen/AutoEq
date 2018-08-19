# Sennheiser Momentum On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.6; 23 -3.7; 25 -3.8; 26 -3.8; 28 -3.9; 30 -4.0; 32 -4.1; 35 -4.3; 37 -4.3; 40 -4.4; 42 -4.4; 45 -4.4; 49 -4.5; 52 -4.5; 56 -4.5; 59 -4.5; 64 -4.5; 68 -4.4; 73 -4.4; 78 -4.4; 83 -4.5; 89 -4.6; 95 -4.6; 102 -4.6; 109 -4.5; 117 -4.5; 125 -4.5; 134 -4.5; 143 -4.4; 153 -4.2; 164 -3.9; 175 -3.5; 188 -3.3; 201 -2.9; 215 -2.4; 230 -1.9; 246 -1.2; 263 -0.6; 282 0.1; 301 0.7; 323 1.0; 345 1.3; 369 1.5; 395 1.6; 423 1.8; 452 1.9; 484 1.6; 518 1.4; 554 1.2; 593 1.0; 635 0.5; 679 0.1; 726 -0.2; 777 -0.1; 832 -0.0; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -2.8; 1429 -3.7; 1529 -4.4; 1636 -5.1; 1751 -5.4; 1873 -5.3; 2004 -4.6; 2145 -3.8; 2295 -2.9; 2455 -1.4; 2627 0.1; 2811 1.2; 3008 2.3; 3219 3.1; 3444 4.2; 3685 5.3; 3943 6.0; 4219 6.0; 4514 5.1; 4830 0.9; 5168 1.1; 5530 2.4; 5917 2.7; 6331 1.4; 6775 -0.1; 7249 -0.9; 7756 -1.0; 8299 -1.6; 8880 -2.5; 9502 -1.9; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999254591366dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.53 | -4.6 dB |
| Peaking | 134 Hz   | 1.55 | -3.4 dB |
| Peaking | 1811 Hz  | 2.13 | -6.4 dB |
| Peaking | 3885 Hz  | 2.1  | 6.6 dB  |
| Peaking | 8774 Hz  | 4.01 | -2.9 dB |
| Peaking | 14 Hz    | 1.51 | -1.4 dB |
| Peaking | 206 Hz   | 2.99 | -1.3 dB |
| Peaking | 323 Hz   | 2.47 | 1.1 dB  |
| Peaking | 456 Hz   | 1.77 | 2.0 dB  |
| Peaking | 24000 Hz | 1.97 | -0.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)