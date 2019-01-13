# Sennheiser HD 229 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 1.6; 25 0.9; 28 -0.0; 31 -0.8; 34 -1.5; 37 -2.0; 41 -2.7; 45 -3.2; 49 -3.7; 54 -4.2; 60 -4.7; 66 -5.1; 72 -5.3; 79 -5.5; 87 -5.5; 96 -5.7; 106 -5.5; 116 -5.1; 128 -4.5; 141 -4.0; 155 -5.3; 170 -4.3; 187 -4.0; 206 -2.6; 227 -3.2; 249 -2.4; 274 -1.2; 302 0.0; 332 1.0; 365 1.8; 402 1.9; 442 1.7; 486 1.7; 535 1.5; 588 1.7; 647 1.7; 712 1.2; 783 0.8; 861 0.4; 947 0.2; 1042 0.0; 1146 0.0; 1261 0.2; 1387 0.5; 1526 0.9; 1678 -1.2; 1846 -1.0; 2031 -0.3; 2234 0.3; 2457 0.6; 2703 0.5; 2973 0.7; 3270 0.8; 3597 0.6; 3957 -0.8; 4353 -2.1; 4788 -1.8; 5267 1.2; 5793 3.8; 6373 5.3; 7010 2.5; 7711 0.1; 8482 -4.1; 9330 -6.2; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 229 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 80 Hz   | 0.98 | -5.8 dB |
| Peaking | 167 Hz  | 2.36 | -3.3 dB |
| Peaking | 6349 Hz | 4.93 | 6.2 dB  |
| Peaking | 9098 Hz | 5.27 | -7.2 dB |
| Peaking | 20 Hz   | 2.9  | 2.8 dB  |
| Peaking | 244 Hz  | 4.03 | -1.9 dB |
| Peaking | 386 Hz  | 1.9  | 2.3 dB  |
| Peaking | 622 Hz  | 2.54 | 1.4 dB  |
| Peaking | 4522 Hz | 7.16 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20229%20Black/Sennheiser%20HD%20229%20Black.png)