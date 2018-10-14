# Nocs NS 400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -12.4; 23 -12.3; 25 -12.3; 28 -12.1; 31 -12.0; 34 -11.8; 37 -11.7; 41 -11.5; 45 -11.4; 49 -11.2; 54 -11.1; 60 -11.0; 66 -10.8; 72 -10.7; 79 -10.6; 87 -10.5; 96 -10.4; 106 -10.1; 116 -9.8; 128 -9.5; 141 -9.2; 155 -8.8; 170 -8.4; 187 -7.9; 206 -7.3; 227 -6.7; 249 -6.2; 274 -5.6; 302 -4.9; 332 -4.3; 365 -3.6; 402 -3.0; 442 -2.3; 486 -1.8; 535 -1.3; 588 -0.5; 647 -0.1; 712 0.1; 783 0.6; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.5; 1526 -1.9; 1678 -2.4; 1846 -2.6; 2031 -3.1; 2234 -4.3; 2457 -4.2; 2703 -4.0; 2973 -2.0; 3270 0.6; 3597 2.4; 3957 2.2; 4353 0.2; 4788 -1.0; 5267 -2.1; 5793 -5.0; 6373 -7.8; 7010 -5.2; 7711 -2.6; 8482 -1.9; 9330 -2.5; 10263 -1.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.7dB` and instead set Global volume in the UI for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.18 | -12.0 dB |
| Peaking | 167 Hz  | 0.71 | -4.2 dB  |
| Peaking | 2483 Hz | 1.73 | -5.2 dB  |
| Peaking | 3664 Hz | 2.63 | 5.0 dB   |
| Peaking | 6399 Hz | 2.81 | -7.5 dB  |
| Peaking | 169 Hz  | 2.02 | 0.6 dB   |
| Peaking | 331 Hz  | 1.17 | -0.7 dB  |
| Peaking | 769 Hz  | 1.34 | 1.6 dB   |
| Peaking | 1510 Hz | 2.79 | -0.9 dB  |
| Peaking | 9588 Hz | 7.94 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS%20400/Nocs%20NS%20400.png)