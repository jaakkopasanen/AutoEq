# Sony XBA-N3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.3; 23 -4.4; 25 -4.5; 26 -4.6; 28 -4.7; 30 -4.8; 32 -4.8; 35 -4.9; 37 -4.9; 40 -4.9; 42 -4.9; 45 -4.9; 49 -4.9; 52 -4.9; 56 -4.8; 59 -4.8; 64 -4.8; 68 -4.8; 73 -4.8; 78 -4.8; 83 -4.7; 89 -4.7; 95 -4.5; 102 -4.3; 109 -4.2; 117 -4.6; 125 -4.9; 134 -4.9; 143 -4.9; 153 -4.8; 164 -4.5; 175 -4.3; 188 -4.0; 201 -3.8; 215 -3.5; 230 -3.2; 246 -2.9; 263 -2.6; 282 -2.4; 301 -2.0; 323 -1.7; 345 -1.3; 369 -1.0; 395 -0.8; 423 -0.6; 452 -0.4; 484 -0.2; 518 0.0; 554 0.2; 593 0.3; 635 0.4; 679 0.6; 726 0.7; 777 0.7; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -0.9; 1336 -0.9; 1429 -0.6; 1529 0.4; 1636 1.2; 1751 1.0; 1873 1.0; 2004 1.2; 2145 1.8; 2295 2.6; 2455 3.4; 2627 4.2; 2811 5.0; 3008 5.6; 3219 5.7; 3444 4.8; 3685 3.3; 3943 2.6; 4219 3.7; 4514 3.8; 4830 2.9; 5168 3.2; 5530 4.3; 5917 5.1; 6331 4.8; 6775 3.1; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -1.5; 9502 -2.3; 10167 -2.6; 10879 -2.2; 11640 -1.5; 12455 -2.1; 13327 -5.8; 14260 -12.7; 15258 -19.7; 16326 -22.6; 17469 -20.3; 18692 -14.2; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.33 | -4.8 dB  |
| Peaking | 166 Hz   | 1.01 | -2.9 dB  |
| Peaking | 3016 Hz  | 3.1  | 3.9 dB   |
| Peaking | 9290 Hz  | 0.38 | 7.5 dB   |
| Peaking | 16447 Hz | 1.05 | -28.6 dB |
| Peaking | 1299 Hz  | 4.86 | -1.8 dB  |
| Peaking | 6109 Hz  | 4.2  | 3.4 dB   |
| Peaking | 9414 Hz  | 1.34 | -3.3 dB  |
| Peaking | 12437 Hz | 2.54 | 5.7 dB   |
| Peaking | 14931 Hz | 5.06 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-N3/Sony%20XBA-N3.png)