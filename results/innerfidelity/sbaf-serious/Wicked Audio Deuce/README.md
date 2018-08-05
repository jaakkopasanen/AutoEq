# Wicked Audio Deuce

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 10 -84; 20 -13.9; 22 -13.8; 23 -13.7; 25 -13.6; 26 -13.5; 28 -13.4; 30 -13.3; 32 -13.1; 35 -12.9; 37 -12.7; 40 -12.5; 42 -12.4; 45 -12.1; 49 -11.8; 52 -11.6; 56 -11.3; 59 -11.1; 64 -10.8; 68 -10.6; 73 -10.3; 78 -10.2; 83 -10.1; 89 -10.1; 95 -10.2; 102 -10.3; 109 -10.4; 117 -10.5; 125 -10.7; 134 -10.7; 143 -10.6; 153 -10.4; 164 -10.1; 175 -9.7; 188 -9.3; 201 -8.9; 215 -8.4; 230 -7.9; 246 -7.4; 263 -7.0; 282 -6.4; 301 -5.9; 323 -5.4; 345 -4.9; 369 -4.4; 395 -4.0; 423 -3.3; 452 -2.9; 484 -2.5; 518 -2.1; 554 -1.5; 593 -0.9; 635 -0.6; 679 -0.5; 726 -0.3; 777 -0.2; 832 0.3; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.8; 1336 -1.0; 1429 -1.5; 1529 -2.3; 1636 -3.0; 1751 -3.8; 1873 -4.5; 2004 -5.0; 2145 -5.4; 2295 -5.7; 2455 -5.5; 2627 -5.3; 2811 -4.6; 3008 -2.9; 3219 -1.6; 3444 -0.1; 3685 0.4; 3943 -0.3; 4219 -1.8; 4514 -3.5; 4830 -4.9; 5168 -6.5; 5530 -10.2; 5917 -12.7; 6331 -8.6; 6775 -4.9; 7249 -3.1; 7756 -3.0; 8299 -4.6; 8880 -6.2; 9502 -6.1; 10167 -3.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.0dB` and instead set Global volume in the UI for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Wicked Audio Deuce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 1.01 | -13.7 dB |
| Peaking | 31 Hz   | 0.31 | -11.0 dB |
| Peaking | 175 Hz  | 0.73 | -6.8 dB  |
| Peaking | 2225 Hz | 2.37 | -5.9 dB  |
| Peaking | 5898 Hz | 3.15 | -12.0 dB |
| Peaking | 861 Hz  | 2.22 | 1.4 dB   |
| Peaking | 1711 Hz | 4.05 | -1.3 dB  |
| Peaking | 7163 Hz | 5.67 | 1.4 dB   |
| Peaking | 7995 Hz | 0.37 | 0.8 dB   |
| Peaking | 9142 Hz | 4.02 | -6.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Wicked%20Audio%20Deuce/Wicked%20Audio%20Deuce.png)