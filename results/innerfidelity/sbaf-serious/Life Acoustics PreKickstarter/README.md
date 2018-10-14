# Life Acoustics PreKickstarter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.6; 28 0.4; 31 0.2; 34 0.1; 37 -0.1; 41 -0.2; 45 -0.4; 49 -0.7; 54 -0.9; 60 -1.2; 66 -1.5; 72 -1.9; 79 -2.3; 87 -2.7; 96 -3.1; 106 -3.4; 116 -3.5; 128 -3.9; 141 -4.1; 155 -4.2; 170 -4.4; 187 -4.4; 206 -4.4; 227 -4.3; 249 -4.3; 274 -4.0; 302 -3.9; 332 -3.6; 365 -3.3; 402 -3.0; 442 -2.6; 486 -2.3; 535 -1.9; 588 -1.2; 647 -0.8; 712 -0.5; 783 -0.0; 861 -0.0; 947 -0.0; 1042 0.0; 1146 0.0; 1261 0.1; 1387 0.1; 1526 0.0; 1678 0.1; 1846 0.2; 2031 0.3; 2234 0.4; 2457 1.6; 2703 3.2; 2973 5.1; 3270 6.0; 3597 6.0; 3957 5.2; 4353 2.4; 4788 2.6; 5267 4.4; 5793 5.4; 6373 4.8; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -0.5; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Life Acoustics PreKickstarter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.56 | 1.2 dB  |
| Peaking | 151 Hz  | 0.62 | -4.0 dB |
| Peaking | 330 Hz  | 1.17 | -1.9 dB |
| Peaking | 3390 Hz | 2.48 | 6.5 dB  |
| Peaking | 5940 Hz | 3.75 | 5.3 dB  |
| Peaking | 832 Hz  | 3.11 | 0.6 dB  |
| Peaking | 2260 Hz | 3.1  | -1.0 dB |
| Peaking | 2703 Hz | 4.39 | 1.0 dB  |
| Peaking | 8877 Hz | 3.83 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Life%20Acoustics%20PreKickstarter/Life%20Acoustics%20PreKickstarter.png)