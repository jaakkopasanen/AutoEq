# Sennheiser HD 239
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -0.8; 25 -1.2; 28 -1.7; 31 -2.0; 34 -2.3; 37 -2.5; 41 -2.8; 45 -3.0; 49 -3.3; 54 -3.5; 60 -3.8; 66 -4.0; 72 -4.1; 79 -4.3; 87 -4.5; 96 -4.5; 106 -4.1; 116 -4.2; 128 -4.6; 141 -4.7; 155 -4.7; 170 -4.7; 187 -4.5; 206 -4.4; 227 -4.1; 249 -3.8; 274 -3.3; 302 -2.8; 332 -2.5; 365 -2.1; 402 -1.7; 442 -1.4; 486 -1.3; 535 -0.8; 588 -0.6; 647 -0.4; 712 -0.2; 783 -0.0; 861 0.1; 947 0.2; 1042 -0.1; 1146 0.0; 1261 -0.3; 1387 0.1; 1526 -0.4; 1678 0.0; 1846 1.2; 2031 3.7; 2234 5.6; 2457 6.0; 2703 6.0; 2973 5.0; 3270 3.7; 3597 5.9; 3957 5.8; 4353 1.8; 4788 2.3; 5267 4.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 239 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 65 Hz    | 0.6  | -3.2 dB |
| Peaking | 190 Hz   | 0.69 | -3.6 dB |
| Peaking | 2792 Hz  | 1.54 | 6.1 dB  |
| Peaking | 5906 Hz  | 3.53 | 5.8 dB  |
| Peaking | 22050 Hz | 2.55 | 3.6 dB  |
| Peaking | 1705 Hz  | 2.54 | -2.3 dB |
| Peaking | 2217 Hz  | 2.85 | 2.8 dB  |
| Peaking | 3338 Hz  | 1.96 | -2.5 dB |
| Peaking | 3762 Hz  | 6.08 | 4.9 dB  |
| Peaking | 8287 Hz  | 4.51 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)