# RHA T20 Treble Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 -4.9; 22 -5.2; 23 -5.3; 25 -5.5; 26 -5.6; 28 -5.8; 30 -5.9; 32 -6.0; 35 -6.1; 37 -6.1; 40 -6.2; 42 -6.2; 45 -6.2; 49 -6.2; 52 -6.2; 56 -6.2; 59 -6.3; 64 -6.3; 68 -6.3; 73 -6.3; 78 -6.3; 83 -6.4; 89 -6.4; 95 -6.4; 102 -6.3; 109 -6.1; 117 -6.0; 125 -5.9; 134 -5.7; 143 -5.6; 153 -5.4; 164 -5.2; 175 -4.9; 188 -4.6; 201 -4.3; 215 -4.0; 230 -3.7; 246 -3.4; 263 -3.1; 282 -2.7; 301 -2.4; 323 -2.1; 345 -1.6; 369 -1.4; 395 -1.0; 423 -0.6; 452 -0.4; 484 -0.2; 518 0.0; 554 0.4; 593 0.8; 635 1.0; 679 1.0; 726 1.0; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.6; 1336 -2.6; 1429 -3.6; 1529 -4.3; 1636 -4.0; 1751 -2.0; 1873 -0.1; 2004 -2.1; 2145 -3.3; 2295 -4.0; 2455 -5.0; 2627 -5.9; 2811 -6.4; 3008 -5.6; 3219 -4.5; 3444 -3.3; 3685 -3.4; 3943 -4.8; 4219 -7.7; 4514 -10.8; 4830 -10.6; 5168 -6.3; 5530 -1.4; 5917 2.1; 6331 4.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -1.1; 15258 -0.3; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.656032004556693dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.42 | -5.8 dB  |
| Peaking | 112 Hz  | 0.95 | -3.5 dB  |
| Peaking | 208 Hz  | 1.59 | -2.2 dB  |
| Peaking | 2688 Hz | 1.89 | -5.8 dB  |
| Peaking | 4625 Hz | 6.24 | -11.5 dB |
| Peaking | 747 Hz  | 1.78 | 1.8 dB   |
| Peaking | 1561 Hz | 3.05 | -4.3 dB  |
| Peaking | 1857 Hz | 5.98 | 3.6 dB   |
| Peaking | 5036 Hz | 6.33 | -3.0 dB  |
| Peaking | 6340 Hz | 4.33 | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Treble%20Filter/RHA%20T20%20Treble%20Filter.png)