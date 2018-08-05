# Massdrop NuForce Every Day Car

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -12.8; 22 -12.7; 23 -12.7; 25 -12.6; 26 -12.5; 28 -12.3; 30 -12.2; 32 -12.0; 35 -11.8; 37 -11.6; 40 -11.3; 42 -11.2; 45 -10.9; 49 -10.5; 52 -10.3; 56 -9.9; 59 -9.7; 64 -9.3; 68 -9.0; 73 -8.7; 78 -8.4; 83 -8.3; 89 -8.3; 95 -8.3; 102 -8.4; 109 -8.5; 117 -8.6; 125 -8.8; 134 -8.9; 143 -8.8; 153 -8.7; 164 -8.5; 175 -8.1; 188 -7.8; 201 -7.4; 215 -6.9; 230 -6.4; 246 -6.1; 263 -5.7; 282 -5.2; 301 -4.7; 323 -4.3; 345 -3.9; 369 -3.5; 395 -2.9; 423 -2.4; 452 -1.9; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.1; 679 -0.1; 726 0.1; 777 0.3; 832 0.1; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.5; 1429 -2.1; 1529 -2.5; 1636 -3.0; 1751 -3.1; 1873 -3.2; 2004 -3.1; 2145 -3.0; 2295 -2.8; 2455 -2.2; 2627 -1.5; 2811 -0.5; 3008 1.3; 3219 3.3; 3444 5.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop NuForce Every Day Car ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 10 Hz   | 0.83 | -12.5 dB |
| Peaking | 34 Hz   | 0.39 | -9.5 dB  |
| Peaking | 173 Hz  | 0.79 | -6.2 dB  |
| Peaking | 2156 Hz | 1.51 | -5.2 dB  |
| Peaking | 4321 Hz | 1.2  | 7.8 dB   |
| Peaking | 795 Hz  | 1.04 | 3.7 dB   |
| Peaking | 2097 Hz | 5.59 | 1.1 dB   |
| Peaking | 848 Hz  | 0.58 | -2.5 dB  |
| Peaking | 6298 Hz | 3.61 | 4.1 dB   |
| Peaking | 7626 Hz | 1.47 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20NuForce%20Every%20Day%20Car/Massdrop%20NuForce%20Every%20Day%20Car.png)