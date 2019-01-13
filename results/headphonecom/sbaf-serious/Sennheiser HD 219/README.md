# Sennheiser HD 219
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 1.1; 28 0.3; 31 -0.4; 34 -1.0; 37 -1.6; 41 -2.2; 45 -2.7; 49 -3.1; 54 -3.6; 60 -4.1; 66 -4.4; 72 -4.6; 79 -4.8; 87 -4.8; 96 -5.0; 106 -5.1; 116 -4.8; 128 -4.4; 141 -3.6; 155 -3.6; 170 -3.6; 187 -3.7; 206 -3.0; 227 -2.1; 249 -1.9; 274 -1.2; 302 0.1; 332 1.2; 365 1.6; 402 2.0; 442 2.0; 486 1.7; 535 1.4; 588 1.0; 647 1.1; 712 2.0; 783 1.4; 861 0.8; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.2; 1526 0.2; 1678 -1.1; 1846 -1.5; 2031 -1.2; 2234 -0.6; 2457 -0.1; 2703 0.3; 2973 0.4; 3270 0.9; 3597 1.5; 3957 0.4; 4353 -1.8; 4788 -0.8; 5267 2.1; 5793 4.2; 6373 4.9; 7010 2.5; 7711 -1.3; 8482 -4.7; 9330 -4.8; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.5; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 219 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.98 | -5.3 dB |
| Peaking | 179 Hz  | 2.78 | -2.4 dB |
| Peaking | 6292 Hz | 3.97 | 6.1 dB  |
| Peaking | 8773 Hz | 4.18 | -6.3 dB |
| Peaking | 18 Hz   | 2.72 | 3.0 dB  |
| Peaking | 418 Hz  | 2.48 | 2.6 dB  |
| Peaking | 725 Hz  | 4.36 | 1.9 dB  |
| Peaking | 1863 Hz | 4.93 | -1.8 dB |
| Peaking | 4483 Hz | 9.58 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)