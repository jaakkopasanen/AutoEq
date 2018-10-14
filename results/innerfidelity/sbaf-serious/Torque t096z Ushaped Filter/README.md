# Torque t096z Ushaped Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 -12.3; 23 -12.2; 25 -12.2; 28 -12.1; 31 -12.0; 34 -11.9; 37 -11.8; 41 -11.7; 45 -11.5; 49 -11.3; 54 -11.2; 60 -11.0; 66 -10.9; 72 -10.8; 79 -10.7; 87 -10.6; 96 -10.5; 106 -10.2; 116 -9.8; 128 -9.6; 141 -9.3; 155 -8.9; 170 -8.4; 187 -7.8; 206 -7.3; 227 -6.7; 249 -6.2; 274 -5.5; 302 -4.9; 332 -4.2; 365 -3.6; 402 -2.9; 442 -2.2; 486 -1.8; 535 -1.2; 588 -0.4; 647 0.0; 712 0.3; 783 0.7; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.9; 1526 -2.8; 1678 -3.6; 1846 -4.2; 2031 -4.6; 2234 -5.6; 2457 -6.6; 2703 -7.0; 2973 -5.8; 3270 -3.6; 3597 -2.5; 3957 -3.9; 4353 -8.3; 4788 -10.6; 5267 -5.1; 5793 1.0; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -2.5; 11289 -4.0; 12418 -0.1; 13660 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Ushaped Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.21 | -12.0 dB |
| Peaking | 164 Hz   | 0.73 | -4.2 dB  |
| Peaking | 2461 Hz  | 1.77 | -6.6 dB  |
| Peaking | 4736 Hz  | 4.47 | -11.1 dB |
| Peaking | 6356 Hz  | 4.5  | 6.4 dB   |
| Peaking | 328 Hz   | 1.67 | -0.9 dB  |
| Peaking | 778 Hz   | 1.56 | 1.6 dB   |
| Peaking | 1631 Hz  | 3.44 | -1.6 dB  |
| Peaking | 2760 Hz  | 0.06 | 0.2 dB   |
| Peaking | 10962 Hz | 6.06 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Ushaped%20Filter/Torque%20t096z%20Ushaped%20Filter.png)