# Phiaton Bridge M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.4; 34 -2.0; 37 -2.5; 41 -3.1; 45 -3.4; 49 -3.7; 54 -3.8; 60 -4.2; 66 -5.6; 72 -6.0; 79 -5.8; 87 -6.0; 96 -6.7; 106 -7.4; 116 -7.7; 128 -7.6; 141 -7.5; 155 -7.2; 170 -6.8; 187 -6.4; 206 -5.8; 227 -5.1; 249 -4.5; 274 -4.1; 302 -4.6; 332 -4.9; 365 -5.3; 402 -6.1; 442 -6.9; 486 -7.5; 535 -8.1; 588 -8.5; 647 -8.9; 712 -9.3; 783 -9.6; 861 -9.8; 947 -10.2; 1042 -10.3; 1146 -10.0; 1261 -10.0; 1387 -9.5; 1526 -8.9; 1678 -9.4; 1846 -10.2; 2031 -8.4; 2234 -6.1; 2457 -4.3; 2703 -3.9; 2973 -5.1; 3270 -7.4; 3597 -7.7; 3957 -6.8; 4353 -4.2; 4788 -2.4; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -10.4; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Bridge M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.94 | 6.2 dB  |
| Peaking | 992 Hz  | 1.38 | -4.1 dB |
| Peaking | 1799 Hz | 6.53 | -3.1 dB |
| Peaking | 5719 Hz | 2.42 | 6.9 dB  |
| Peaking | 9426 Hz | 4.73 | -5.0 dB |
| Peaking | 129 Hz  | 1.93 | -1.9 dB |
| Peaking | 284 Hz  | 1.68 | 2.7 dB  |
| Peaking | 573 Hz  | 2.19 | -1.2 dB |
| Peaking | 2642 Hz | 4.54 | 3.4 dB  |
| Peaking | 3572 Hz | 4.84 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)