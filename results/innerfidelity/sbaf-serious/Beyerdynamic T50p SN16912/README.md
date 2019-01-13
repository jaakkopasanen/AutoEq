# Beyerdynamic T50p sn16912
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.4; 45 5.0; 49 4.5; 54 3.9; 60 3.4; 66 2.9; 72 2.7; 79 2.6; 87 2.6; 96 2.2; 106 2.8; 116 3.3; 128 3.0; 141 3.4; 155 3.6; 170 3.2; 187 1.5; 206 -0.5; 227 -2.0; 249 -2.8; 274 -3.0; 302 -4.0; 332 -4.9; 365 -4.5; 402 -4.0; 442 -3.7; 486 -3.3; 535 -2.8; 588 -2.2; 647 -1.8; 712 -0.9; 783 -0.2; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.4; 1526 0.2; 1678 0.3; 1846 1.0; 2031 2.2; 2234 4.1; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.5; 9330 -1.0; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sn16912 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sn16912 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.53 | 6.3 dB  |
| Peaking | 157 Hz   | 1.46 | 5.3 dB  |
| Peaking | 313 Hz   | 0.76 | -5.6 dB |
| Peaking | 4255 Hz  | 0.68 | 7.1 dB  |
| Peaking | 8767 Hz  | 2.62 | -4.6 dB |
| Peaking | 1756 Hz  | 2.97 | -2.0 dB |
| Peaking | 2499 Hz  | 3.47 | 2.4 dB  |
| Peaking | 4154 Hz  | 2.63 | -1.0 dB |
| Peaking | 6158 Hz  | 6.29 | 1.6 dB  |
| Peaking | 13643 Hz | 1.61 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sn16912/Beyerdynamic%20T50p%20sn16912.png)