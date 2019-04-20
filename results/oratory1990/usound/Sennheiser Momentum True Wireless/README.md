# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.3; 28 -9.5; 31 -9.7; 34 -9.8; 37 -9.9; 41 -10.0; 45 -10.0; 49 -10.1; 54 -10.2; 60 -10.3; 66 -10.4; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.7; 116 -10.7; 128 -11.6; 141 -11.7; 155 -11.5; 170 -11.3; 187 -11.1; 206 -10.8; 227 -10.4; 249 -10.0; 274 -9.8; 302 -9.8; 332 -9.4; 365 -8.9; 402 -8.5; 442 -8.2; 486 -7.8; 535 -7.4; 588 -7.1; 647 -6.8; 712 -6.4; 783 -6.2; 861 -6.1; 947 -6.2; 1042 -6.6; 1146 -6.8; 1261 -6.8; 1387 -7.0; 1526 -6.9; 1678 -6.4; 1846 -5.5; 2031 -4.5; 2234 -3.1; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.1; 6373 -6.6; 7010 -10.1; 7711 -9.6; 8482 -9.7; 9330 -12.1; 10263 -12.6; 11289 -9.6; 12418 -8.2; 13660 -10.9; 15026 -13.6; 16529 -12.2; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.47 | -2.7 dB |
| Peaking | 165 Hz   | 0.55 | -4.4 dB |
| Peaking | 4421 Hz  | 0.84 | 9.0 dB  |
| Peaking | 8401 Hz  | 1.06 | -7.8 dB |
| Peaking | 15574 Hz | 2.01 | -7.2 dB |
| Peaking | 1564 Hz  | 2.49 | -1.9 dB |
| Peaking | 2662 Hz  | 3.35 | 2.2 dB  |
| Peaking | 4354 Hz  | 2.13 | -2.5 dB |
| Peaking | 5797 Hz  | 1.65 | 3.4 dB  |
| Peaking | 6748 Hz  | 5.37 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -7.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)