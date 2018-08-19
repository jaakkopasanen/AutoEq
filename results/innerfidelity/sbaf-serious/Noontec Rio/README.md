# Noontec Rio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -14.0; 22 -13.7; 23 -13.6; 25 -13.4; 26 -13.3; 28 -13.1; 30 -12.9; 32 -12.6; 35 -12.3; 37 -12.1; 40 -11.9; 42 -11.7; 45 -11.4; 49 -11.1; 52 -10.9; 56 -10.7; 59 -10.5; 64 -10.2; 68 -10.1; 73 -9.9; 78 -9.7; 83 -9.6; 89 -9.4; 95 -9.3; 102 -9.0; 109 -8.7; 117 -8.5; 125 -8.2; 134 -8.0; 143 -7.7; 153 -7.4; 164 -7.1; 175 -6.8; 188 -6.4; 201 -6.1; 215 -5.6; 230 -5.2; 246 -4.8; 263 -4.5; 282 -4.1; 301 -3.6; 323 -3.3; 345 -2.8; 369 -2.5; 395 -2.1; 423 -1.6; 452 -1.3; 484 -1.1; 518 -0.8; 554 -0.3; 593 -0.1; 635 0.0; 679 0.2; 726 0.9; 777 1.0; 832 0.8; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.5; 1429 -2.1; 1529 -2.7; 1636 -3.2; 1751 -3.6; 1873 -3.8; 2004 -4.1; 2145 -4.5; 2295 -5.0; 2455 -5.5; 2627 -6.2; 2811 -6.9; 3008 -7.1; 3219 -6.7; 3444 -5.5; 3685 -5.4; 3943 -6.8; 4219 -9.8; 4514 -11.0; 4830 -8.8; 5168 -3.5; 5530 0.9; 5917 4.2; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.4; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.609135449382928dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Rio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.19 | -13.6 dB |
| Peaking | 157 Hz  | 0.79 | -3.5 dB  |
| Peaking | 2719 Hz | 1.36 | -6.2 dB  |
| Peaking | 4561 Hz | 3.85 | -10.9 dB |
| Peaking | 6184 Hz | 3.63 | 8.2 dB   |
| Peaking | 299 Hz  | 2.1  | -0.7 dB  |
| Peaking | 784 Hz  | 1.67 | 1.8 dB   |
| Peaking | 1623 Hz | 3.73 | -1.3 dB  |
| Peaking | 5332 Hz | 4.38 | 0.4 dB   |
| Peaking | 7712 Hz | 5.47 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Rio/Noontec%20Rio.png)