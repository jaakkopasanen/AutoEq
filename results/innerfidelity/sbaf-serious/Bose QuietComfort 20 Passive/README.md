# Bose QuietComfort 20 Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.2; 37 4.6; 40 3.7; 42 3.2; 45 2.4; 49 1.5; 52 0.9; 56 0.1; 59 -0.4; 64 -1.2; 68 -1.8; 73 -2.4; 78 -2.9; 83 -3.4; 89 -3.8; 95 -4.1; 102 -4.3; 109 -4.3; 117 -4.2; 125 -4.1; 134 -3.9; 143 -3.7; 153 -3.3; 164 -2.9; 175 -2.5; 188 -2.3; 201 -2.3; 215 -2.4; 230 -2.8; 246 -3.2; 263 -3.5; 282 -3.7; 301 -3.7; 323 -3.4; 345 -2.8; 369 -2.1; 395 -1.3; 423 -0.4; 452 0.4; 484 1.1; 518 1.8; 554 2.5; 593 2.9; 635 2.9; 679 2.7; 726 2.5; 777 2.2; 832 1.7; 890 1.1; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -1.9; 1336 -2.8; 1429 -3.7; 1529 -4.1; 1636 -3.7; 1751 -1.9; 1873 0.3; 2004 2.8; 2145 5.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.4; 3943 1.2; 4219 -0.4; 4514 2.1; 4830 5.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 0.0; 7756 -1.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.62 | 9.8 dB   |
| Peaking | 82 Hz    | 0.35 | -6.4 dB  |
| Peaking | 1524 Hz  | 1.77 | -15.1 dB |
| Peaking | 1863 Hz  | 0.64 | 11.0 dB  |
| Peaking | 5785 Hz  | 4.95 | 4.6 dB   |
| Peaking | 190 Hz   | 2.93 | 1.6 dB   |
| Peaking | 307 Hz   | 2.19 | -2.3 dB  |
| Peaking | 580 Hz   | 2.8  | 2.6 dB   |
| Peaking | 7879 Hz  | 5.47 | -2.6 dB  |
| Peaking | 21356 Hz | 1.76 | -0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Passive/Bose%20QuietComfort%2020%20Passive.png)