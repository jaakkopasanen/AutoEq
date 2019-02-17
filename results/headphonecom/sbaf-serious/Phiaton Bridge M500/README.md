# Phiaton Bridge M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.8; 72 -2.2; 79 -2.0; 87 -2.2; 96 -2.9; 106 -3.6; 116 -3.9; 128 -3.8; 141 -3.8; 155 -3.4; 170 -3.1; 187 -2.6; 206 -2.0; 227 -1.3; 249 -0.8; 274 -0.5; 302 -0.8; 332 -1.1; 365 -1.6; 402 -2.4; 442 -3.1; 486 -3.7; 535 -4.3; 588 -4.7; 647 -5.1; 712 -5.5; 783 -5.8; 861 -6.0; 947 -6.4; 1042 -6.5; 1146 -6.2; 1261 -6.2; 1387 -5.8; 1526 -5.1; 1678 -5.6; 1846 -6.4; 2031 -4.6; 2234 -2.3; 2457 -0.6; 2703 -0.5; 2973 -1.3; 3270 -3.6; 3597 -4.0; 3957 -3.1; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Bridge M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.29 | 6.2 dB  |
| Peaking | 120 Hz  | 1.87 | -1.5 dB |
| Peaking | 293 Hz  | 1.11 | 5.3 dB  |
| Peaking | 2606 Hz | 3.16 | 5.9 dB  |
| Peaking | 5221 Hz | 1.95 | 6.6 dB  |
| Peaking | 1009 Hz | 3.34 | -0.7 dB |
| Peaking | 5384 Hz | 5.69 | -2.2 dB |
| Peaking | 6528 Hz | 1.97 | 3.2 dB  |
| Peaking | 7433 Hz | 4.3  | -2.4 dB |
| Peaking | 8586 Hz | 1.51 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 5.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)