# Phiaton MS 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.3; 25 -1.8; 28 -2.6; 31 -3.4; 34 -4.3; 37 -4.9; 41 -5.4; 45 -5.9; 49 -6.7; 54 -7.4; 60 -8.0; 66 -7.6; 72 -7.4; 79 -8.5; 87 -9.4; 96 -10.0; 106 -10.4; 116 -10.6; 128 -10.6; 141 -9.3; 155 -7.7; 170 -8.3; 187 -8.2; 206 -8.1; 227 -8.7; 249 -8.8; 274 -8.6; 302 -8.4; 332 -8.2; 365 -7.8; 402 -7.6; 442 -7.6; 486 -7.8; 535 -7.7; 588 -7.8; 647 -7.8; 712 -7.9; 783 -8.0; 861 -8.3; 947 -9.8; 1042 -10.6; 1146 -10.7; 1261 -10.8; 1387 -11.3; 1526 -12.0; 1678 -12.4; 1846 -11.8; 2031 -10.3; 2234 -7.9; 2457 -5.6; 2703 -4.2; 2973 -2.6; 3270 -1.5; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -1.7; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.42 | 5.8 dB  |
| Peaking | 108 Hz  | 1.46 | -4.1 dB |
| Peaking | 270 Hz  | 1.74 | -1.7 dB |
| Peaking | 1635 Hz | 1.03 | -7.7 dB |
| Peaking | 3839 Hz | 0.94 | 8.1 dB  |
| Peaking | 840 Hz  | 4.15 | 1.5 dB  |
| Peaking | 978 Hz  | 1.99 | -1.4 dB |
| Peaking | 1314 Hz | 4.35 | 1.3 dB  |
| Peaking | 6452 Hz | 2.64 | 4.9 dB  |
| Peaking | 7339 Hz | 1.6  | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20400/Phiaton%20MS%20400.png)