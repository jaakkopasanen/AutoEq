# Torque t402v OnEar Black

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -0.7; 23 -1.4; 25 -2.0; 28 -2.8; 31 -3.5; 34 -4.0; 37 -4.5; 41 -5.0; 45 -5.5; 49 -5.9; 54 -6.3; 60 -6.7; 66 -7.0; 72 -7.3; 79 -7.6; 87 -8.0; 96 -8.7; 106 -8.9; 116 -9.2; 128 -9.5; 141 -9.6; 155 -9.6; 170 -9.4; 187 -9.4; 206 -9.2; 227 -8.9; 249 -8.5; 274 -8.0; 302 -7.3; 332 -7.0; 365 -6.7; 402 -5.8; 442 -5.0; 486 -4.1; 535 -2.6; 588 -0.8; 647 0.9; 712 2.4; 783 3.4; 861 2.6; 947 1.1; 1042 -0.9; 1146 -2.4; 1261 -3.4; 1387 -3.5; 1526 -5.3; 1678 -4.9; 1846 -3.4; 2031 -3.0; 2234 -3.6; 2457 -3.8; 2703 -3.6; 2973 -3.0; 3270 -2.1; 3597 -1.6; 3957 -1.6; 4353 -2.6; 4788 -1.7; 5267 2.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 97 Hz   | 0.49 | -8.1 dB |
| Peaking | 250 Hz  | 1.1  | -5.3 dB |
| Peaking | 1576 Hz | 4.02 | -4.5 dB |
| Peaking | 2831 Hz | 1.21 | -3.3 dB |
| Peaking | 6045 Hz | 4.38 | 7.4 dB  |
| Peaking | 443 Hz  | 2.33 | -2.4 dB |
| Peaking | 783 Hz  | 2.06 | 5.4 dB  |
| Peaking | 1186 Hz | 3.02 | -2.5 dB |
| Peaking | 4492 Hz | 2.13 | 2.2 dB  |
| Peaking | 4531 Hz | 4.89 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Black/Torque%20t402v%20OnEar%20Black.png)