# Fischer Audio Tandem

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.8; 64 5.4; 68 5.1; 73 4.7; 78 4.3; 83 3.8; 89 3.2; 95 2.5; 102 1.8; 109 1.1; 117 0.5; 125 -0.4; 134 -0.9; 143 -1.4; 153 -1.7; 164 -1.9; 175 -2.1; 188 -2.1; 201 -2.2; 215 -2.2; 230 -2.2; 246 -2.2; 263 -2.2; 282 -2.1; 301 -2.0; 323 -1.9; 345 -1.8; 369 -1.6; 395 -1.5; 423 -1.3; 452 -1.1; 484 -1.1; 518 -0.9; 554 -0.6; 593 -0.2; 635 -0.0; 679 -0.1; 726 -0.0; 777 0.1; 832 0.3; 890 0.2; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.1; 1336 0.0; 1429 0.1; 1529 0.2; 1636 0.3; 1751 0.7; 1873 1.3; 2004 2.1; 2145 2.9; 2295 3.8; 2455 5.2; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.7; 4514 2.3; 4830 3.3; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Tandem ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.29 | 7.7 dB  |
| Peaking | 166 Hz  | 0.59 | -6.5 dB |
| Peaking | 3082 Hz | 1.62 | 6.6 dB  |
| Peaking | 5837 Hz | 3.55 | 5.6 dB  |
| Peaking | 1652 Hz | 1.38 | -2.5 dB |
| Peaking | 2228 Hz | 0.66 | 2.1 dB  |
| Peaking | 3046 Hz | 5.82 | -2.0 dB |
| Peaking | 6591 Hz | 6.98 | 2.5 dB  |
| Peaking | 7136 Hz | 1.38 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20Tandem/Fischer%20Audio%20Tandem.png)