# Beats Solo3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.5; 25 -7.7; 28 -8.0; 31 -8.2; 34 -8.3; 37 -8.4; 41 -8.4; 45 -8.4; 49 -8.5; 54 -8.6; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.2; 87 -9.4; 96 -9.5; 106 -9.6; 116 -9.7; 128 -9.8; 141 -9.8; 155 -9.7; 170 -9.5; 187 -9.2; 206 -8.7; 227 -8.2; 249 -7.6; 274 -6.9; 302 -6.1; 332 -5.4; 365 -4.8; 402 -4.3; 442 -4.4; 486 -3.8; 535 -2.9; 588 -2.1; 647 -1.4; 712 -0.8; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.6; 1146 -2.5; 1261 -3.3; 1387 -3.9; 1526 -4.4; 1678 -4.8; 1846 -5.5; 2031 -5.5; 2234 -5.2; 2457 -4.8; 2703 -5.7; 2973 -7.2; 3270 -8.3; 3597 -9.2; 3957 -7.0; 4353 -6.1; 4788 -7.1; 5267 -5.3; 5793 -4.2; 6373 -5.7; 7010 -6.2; 7711 -6.2; 8482 -7.4; 9330 -7.5; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.39 | -2.7 dB |
| Peaking | 156 Hz  | 0.97 | -3.0 dB |
| Peaking | 777 Hz  | 1.06 | 5.5 dB  |
| Peaking | 3462 Hz | 4.17 | -3.9 dB |
| Peaking | 8896 Hz | 5.45 | -2.3 dB |
| Peaking | 366 Hz  | 6.04 | 0.7 dB  |
| Peaking | 1972 Hz | 2.49 | -1.7 dB |
| Peaking | 2453 Hz | 1.74 | 1.8 dB  |
| Peaking | 2947 Hz | 4.03 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)