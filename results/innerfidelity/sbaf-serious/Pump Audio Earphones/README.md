# Pump Audio Earphones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 -13.9; 22 -13.9; 23 -13.9; 25 -13.9; 26 -13.8; 28 -13.8; 30 -13.7; 32 -13.6; 35 -13.5; 37 -13.4; 40 -13.2; 42 -13.1; 45 -13.0; 49 -12.7; 52 -12.6; 56 -12.4; 59 -12.2; 64 -11.9; 68 -11.8; 73 -11.6; 78 -11.5; 83 -11.4; 89 -11.4; 95 -11.6; 102 -11.7; 109 -11.8; 117 -11.9; 125 -12.2; 134 -12.2; 143 -12.1; 153 -11.9; 164 -11.6; 175 -11.3; 188 -10.8; 201 -10.4; 215 -9.9; 230 -9.4; 246 -8.9; 263 -8.4; 282 -7.8; 301 -7.3; 323 -6.8; 345 -6.3; 369 -5.7; 395 -5.2; 423 -4.5; 452 -4.0; 484 -3.6; 518 -3.1; 554 -2.5; 593 -1.4; 635 -1.0; 679 -0.8; 726 -0.4; 777 0.1; 832 0.2; 890 0.2; 952 0.1; 1019 0.0; 1090 0.1; 1167 -0.0; 1248 -0.0; 1336 -0.3; 1429 -0.8; 1529 -1.1; 1636 -1.7; 1751 -2.3; 1873 -2.9; 2004 -2.9; 2145 -3.1; 2295 -3.0; 2455 -2.3; 2627 -1.9; 2811 -1.0; 3008 0.5; 3219 1.7; 3444 2.6; 3685 2.2; 3943 1.1; 4219 -1.4; 4514 -4.3; 4830 -7.6; 5168 -9.6; 5530 -5.4; 5917 0.3; 6331 3.2; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.7dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pump Audio Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 7 Hz    | 1.03 | -13.8 dB |
| Peaking | 29 Hz   | 0.23 | -12.1 dB |
| Peaking | 185 Hz  | 0.7  | -7.0 dB  |
| Peaking | 2077 Hz | 3.77 | -3.4 dB  |
| Peaking | 5067 Hz | 7.81 | -10.6 dB |
| Peaking | 844 Hz  | 2.45 | 1.5 dB   |
| Peaking | 2628 Hz | 3.71 | -1.6 dB  |
| Peaking | 3575 Hz | 2.6  | 5.7 dB   |
| Peaking | 4615 Hz | 1.38 | -3.5 dB  |
| Peaking | 6531 Hz | 4.92 | 6.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pump%20Audio%20Earphones/Pump%20Audio%20Earphones.png)