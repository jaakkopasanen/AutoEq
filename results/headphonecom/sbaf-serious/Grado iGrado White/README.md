# Grado iGrado White
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.4; 79 4.4; 87 3.6; 96 2.9; 106 2.5; 116 2.0; 128 1.5; 141 1.0; 155 0.6; 170 0.4; 187 0.1; 206 -0.0; 227 -0.1; 249 0.1; 274 0.1; 302 0.2; 332 0.4; 365 0.4; 402 0.3; 442 0.3; 486 0.4; 535 0.3; 588 0.5; 647 0.5; 712 0.6; 783 0.6; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.5; 1526 -2.5; 1678 -3.2; 1846 -3.4; 2031 -3.1; 2234 -1.9; 2457 -0.3; 2703 -0.7; 2973 0.2; 3270 3.1; 3597 4.1; 3957 3.4; 4353 3.6; 4788 4.9; 5267 5.7; 5793 6.0; 6373 3.8; 7010 2.4; 7711 0.3; 8482 -0.2; 9330 -2.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGrado White GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGrado White ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.54 | 6.8 dB  |
| Peaking | 1853 Hz | 2.2  | -4.0 dB |
| Peaking | 3566 Hz | 3.95 | 3.2 dB  |
| Peaking | 5492 Hz | 2.15 | 6.2 dB  |
| Peaking | 9057 Hz | 4.43 | -2.7 dB |
| Peaking | 39 Hz   | 2.54 | -0.9 dB |
| Peaking | 69 Hz   | 3.02 | 1.4 dB  |
| Peaking | 189 Hz  | 1.58 | -0.9 dB |
| Peaking | 710 Hz  | 1.15 | 0.7 dB  |
| Peaking | 1494 Hz | 5.43 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGrado%20White/Grado%20iGrado%20White.png)