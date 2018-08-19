# RHA T10i Treble Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.7; 22 -9.7; 23 -9.7; 25 -9.8; 26 -9.9; 28 -10.2; 30 -10.4; 32 -10.6; 35 -10.7; 37 -10.7; 40 -10.7; 42 -10.8; 45 -10.9; 49 -11.0; 52 -11.0; 56 -11.1; 59 -11.1; 64 -11.2; 68 -11.2; 73 -11.2; 78 -11.3; 83 -11.4; 89 -11.4; 95 -11.5; 102 -11.4; 109 -11.3; 117 -11.1; 125 -11.0; 134 -10.9; 143 -10.7; 153 -10.5; 164 -10.3; 175 -9.9; 188 -9.6; 201 -9.3; 215 -8.9; 230 -8.5; 246 -8.1; 263 -7.7; 282 -7.2; 301 -6.7; 323 -6.3; 345 -5.8; 369 -5.3; 395 -4.9; 423 -4.3; 452 -3.8; 484 -3.5; 518 -3.0; 554 -2.5; 593 -1.8; 635 -1.3; 679 -1.3; 726 -1.1; 777 -0.6; 832 -0.2; 890 0.0; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.5; 1636 -3.2; 1751 -3.8; 1873 -4.3; 2004 -5.0; 2145 -5.9; 2295 -6.8; 2455 -7.0; 2627 -6.4; 2811 -5.3; 3008 -3.7; 3219 -2.4; 3444 -1.7; 3685 -1.6; 3943 -0.2; 4219 1.1; 4514 3.7; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -2.3; 8299 -9.6; 8880 -13.0; 9502 -13.2; 10167 -10.5; 10879 -4.4; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099566618642663dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.24 | -10.4 dB |
| Peaking | 187 Hz   | 0.64 | -4.9 dB  |
| Peaking | 2472 Hz  | 1.68 | -7.8 dB  |
| Peaking | 5882 Hz  | 1.48 | 9.4 dB   |
| Peaking | 9113 Hz  | 3.22 | -17.8 dB |
| Peaking | 916 Hz   | 1.22 | 3.4 dB   |
| Peaking | 924 Hz   | 0.64 | -1.9 dB  |
| Peaking | 10285 Hz | 6.88 | -4.4 dB  |
| Peaking | 11493 Hz | 4.4  | 3.2 dB   |
| Peaking | 13312 Hz | 1.75 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Treble%20Filter/RHA%20T10i%20Treble%20Filter.png)