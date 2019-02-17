# Phiaton MS 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.1; 41 -1.6; 45 -2.2; 49 -2.9; 54 -3.6; 60 -4.2; 66 -3.8; 72 -3.6; 79 -4.7; 87 -5.6; 96 -6.2; 106 -6.6; 116 -6.8; 128 -6.8; 141 -5.5; 155 -3.9; 170 -4.5; 187 -4.4; 206 -4.3; 227 -4.9; 249 -5.0; 274 -4.8; 302 -4.6; 332 -4.4; 365 -4.0; 402 -3.8; 442 -3.8; 486 -4.0; 535 -3.9; 588 -4.0; 647 -4.0; 712 -4.1; 783 -4.2; 861 -4.5; 947 -6.0; 1042 -6.8; 1146 -6.9; 1261 -7.0; 1387 -7.5; 1526 -8.2; 1678 -8.6; 1846 -8.0; 2031 -6.5; 2234 -4.1; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.82 | 6.5 dB  |
| Peaking | 182 Hz  | 3.38 | 1.6 dB  |
| Peaking | 497 Hz  | 0.85 | 2.7 dB  |
| Peaking | 1678 Hz | 1.59 | -5.6 dB |
| Peaking | 3459 Hz | 0.75 | 7.5 dB  |
| Peaking | 115 Hz  | 4.66 | -1.5 dB |
| Peaking | 2627 Hz | 3.76 | 2.1 dB  |
| Peaking | 3240 Hz | 1.28 | -1.3 dB |
| Peaking | 6262 Hz | 2.12 | 5.4 dB  |
| Peaking | 7438 Hz | 1.48 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20400/Phiaton%20MS%20400.png)