# Beats Solo3 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 10 -84; 20 -5.7; 22 -5.9; 23 -6.0; 25 -6.1; 26 -6.1; 28 -6.2; 30 -6.2; 32 -6.3; 35 -6.4; 37 -6.4; 40 -6.4; 42 -6.4; 45 -6.4; 49 -6.5; 52 -6.5; 56 -6.6; 59 -6.6; 64 -6.8; 68 -6.8; 73 -6.9; 78 -7.1; 83 -7.1; 89 -7.3; 95 -7.4; 102 -7.8; 109 -7.9; 117 -7.8; 125 -7.9; 134 -7.8; 143 -8.1; 153 -8.2; 164 -7.9; 175 -7.8; 188 -8.0; 201 -7.8; 215 -7.5; 230 -7.2; 246 -6.9; 263 -6.5; 282 -5.9; 301 -5.3; 323 -4.7; 345 -4.3; 369 -3.7; 395 -2.9; 423 -2.3; 452 -2.1; 484 -2.0; 518 -1.8; 554 -1.2; 593 -0.5; 635 -0.1; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.5; 1636 -1.7; 1751 -1.8; 1873 -1.4; 2004 -1.0; 2145 -0.9; 2295 -1.0; 2455 -0.8; 2627 -1.0; 2811 -1.5; 3008 -1.8; 3219 -2.4; 3444 -2.7; 3685 -2.0; 3943 -0.4; 4219 -0.8; 4514 -2.5; 4830 -1.9; 5168 0.1; 5530 2.1; 5917 2.6; 6331 1.6; 6775 1.6; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.1; 18692 -0.9; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.7946855057746016dB` and instead set Global volume in the UI for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.6dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.29 | -5.9 dB |
| Peaking | 136 Hz  |  0.85 | -4.6 dB |
| Peaking | 247 Hz  |  1.35 | -3.9 dB |
| Peaking | 4009 Hz |  0.84 | -2.5 dB |
| Peaking | 5986 Hz |  2.73 | 4.1 dB  |
| Peaking | 786 Hz  |  2.63 | 1.4 dB  |
| Peaking | 1630 Hz |  3.21 | -1.2 dB |
| Peaking | 2473 Hz |  6.21 | 0.7 dB  |
| Peaking | 4049 Hz | 11.75 | 2.1 dB  |
| Peaking | 4641 Hz |  9.08 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wired/Beats%20Solo3%20Wired.png)