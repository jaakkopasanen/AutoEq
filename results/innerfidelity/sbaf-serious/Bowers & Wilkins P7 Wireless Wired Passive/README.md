# Bowers & Wilkins P7 Wireless Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.0; 22 4.4; 23 4.2; 25 3.8; 26 3.6; 28 3.3; 30 3.0; 32 2.8; 35 2.5; 37 2.4; 40 2.2; 42 2.1; 45 1.9; 49 1.8; 52 1.7; 56 1.6; 59 1.5; 64 1.4; 68 1.2; 73 1.0; 78 0.8; 83 0.8; 89 0.6; 95 0.4; 102 0.3; 109 0.3; 117 0.3; 125 0.2; 134 0.2; 143 0.3; 153 0.2; 164 0.1; 175 0.5; 188 0.8; 201 0.8; 215 1.0; 230 1.1; 246 1.2; 263 1.4; 282 1.5; 301 1.5; 323 1.7; 345 1.8; 369 2.0; 395 2.0; 423 1.9; 452 1.8; 484 1.7; 518 1.7; 554 1.8; 593 1.9; 635 1.7; 679 1.4; 726 1.1; 777 1.0; 832 0.7; 890 0.4; 952 0.1; 1019 0.2; 1090 0.2; 1167 -0.3; 1248 -1.0; 1336 -1.7; 1429 -2.5; 1529 -3.1; 1636 -3.6; 1751 -3.9; 1873 -3.9; 2004 -3.5; 2145 -3.3; 2295 -3.3; 2455 -2.5; 2627 -1.5; 2811 -0.0; 3008 3.7; 3219 6.0; 3444 4.4; 3685 2.2; 3943 1.0; 4219 0.8; 4514 1.0; 4830 1.3; 5168 2.5; 5530 2.1; 5917 0.5; 6331 3.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.081140761822153dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.52 | 5.1 dB  |
| Peaking | 502 Hz  | 0.67 | 2.1 dB  |
| Peaking | 1946 Hz | 1.3  | -4.8 dB |
| Peaking | 3248 Hz | 4.35 | 7.5 dB  |
| Peaking | 6584 Hz | 5.05 | 4.1 dB  |
| Peaking | 133 Hz  | 2.61 | -0.4 dB |
| Peaking | 2054 Hz | 5.26 | 1.6 dB  |
| Peaking | 2182 Hz | 2.18 | -1.0 dB |
| Peaking | 5306 Hz | 5.55 | 2.5 dB  |
| Peaking | 5907 Hz | 8.77 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive.png)