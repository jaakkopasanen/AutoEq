# Sennheiser HD 419
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.8; 28 -7.0; 31 -7.2; 34 -7.4; 37 -7.5; 41 -7.6; 45 -7.7; 49 -7.8; 54 -7.9; 60 -7.9; 66 -7.9; 72 -8.1; 79 -7.6; 87 -5.4; 96 -5.7; 106 -8.9; 116 -9.7; 128 -9.6; 141 -9.9; 155 -9.9; 170 -9.7; 187 -10.3; 206 -10.1; 227 -10.0; 249 -9.0; 274 -7.9; 302 -6.6; 332 -5.6; 365 -4.3; 402 -2.7; 442 -2.1; 486 -2.1; 535 -2.9; 588 -2.8; 647 -1.8; 712 -1.1; 783 -1.2; 861 -0.6; 947 -0.3; 1042 -0.0; 1146 -0.9; 1261 -0.4; 1387 -1.4; 1526 -1.9; 1678 -1.9; 1846 -2.3; 2031 -1.4; 2234 0.5; 2457 1.6; 2703 1.6; 2973 2.2; 3270 2.1; 3597 1.9; 3957 3.8; 4353 6.0; 4788 6.0; 5267 4.8; 5793 5.6; 6373 4.8; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 419 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.76 | -6.3 dB |
| Peaking | 56 Hz   | 1.82 | -3.1 dB |
| Peaking | 164 Hz  | 0.68 | -9.3 dB |
| Peaking | 244 Hz  | 2.5  | -2.3 dB |
| Peaking | 4938 Hz | 1.77 | 6.4 dB  |
| Peaking | 91 Hz   | 6.33 | 6.2 dB  |
| Peaking | 94 Hz   | 2.48 | -3.2 dB |
| Peaking | 1861 Hz | 2.36 | -3.9 dB |
| Peaking | 2336 Hz | 1.98 | 2.4 dB  |
| Peaking | 8499 Hz | 4.31 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)