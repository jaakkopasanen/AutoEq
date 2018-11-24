# Torque t103z Deep

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.4; 23 -9.5; 25 -9.6; 28 -9.7; 31 -9.8; 34 -9.8; 37 -9.9; 41 -9.9; 45 -10.0; 49 -10.1; 54 -10.1; 60 -10.2; 66 -10.4; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.7; 116 -10.6; 128 -10.5; 141 -10.3; 155 -10.0; 170 -9.7; 187 -9.3; 206 -8.8; 227 -8.3; 249 -7.7; 274 -7.1; 302 -6.5; 332 -5.8; 365 -5.1; 402 -4.4; 442 -3.5; 486 -3.0; 535 -2.3; 588 -1.5; 647 -1.1; 712 0.3; 783 0.4; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.3; 1526 -2.1; 1678 -2.7; 1846 -3.1; 2031 -3.1; 2234 -2.5; 2457 0.0; 2703 2.8; 2973 5.7; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Deep GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Deep ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.37 | -9.0 dB |
| Peaking | 53 Hz   | 0.3  | -9.2 dB |
| Peaking | 192 Hz  | 0.66 | -4.9 dB |
| Peaking | 2046 Hz | 1.85 | -7.5 dB |
| Peaking | 3574 Hz | 0.82 | 8.0 dB  |
| Peaking | 783 Hz  | 3.23 | 1.6 dB  |
| Peaking | 1505 Hz | 6.03 | -0.9 dB |
| Peaking | 3958 Hz | 5.86 | -1.0 dB |
| Peaking | 6306 Hz | 2.34 | 5.2 dB  |
| Peaking | 7435 Hz | 1.56 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Deep/Torque%20t103z%20Deep.png)