# Noontec Rio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -13.9; 22 -13.7; 23 -13.5; 25 -13.3; 26 -13.2; 28 -12.9; 30 -12.7; 32 -12.4; 35 -12.0; 37 -11.8; 40 -11.4; 42 -11.2; 45 -10.8; 49 -10.4; 52 -10.1; 56 -9.7; 59 -9.4; 64 -8.9; 68 -8.6; 73 -8.3; 78 -8.1; 83 -8.0; 89 -7.9; 95 -7.9; 102 -7.9; 109 -8.0; 117 -8.1; 125 -8.2; 134 -8.2; 143 -8.1; 153 -7.9; 164 -7.7; 175 -7.3; 188 -6.9; 201 -6.5; 215 -6.0; 230 -5.5; 246 -5.1; 263 -4.8; 282 -4.3; 301 -3.8; 323 -3.4; 345 -3.0; 369 -2.6; 395 -2.2; 423 -1.7; 452 -1.3; 484 -1.1; 518 -0.9; 554 -0.4; 593 -0.1; 635 0.0; 679 0.2; 726 0.9; 777 1.0; 832 0.8; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.5; 1429 -2.1; 1529 -2.7; 1636 -3.2; 1751 -3.6; 1873 -3.8; 2004 -4.1; 2145 -4.5; 2295 -5.0; 2455 -5.5; 2627 -6.2; 2811 -6.9; 3008 -7.1; 3219 -6.7; 3444 -5.5; 3685 -5.4; 3943 -6.8; 4219 -9.8; 4514 -11.0; 4830 -8.8; 5168 -3.5; 5530 0.9; 5917 4.2; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.4; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Rio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 9 Hz     | 0.65 | -13.5 dB |
| Peaking | 32 Hz    | 0.37 | -9.3 dB  |
| Peaking | 165 Hz   | 0.87 | -5.5 dB  |
| Peaking | 2718 Hz  | 1.68 | -6.9 dB  |
| Peaking | 4446 Hz  | 6.33 | -10.6 dB |
| Peaking | 853 Hz   | 0.9  | 4.3 dB   |
| Peaking | 1550 Hz  | 0.34 | -3.5 dB  |
| Peaking | 2522 Hz  | 2.29 | 3.2 dB   |
| Peaking | 22871 Hz | 1.15 | -0.4 dB  |
| Peaking | 6253 Hz  | 4.2  | 8.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Rio/Noontec%20Rio.png)