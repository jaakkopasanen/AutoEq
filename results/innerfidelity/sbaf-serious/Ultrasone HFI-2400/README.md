# Ultrasone HFI-2400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.1dB
GraphicEQ: 10 -84; 20 6.6; 22 5.5; 23 4.9; 25 4.0; 26 3.5; 28 2.7; 30 1.9; 32 1.2; 35 0.2; 37 -0.4; 40 -1.1; 42 -1.5; 45 -2.0; 49 -2.5; 52 -2.9; 56 -3.3; 59 -3.3; 64 -3.0; 68 -3.2; 73 -3.9; 78 -4.2; 83 -4.4; 89 -4.6; 95 -4.7; 102 -4.7; 109 -4.8; 117 -4.8; 125 -4.9; 134 -4.9; 143 -4.8; 153 -4.6; 164 -4.2; 175 -3.9; 188 -3.5; 201 -3.2; 215 -3.0; 230 -3.2; 246 -3.7; 263 -3.5; 282 -2.8; 301 -2.4; 323 -2.1; 345 -1.8; 369 -1.5; 395 -1.2; 423 -0.8; 452 -0.6; 484 -0.4; 518 -0.4; 554 0.7; 593 0.8; 635 0.6; 679 0.2; 726 0.1; 777 0.3; 832 0.1; 890 -0.0; 952 -0.2; 1019 -0.1; 1090 -0.3; 1167 -0.2; 1248 -0.2; 1336 -0.2; 1429 -0.4; 1529 -0.6; 1636 -0.7; 1751 -1.2; 1873 -1.0; 2004 -0.1; 2145 2.3; 2295 5.7; 2455 6.0; 2627 4.6; 2811 2.9; 3008 1.4; 3219 -0.6; 3444 -2.3; 3685 -1.6; 3943 -1.6; 4219 -2.4; 4514 0.4; 4830 3.4; 5168 4.5; 5530 2.4; 5917 -3.0; 6331 -9.1; 6775 -7.2; 7249 -2.0; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.7; 13327 -3.7; 14260 -6.9; 15258 -8.6; 16326 -8.1; 17469 -5.8; 18692 -2.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.1dB` and instead set Global volume in the UI for both channels to **-71**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.52 | 6.8 dB   |
| Peaking | 107 Hz   | 0.51 | -5.1 dB  |
| Peaking | 2472 Hz  | 4.95 | 7.1 dB   |
| Peaking | 3572 Hz  | 4.55 | -2.7 dB  |
| Peaking | 15867 Hz | 1.82 | -9.4 dB  |
| Peaking | 596 Hz   | 4.13 | 1.5 dB   |
| Peaking | 1803 Hz  | 5.3  | -1.9 dB  |
| Peaking | 5211 Hz  | 5.71 | 6.5 dB   |
| Peaking | 6407 Hz  | 5.52 | -11.4 dB |
| Peaking | 8786 Hz  | 1.27 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-2400/Ultrasone%20HFI-2400.png)