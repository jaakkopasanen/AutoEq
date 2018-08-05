# Massdrop x AKG K7XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 0.9; 22 0.4; 23 0.2; 25 -0.2; 26 -0.4; 28 -0.7; 30 -1.0; 32 -1.3; 35 -1.6; 37 -1.7; 40 -1.9; 42 -2.1; 45 -2.2; 49 -2.4; 52 -2.5; 56 -2.6; 59 -2.7; 64 -2.9; 68 -2.9; 73 -3.0; 78 -3.2; 83 -3.4; 89 -3.7; 95 -4.0; 102 -4.3; 109 -4.5; 117 -4.9; 125 -5.2; 134 -5.4; 143 -5.5; 153 -5.5; 164 -5.8; 175 -5.5; 188 -5.2; 201 -5.2; 215 -5.2; 230 -5.2; 246 -5.1; 263 -5.1; 282 -5.0; 301 -4.9; 323 -4.7; 345 -4.5; 369 -4.3; 395 -4.1; 423 -3.7; 452 -3.3; 484 -3.1; 518 -2.8; 554 -2.3; 593 -1.7; 635 -1.2; 679 -0.9; 726 -0.3; 777 0.2; 832 0.5; 890 0.6; 952 0.2; 1019 0.1; 1090 -0.3; 1167 -0.7; 1248 -1.0; 1336 -1.6; 1429 -2.5; 1529 -3.6; 1636 -4.7; 1751 -5.3; 1873 -5.6; 2004 -5.7; 2145 -5.0; 2295 -3.8; 2455 -1.4; 2627 0.6; 2811 2.5; 3008 3.6; 3219 3.6; 3444 2.9; 3685 1.3; 3943 0.1; 4219 -0.9; 4514 -1.4; 4830 -0.6; 5168 1.0; 5530 2.0; 5917 1.1; 6331 0.2; 6775 -1.8; 7249 -2.8; 7756 -3.2; 8299 -4.3; 8880 -4.7; 9502 -2.6; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -3.0; 18692 -3.6; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x AKG K7XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 173 Hz   | 0.47 | -5.7 dB |
| Peaking | 1947 Hz  | 2.5  | -6.6 dB |
| Peaking | 3056 Hz  | 3.49 | 5.2 dB  |
| Peaking | 8459 Hz  | 4.02 | -5.0 dB |
| Peaking | 29532 Hz | 3.16 | -4.4 dB |
| Peaking | 17 Hz    | 0.32 | 1.8 dB  |
| Peaking | 37 Hz    | 1    | -2.1 dB |
| Peaking | 866 Hz   | 3.35 | 2.0 dB  |
| Peaking | 4454 Hz  | 6    | -1.9 dB |
| Peaking | 5524 Hz  | 6.81 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20AKG%20K7XX/Massdrop%20x%20AKG%20K7XX.png)