# Polk Audio UltraFit 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.4; 106 4.8; 116 4.2; 128 3.5; 141 3.0; 155 2.5; 170 2.0; 187 1.6; 206 1.3; 227 1.0; 249 0.7; 274 0.6; 302 0.3; 332 0.3; 365 0.3; 402 0.1; 442 -0.1; 486 -0.3; 535 -0.5; 588 -0.6; 647 -0.8; 712 -0.9; 783 -0.9; 861 -0.8; 947 -0.4; 1042 0.3; 1146 1.9; 1261 3.0; 1387 2.7; 1526 3.5; 1678 5.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.26 | 6.7 dB  |
| Peaking | 1199 Hz | 0.1  | -2.2 dB |
| Peaking | 1998 Hz | 1.01 | 6.9 dB  |
| Peaking | 3976 Hz | 1.21 | 5.5 dB  |
| Peaking | 5907 Hz | 2.94 | 4.6 dB  |
| Peaking | 87 Hz   | 5.52 | 0.8 dB  |
| Peaking | 404 Hz  | 3.13 | 0.6 dB  |
| Peaking | 856 Hz  | 4.6  | -0.8 dB |
| Peaking | 7759 Hz | 7.69 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%20500/Polk%20Audio%20UltraFit%20500.png)