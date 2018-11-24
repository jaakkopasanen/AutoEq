# Torque t103z Reference

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.3; 54 4.5; 60 3.7; 66 2.9; 72 2.2; 79 1.4; 87 0.5; 96 -0.4; 106 -1.1; 116 -1.8; 128 -2.6; 141 -3.4; 155 -4.2; 170 -4.9; 187 -5.5; 206 -6.2; 227 -6.7; 249 -7.3; 274 -7.6; 302 -7.7; 332 -7.4; 365 -7.0; 402 -6.3; 442 -5.4; 486 -4.5; 535 -3.6; 588 -2.4; 647 -1.8; 712 -0.3; 783 0.0; 861 0.2; 947 0.1; 1042 0.0; 1146 -0.2; 1261 -0.5; 1387 -1.0; 1526 -1.7; 1678 -2.2; 1846 -2.5; 2031 -2.4; 2234 -1.4; 2457 1.0; 2703 3.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.61 | 6.9 dB  |
| Peaking | 269 Hz  | 0.74 | -8.3 dB |
| Peaking | 2006 Hz | 1.63 | -9.0 dB |
| Peaking | 3123 Hz | 0.7  | 9.1 dB  |
| Peaking | 424 Hz  | 2.89 | -0.8 dB |
| Peaking | 778 Hz  | 2.81 | 1.6 dB  |
| Peaking | 3700 Hz | 4.76 | -0.8 dB |
| Peaking | 6235 Hz | 2.21 | 5.6 dB  |
| Peaking | 7394 Hz | 1.4  | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Reference/Torque%20t103z%20Reference.png)