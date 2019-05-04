# Beats Solo2 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.2; 28 -7.5; 31 -7.7; 34 -7.8; 37 -7.9; 41 -7.9; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.3; 66 -8.5; 72 -8.6; 79 -8.7; 87 -8.8; 96 -9.0; 106 -9.1; 116 -9.2; 128 -9.3; 141 -9.3; 155 -9.2; 170 -9.1; 187 -8.8; 206 -8.3; 227 -7.9; 249 -7.3; 274 -6.6; 302 -5.7; 332 -5.1; 365 -4.3; 402 -3.3; 442 -2.8; 486 -2.6; 535 -2.1; 588 -1.6; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.5; 947 -0.9; 1042 -1.5; 1146 -2.2; 1261 -2.9; 1387 -3.4; 1526 -3.9; 1678 -4.4; 1846 -4.8; 2031 -4.8; 2234 -4.6; 2457 -4.2; 2703 -4.4; 2973 -5.2; 3270 -5.9; 3597 -6.7; 3957 -3.6; 4353 -2.8; 4788 -5.9; 5267 -4.2; 5793 -3.1; 6373 -4.5; 7010 -5.8; 7711 -6.2; 8482 -5.7; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.64 | -2.3 dB |
| Peaking | 95 Hz   | 0.71 | -2.4 dB |
| Peaking | 187 Hz  | 0.84 | -3.4 dB |
| Peaking | 863 Hz  | 0.63 | 6.1 dB  |
| Peaking | 1487 Hz | 0.74 | -2.9 dB |
| Peaking | 2636 Hz | 2.73 | 1.6 dB  |
| Peaking | 4074 Hz | 1.62 | -4.1 dB |
| Peaking | 4172 Hz | 6.11 | 6.7 dB  |
| Peaking | 5719 Hz | 4.8  | 3.2 dB  |
| Peaking | 7590 Hz | 4.52 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Solo2%20Wireless/Beats%20Solo2%20Wireless.png)