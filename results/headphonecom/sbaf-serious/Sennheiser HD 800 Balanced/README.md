# Sennheiser HD 800 Balanced
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.3; 28 1.9; 31 1.6; 34 1.4; 37 1.2; 41 1.2; 45 1.2; 49 1.4; 54 1.5; 60 0.4; 66 -0.3; 72 -0.2; 79 -0.8; 87 -1.4; 96 -1.8; 106 -2.0; 116 -2.2; 128 -2.6; 141 -2.9; 155 -3.1; 170 -3.0; 187 -3.3; 206 -3.2; 227 -3.0; 249 -3.0; 274 -3.0; 302 -2.8; 332 -2.4; 365 -2.3; 402 -2.0; 442 -1.8; 486 -1.6; 535 -1.3; 588 -1.1; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.5; 947 0.1; 1042 0.1; 1146 1.0; 1261 1.1; 1387 1.3; 1526 0.9; 1678 1.2; 1846 1.5; 2031 1.7; 2234 1.0; 2457 1.4; 2703 2.1; 2973 0.1; 3270 1.6; 3597 2.2; 3957 0.6; 4353 -2.0; 4788 -2.6; 5267 -3.2; 5793 -3.3; 6373 -4.7; 7010 -5.3; 7711 -5.4; 8482 -2.1; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 Balanced GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 Balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.33 | 3.0 dB  |
| Peaking | 53 Hz   | 0.96 | 2.5 dB  |
| Peaking | 256 Hz  | 0.26 | -4.3 dB |
| Peaking | 2119 Hz | 0.14 | 2.8 dB  |
| Peaking | 6580 Hz | 1.36 | -7.6 dB |
| Peaking | 3629 Hz | 7.88 | 1.9 dB  |
| Peaking | 4492 Hz | 7.54 | -2.0 dB |
| Peaking | 7808 Hz | 7.63 | -2.0 dB |
| Peaking | 8909 Hz | 7.14 | 1.3 dB  |
| Peaking | 9395 Hz | 4.29 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20Balanced/Sennheiser%20HD%20800%20Balanced.png)