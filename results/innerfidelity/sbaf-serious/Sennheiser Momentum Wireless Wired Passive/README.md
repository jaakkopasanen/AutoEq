# Sennheiser Momentum Wireless Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.5; 22 2.1; 23 1.9; 25 1.5; 26 1.3; 28 1.1; 30 0.8; 32 0.6; 35 0.4; 37 0.2; 40 0.1; 42 -0.1; 45 -0.2; 49 -0.4; 52 -0.5; 56 -0.6; 59 -0.7; 64 -0.9; 68 -1.1; 73 -1.3; 78 -1.5; 83 -1.7; 89 -1.9; 95 -2.2; 102 -2.3; 109 -2.2; 117 -2.3; 125 -2.2; 134 -2.1; 143 -1.9; 153 -2.1; 164 -2.1; 175 -1.4; 188 -1.1; 201 -1.0; 215 -0.7; 230 -0.2; 246 0.2; 263 0.4; 282 0.9; 301 1.5; 323 2.0; 345 2.2; 369 2.0; 395 1.6; 423 1.4; 452 1.1; 484 0.8; 518 0.6; 554 0.5; 593 0.5; 635 0.5; 679 0.3; 726 0.3; 777 0.5; 832 0.4; 890 0.2; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.8; 1636 -1.9; 1751 -1.8; 1873 -2.1; 2004 -1.7; 2145 -1.1; 2295 -0.2; 2455 1.0; 2627 2.0; 2811 3.2; 3008 4.6; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 2.0; 5168 2.5; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230118dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.93 | 3.2 dB  |
| Peaking | 122 Hz  | 0.7  | -2.5 dB |
| Peaking | 340 Hz  | 1.9  | 2.8 dB  |
| Peaking | 3715 Hz | 2.5  | 6.8 dB  |
| Peaking | 6047 Hz | 4.43 | 5.7 dB  |
| Peaking | 1811 Hz | 2.14 | -2.8 dB |
| Peaking | 2965 Hz | 4.76 | 2.0 dB  |
| Peaking | 6710 Hz | 8.44 | 1.5 dB  |
| Peaking | 7792 Hz | 2.68 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Passive/Sennheiser%20Momentum%20Wireless%20Wired%20Passive.png)