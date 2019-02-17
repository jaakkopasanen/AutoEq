# Beats Solo2 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.8; 31 -8.0; 34 -8.2; 37 -8.2; 41 -8.2; 45 -8.3; 49 -8.3; 54 -8.4; 60 -8.6; 66 -8.8; 72 -8.9; 79 -9.0; 87 -9.2; 96 -9.4; 106 -9.5; 116 -9.6; 128 -9.6; 141 -9.6; 155 -9.5; 170 -9.4; 187 -9.1; 206 -8.6; 227 -8.1; 249 -7.5; 274 -6.8; 302 -5.9; 332 -5.2; 365 -4.6; 402 -3.4; 442 -3.0; 486 -2.7; 535 -2.2; 588 -1.7; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.5; 1146 -2.2; 1261 -2.8; 1387 -3.4; 1526 -3.8; 1678 -4.3; 1846 -4.7; 2031 -4.5; 2234 -3.8; 2457 -3.4; 2703 -3.9; 2973 -5.2; 3270 -6.2; 3597 -7.0; 3957 -4.3; 4353 -3.0; 4788 -5.8; 5267 -3.9; 5793 -3.2; 6373 -5.6; 7010 -5.8; 7711 -5.4; 8482 -6.2; 9330 -5.3; 10263 -1.8; 11289 -1.2; 12418 -1.2; 13660 -1.2; 15026 -1.2; 16529 -1.2; 18182 -2.2; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.34 | -6.6 dB |
| Peaking | 134 Hz   | 0.92 | -4.9 dB |
| Peaking | 239 Hz   | 1.51 | -3.4 dB |
| Peaking | 3180 Hz  | 0.81 | -4.0 dB |
| Peaking | 7990 Hz  | 2.15 | -4.3 dB |
| Peaking | 817 Hz   | 2.12 | 1.9 dB  |
| Peaking | 1893 Hz  | 1.45 | -3.3 dB |
| Peaking | 2385 Hz  | 1.48 | 3.2 dB  |
| Peaking | 3424 Hz  | 6.87 | -2.6 dB |
| Peaking | 11085 Hz | 5.18 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Solo2%20Wireless/Beats%20Solo2%20Wireless.png)