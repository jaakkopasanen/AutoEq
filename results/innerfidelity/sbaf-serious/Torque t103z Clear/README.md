# Torque t103z Clear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -3.2; 23 -3.7; 25 -4.1; 28 -4.8; 31 -5.3; 34 -5.8; 37 -6.1; 41 -6.5; 45 -6.9; 49 -7.3; 54 -7.6; 60 -8.0; 66 -8.4; 72 -8.8; 79 -9.1; 87 -9.5; 96 -9.8; 106 -9.9; 116 -10.0; 128 -10.1; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.5; 206 -9.2; 227 -8.7; 249 -8.3; 274 -7.8; 302 -7.2; 332 -6.5; 365 -5.9; 402 -5.2; 442 -4.3; 486 -3.8; 535 -3.1; 588 -2.1; 647 -1.7; 712 -0.1; 783 -0.0; 861 0.1; 947 0.1; 1042 0.0; 1146 0.0; 1261 -0.0; 1387 -0.4; 1526 -0.7; 1678 -0.8; 1846 -0.6; 2031 -0.2; 2234 -0.2; 2457 -0.1; 2703 -1.0; 2973 -0.7; 3270 0.6; 3597 1.1; 3957 -0.4; 4353 -4.2; 4788 -2.3; 5267 -2.6; 5793 2.6; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 67 Hz   | 0.4  | -7.0 dB |
| Peaking | 164 Hz  | 0.79 | -5.3 dB |
| Peaking | 324 Hz  | 1.36 | -3.1 dB |
| Peaking | 4912 Hz | 3.43 | -4.6 dB |
| Peaking | 6269 Hz | 4.8  | 6.9 dB  |
| Peaking | 552 Hz  | 1.81 | -1.9 dB |
| Peaking | 707 Hz  | 1.19 | 1.9 dB  |
| Peaking | 1633 Hz | 3.9  | -0.8 dB |
| Peaking | 3598 Hz | 4.97 | 4.2 dB  |
| Peaking | 3736 Hz | 2.36 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Clear/Torque%20t103z%20Clear.png)