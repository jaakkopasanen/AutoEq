# Beyerdynamic T70 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.7; 25 4.5; 28 4.2; 31 4.0; 34 3.8; 37 3.6; 41 3.4; 45 3.3; 49 3.2; 54 3.1; 60 3.0; 66 2.8; 72 2.6; 79 2.1; 87 1.6; 96 1.0; 106 0.6; 116 0.2; 128 -0.5; 141 -1.0; 155 -0.8; 170 -0.3; 187 -0.8; 206 -0.7; 227 -0.3; 249 -0.2; 274 -0.2; 302 -0.3; 332 -0.6; 365 -0.8; 402 -1.1; 442 -0.8; 486 -0.4; 535 0.3; 588 0.4; 647 0.2; 712 0.0; 783 0.1; 861 -0.0; 947 0.0; 1042 0.0; 1146 0.0; 1261 0.0; 1387 -0.3; 1526 -0.5; 1678 -0.5; 1846 0.2; 2031 1.2; 2234 3.3; 2457 4.2; 2703 3.6; 2973 3.2; 3270 3.0; 3597 2.9; 3957 6.0; 4353 4.1; 4788 3.5; 5267 5.9; 5793 6.0; 6373 4.6; 7010 -0.7; 7711 -5.5; 8482 -8.4; 9330 -8.3; 10263 -4.6; 11289 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.61 | 4.6 dB   |
| Peaking | 2520 Hz  | 3.55 | 4.2 dB   |
| Peaking | 3975 Hz  | 4.26 | 4.8 dB   |
| Peaking | 5889 Hz  | 2.78 | 7.8 dB   |
| Peaking | 8707 Hz  | 2.72 | -10.8 dB |
| Peaking | 71 Hz    | 1.38 | 2.0 dB   |
| Peaking | 106 Hz   | 0.33 | -1.0 dB  |
| Peaking | 139 Hz   | 4.08 | -0.9 dB  |
| Peaking | 1621 Hz  | 4.81 | -1.1 dB  |
| Peaking | 11616 Hz | 5.72 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)