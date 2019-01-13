# Torque t402v OnEar Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.7; 23 -2.4; 25 -3.1; 28 -3.9; 31 -4.6; 34 -5.2; 37 -5.6; 41 -6.2; 45 -6.6; 49 -7.0; 54 -7.4; 60 -7.9; 66 -8.2; 72 -8.6; 79 -8.8; 87 -9.1; 96 -9.6; 106 -10.1; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.0; 170 -10.7; 187 -10.7; 206 -10.5; 227 -10.1; 249 -9.7; 274 -9.1; 302 -8.5; 332 -8.1; 365 -7.6; 402 -6.7; 442 -5.9; 486 -5.3; 535 -4.0; 588 -2.2; 647 -0.3; 712 1.5; 783 3.0; 861 2.8; 947 1.2; 1042 -1.0; 1146 -2.9; 1261 -4.3; 1387 -3.8; 1526 -4.9; 1678 -3.5; 1846 -2.2; 2031 -2.3; 2234 -3.2; 2457 -3.5; 2703 -3.3; 2973 -2.7; 3270 -1.6; 3597 -1.1; 3957 -1.0; 4353 -2.1; 4788 -1.0; 5267 3.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OnEar Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 91 Hz   | 0.43 | -8.7 dB |
| Peaking | 244 Hz  | 0.94 | -6.0 dB |
| Peaking | 2289 Hz | 0.98 | -3.5 dB |
| Peaking | 6030 Hz | 3.88 | 7.5 dB  |
| Peaking | 8182 Hz | 2.89 | -0.5 dB |
| Peaking | 474 Hz  | 1.62 | -3.4 dB |
| Peaking | 811 Hz  | 2.16 | 5.1 dB  |
| Peaking | 968 Hz  | 0.43 | 1.9 dB  |
| Peaking | 1285 Hz | 1.96 | -5.1 dB |
| Peaking | 4510 Hz | 7.72 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Red/Torque%20t402v%20OnEar%20Red.png)