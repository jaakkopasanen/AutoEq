# Sennheiser Momentum On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.3; 22 -2.5; 23 -2.6; 25 -2.8; 26 -2.8; 28 -3.0; 30 -3.0; 32 -3.1; 35 -3.3; 37 -3.3; 40 -3.4; 42 -3.4; 45 -3.5; 49 -3.5; 52 -3.6; 56 -3.7; 59 -3.8; 64 -3.9; 68 -3.9; 73 -3.8; 78 -3.6; 83 -3.5; 89 -3.7; 95 -4.1; 102 -4.3; 109 -4.3; 117 -4.3; 125 -4.3; 134 -4.2; 143 -4.1; 153 -3.9; 164 -3.6; 175 -3.4; 188 -3.1; 201 -2.6; 215 -2.2; 230 -1.6; 246 -0.9; 263 -0.1; 282 0.6; 301 0.8; 323 1.2; 345 1.7; 369 1.9; 395 2.1; 423 2.0; 452 2.0; 484 1.8; 518 1.6; 554 1.4; 593 1.1; 635 0.8; 679 0.6; 726 0.4; 777 0.4; 832 0.3; 890 0.3; 952 0.3; 1019 -0.0; 1090 -0.5; 1167 -1.1; 1248 -1.9; 1336 -2.9; 1429 -3.6; 1529 -4.5; 1636 -5.4; 1751 -5.6; 1873 -5.4; 2004 -4.9; 2145 -4.2; 2295 -3.2; 2455 -1.9; 2627 -0.4; 2811 0.8; 3008 1.9; 3219 2.8; 3444 3.9; 3685 5.1; 3943 6.0; 4219 6.0; 4514 5.1; 4830 0.5; 5168 0.8; 5530 2.3; 5917 2.6; 6331 1.0; 6775 -1.9; 7249 -3.7; 7756 -3.4; 8299 -2.7; 8880 -2.8; 9502 -2.1; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999017734477dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.62 | -3.7 dB |
| Peaking | 132 Hz   | 1.64 | -3.6 dB |
| Peaking | 1828 Hz  | 2.12 | -6.6 dB |
| Peaking | 3936 Hz  | 2.13 | 6.7 dB  |
| Peaking | 7835 Hz  | 3.1  | -4.3 dB |
| Peaking | 17 Hz    | 1.56 | -0.9 dB |
| Peaking | 202 Hz   | 2.75 | -1.6 dB |
| Peaking | 333 Hz   | 1.73 | 0.7 dB  |
| Peaking | 434 Hz   | 1.22 | 2.1 dB  |
| Peaking | 21279 Hz | 2.03 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)