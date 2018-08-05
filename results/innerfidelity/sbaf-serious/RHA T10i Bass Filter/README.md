# RHA T10i Bass Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -9.7; 22 -9.9; 23 -10.0; 25 -10.1; 26 -10.2; 28 -10.3; 30 -10.4; 32 -10.5; 35 -10.5; 37 -10.5; 40 -10.5; 42 -10.4; 45 -10.4; 49 -10.3; 52 -10.3; 56 -10.1; 59 -10.0; 64 -9.9; 68 -9.8; 73 -9.7; 78 -9.7; 83 -9.7; 89 -9.8; 95 -10.1; 102 -10.3; 109 -10.4; 117 -10.7; 125 -10.9; 134 -11.1; 143 -11.1; 153 -11.0; 164 -10.8; 175 -10.4; 188 -10.1; 201 -9.7; 215 -9.2; 230 -8.8; 246 -8.3; 263 -7.9; 282 -7.3; 301 -6.9; 323 -6.3; 345 -5.9; 369 -5.4; 395 -4.9; 423 -4.3; 452 -3.8; 484 -3.5; 518 -3.0; 554 -2.5; 593 -1.8; 635 -1.4; 679 -1.3; 726 -1.1; 777 -0.6; 832 -0.2; 890 0.1; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.8; 1529 -2.4; 1636 -2.9; 1751 -3.3; 1873 -3.5; 2004 -3.6; 2145 -3.6; 2295 -3.2; 2455 -2.3; 2627 -1.3; 2811 -0.3; 3008 0.8; 3219 1.3; 3444 1.3; 3685 1.3; 3943 2.4; 4219 3.3; 4514 5.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.0; 8299 -7.6; 8880 -10.9; 9502 -11.4; 10167 -9.6; 10879 -4.3; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.24 | -9.8 dB  |
| Peaking | 183 Hz   | 0.65 | -7.6 dB  |
| Peaking | 2061 Hz  | 2    | -4.6 dB  |
| Peaking | 5846 Hz  | 1.18 | 8.4 dB   |
| Peaking | 9163 Hz  | 2.95 | -16.0 dB |
| Peaking | 939 Hz   | 2.54 | 1.5 dB   |
| Peaking | 1797 Hz  | 1.93 | -1.3 dB  |
| Peaking | 1977 Hz  | 4.5  | 1.5 dB   |
| Peaking | 10333 Hz | 6.81 | -4.5 dB  |
| Peaking | 11447 Hz | 3.06 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Bass%20Filter/RHA%20T10i%20Bass%20Filter.png)