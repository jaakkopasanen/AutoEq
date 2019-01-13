# Torque t096z Warm Tilt Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -4.5; 23 -4.8; 25 -5.0; 28 -5.4; 31 -5.6; 34 -5.8; 37 -5.9; 41 -6.1; 45 -6.3; 49 -6.4; 54 -6.6; 60 -6.8; 66 -7.1; 72 -7.3; 79 -7.5; 87 -7.7; 96 -7.9; 106 -7.9; 116 -7.9; 128 -7.9; 141 -7.8; 155 -7.7; 170 -7.5; 187 -7.1; 206 -6.8; 227 -6.3; 249 -5.8; 274 -5.3; 302 -4.8; 332 -4.2; 365 -3.5; 402 -2.9; 442 -2.1; 486 -1.7; 535 -1.2; 588 -0.3; 647 0.1; 712 0.3; 783 0.7; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.3; 1526 -3.4; 1678 -4.4; 1846 -5.5; 2031 -6.4; 2234 -7.3; 2457 -6.4; 2703 -4.2; 2973 -0.7; 3270 1.4; 3597 2.0; 3957 -0.1; 4353 -4.9; 4788 -5.4; 5267 -0.3; 5793 4.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Warm Tilt Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Warm Tilt Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.33 | -6.2 dB |
| Peaking | 179 Hz  | 0.77 | -4.4 dB |
| Peaking | 2124 Hz | 2.54 | -7.7 dB |
| Peaking | 4679 Hz | 6.94 | -7.6 dB |
| Peaking | 6117 Hz | 4.09 | 6.9 dB  |
| Peaking | 787 Hz  | 2.27 | 1.7 dB  |
| Peaking | 1559 Hz | 4.71 | -1.6 dB |
| Peaking | 2572 Hz | 6.27 | -2.6 dB |
| Peaking | 3499 Hz | 2.94 | 4.1 dB  |
| Peaking | 4241 Hz | 5.09 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Warm%20Tilt%20Filter/Torque%20t096z%20Warm%20Tilt%20Filter.png)