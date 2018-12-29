# Phiaton PS 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.1; 34 4.2; 37 3.8; 41 3.6; 45 2.6; 49 1.6; 54 1.8; 60 2.1; 66 0.9; 72 -0.3; 79 -1.1; 87 -1.7; 96 -2.2; 106 -2.5; 116 -2.9; 128 -3.1; 141 -3.4; 155 -3.4; 170 -3.2; 187 -3.4; 206 -3.0; 227 -2.8; 249 -2.0; 274 -0.8; 302 0.9; 332 2.1; 365 2.8; 402 2.9; 442 2.6; 486 2.3; 535 2.1; 588 2.1; 647 1.8; 712 1.4; 783 0.9; 861 1.6; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -0.7; 1387 -0.6; 1526 -0.5; 1678 -1.2; 1846 -2.1; 2031 -1.0; 2234 1.3; 2457 4.6; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.9; 4788 6.0; 5267 6.0; 5793 4.9; 6373 2.9; 7010 2.2; 7711 0.3; 8482 -0.8; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.41 | 7.7 dB   |
| Peaking | 525 Hz  | 0.46 | 12.5 dB  |
| Peaking | 535 Hz  | 0.1  | -10.0 dB |
| Peaking | 2975 Hz | 1.4  | 10.4 dB  |
| Peaking | 5116 Hz | 1.57 | 7.7 dB   |
| Peaking | 231 Hz  | 1.08 | -4.2 dB  |
| Peaking | 401 Hz  | 0.62 | 6.8 dB   |
| Peaking | 533 Hz  | 1.13 | -6.0 dB  |
| Peaking | 1923 Hz | 7.14 | -2.3 dB  |
| Peaking | 4589 Hz | 5.02 | -0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20500/Phiaton%20PS%20500.png)