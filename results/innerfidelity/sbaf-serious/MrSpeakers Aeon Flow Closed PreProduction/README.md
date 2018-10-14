# MrSpeakers Aeon Flow Closed PreProduction

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 0.0; 23 1.1; 25 1.0; 28 0.9; 31 0.8; 34 0.7; 37 0.7; 41 0.7; 45 0.6; 49 0.6; 54 0.4; 60 0.4; 66 0.5; 72 0.4; 79 0.2; 87 -0.5; 96 -1.4; 106 -2.2; 116 -2.3; 128 -2.0; 141 -1.2; 155 -0.0; 170 0.2; 187 0.1; 206 0.3; 227 0.4; 249 0.3; 274 0.2; 302 0.1; 332 -0.1; 365 -0.2; 402 -0.2; 442 0.1; 486 0.1; 535 0.2; 588 0.4; 647 0.4; 712 0.4; 783 0.7; 861 0.9; 947 -0.0; 1042 -0.4; 1146 -0.7; 1261 -0.8; 1387 -1.2; 1526 -1.7; 1678 -2.1; 1846 -1.6; 2031 -0.5; 2234 0.1; 2457 0.7; 2703 2.3; 2973 3.1; 3270 2.8; 3597 1.4; 3957 0.9; 4353 1.0; 4788 1.4; 5267 3.6; 5793 3.4; 6373 3.5; 7010 2.5; 7711 0.3; 8482 -2.4; 9330 -3.2; 10263 -0.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed PreProduction ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 114 Hz  | 3.69 | -2.7 dB |
| Peaking | 1661 Hz | 2.75 | -2.4 dB |
| Peaking | 2970 Hz | 3.43 | 3.2 dB  |
| Peaking | 6063 Hz | 2.48 | 4.3 dB  |
| Peaking | 8937 Hz | 4.57 | -4.3 dB |
| Peaking | 16 Hz   | 0.69 | 0.5 dB  |
| Peaking | 28 Hz   | 0.64 | 0.8 dB  |
| Peaking | 222 Hz  | 3.64 | 0.5 dB  |
| Peaking | 850 Hz  | 2.25 | 1.2 dB  |
| Peaking | 1040 Hz | 2.37 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Closed%20PreProduction/MrSpeakers%20Aeon%20Flow%20Closed%20PreProduction.png)