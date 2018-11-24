# Grado PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 4.9; 34 3.9; 37 3.0; 41 2.0; 45 0.9; 49 0.0; 54 -1.0; 60 -2.1; 66 -2.9; 72 -3.6; 79 -3.9; 87 -4.2; 96 -4.6; 106 -4.6; 116 -4.5; 128 -4.3; 141 -4.0; 155 -3.8; 170 -3.3; 187 -3.0; 206 -2.7; 227 -2.3; 249 -1.9; 274 -1.5; 302 -1.0; 332 -0.6; 365 -0.2; 402 0.1; 442 0.2; 486 0.6; 535 0.7; 588 1.0; 647 1.0; 712 0.9; 783 0.9; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -1.2; 1387 -2.4; 1526 -3.5; 1678 -3.6; 1846 -2.7; 2031 -4.8; 2234 -3.1; 2457 0.5; 2703 3.1; 2973 5.9; 3270 6.0; 3597 6.0; 3957 3.8; 4353 4.5; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -4.0; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.95 | 6.9 dB  |
| Peaking | 100 Hz  | 0.73 | -5.4 dB |
| Peaking | 2056 Hz | 1.85 | -7.1 dB |
| Peaking | 3087 Hz | 1.73 | 8.0 dB  |
| Peaking | 5571 Hz | 2.98 | 5.8 dB  |
| Peaking | 227 Hz  | 1.94 | -0.8 dB |
| Peaking | 627 Hz  | 0.91 | 1.4 dB  |
| Peaking | 1477 Hz | 5.45 | -1.9 dB |
| Peaking | 6503 Hz | 9.71 | 2.0 dB  |
| Peaking | 9372 Hz | 5.67 | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS500/Grado%20PS500.png)