# Sennheiser PXC 550 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.5; 25 -3.2; 28 -4.0; 31 -4.5; 34 -4.9; 37 -5.1; 41 -5.2; 45 -5.2; 49 -5.1; 54 -4.8; 60 -4.7; 66 -4.6; 72 -4.6; 79 -4.8; 87 -5.0; 96 -5.3; 106 -5.7; 116 -6.1; 128 -6.4; 141 -6.6; 155 -6.7; 170 -6.8; 187 -6.7; 206 -6.5; 227 -6.4; 249 -6.2; 274 -5.9; 302 -5.5; 332 -5.3; 365 -5.1; 402 -5.2; 442 -5.5; 486 -5.8; 535 -6.0; 588 -5.8; 647 -5.5; 712 -5.0; 783 -4.5; 861 -4.1; 947 -4.1; 1042 -4.5; 1146 -4.9; 1261 -4.7; 1387 -6.0; 1526 -7.8; 1678 -9.4; 1846 -9.8; 2031 -10.6; 2234 -9.8; 2457 -8.3; 2703 -7.6; 2973 -7.4; 3270 -6.9; 3597 -7.6; 3957 -5.0; 4353 -0.5; 4788 -5.2; 5267 -9.7; 5793 -5.5; 6373 -4.0; 7010 -5.5; 7711 -8.2; 8482 -11.6; 9330 -12.9; 10263 -10.5; 11289 -8.2; 12418 -10.5; 13660 -14.3; 15026 -12.2; 16529 -6.8; 18182 -6.5; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 2032 Hz  | 3.55 | -4.5 dB |
| Peaking | 4367 Hz  | 8.88 | 7.5 dB  |
| Peaking | 13279 Hz | 0.95 | -5.9 dB |
| Peaking | 19847 Hz | 3.55 | -5.8 dB |
| Peaking | 17 Hz    | 1.28 | 5.6 dB  |
| Peaking | 68 Hz    | 1.69 | 1.7 dB  |
| Peaking | 898 Hz   | 1.65 | 2.6 dB  |
| Peaking | 6519 Hz  | 6.44 | 4.0 dB  |
| Peaking | 8972 Hz  | 5.67 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20550%20Wireless/Sennheiser%20PXC%20550%20Wireless.png)