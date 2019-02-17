# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.8; 25 -8.1; 28 -8.6; 31 -8.9; 34 -9.2; 37 -9.4; 41 -9.7; 45 -9.9; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.2; 87 -11.3; 96 -11.5; 106 -11.5; 116 -11.4; 128 -12.2; 141 -12.2; 155 -12.0; 170 -11.8; 187 -11.5; 206 -11.1; 227 -10.7; 249 -10.2; 274 -9.9; 302 -9.9; 332 -9.4; 365 -9.0; 402 -8.6; 442 -8.2; 486 -7.8; 535 -7.5; 588 -7.1; 647 -6.8; 712 -6.5; 783 -6.2; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -6.8; 1387 -7.0; 1526 -6.9; 1678 -6.4; 1846 -5.6; 2031 -4.5; 2234 -3.2; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.2; 6373 -6.6; 7010 -10.2; 7711 -9.7; 8482 -9.8; 9330 -12.2; 10263 -12.7; 11289 -9.7; 12418 -8.3; 13660 -11.0; 15026 -13.6; 16529 -12.1; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.7  | -1.9 dB |
| Peaking | 148 Hz   | 0.52 | -5.1 dB |
| Peaking | 4420 Hz  | 0.85 | 9.0 dB  |
| Peaking | 8401 Hz  | 1.05 | -7.8 dB |
| Peaking | 15558 Hz | 2    | -7.2 dB |
| Peaking | 1564 Hz  | 2.44 | -2.0 dB |
| Peaking | 2671 Hz  | 3.31 | 2.2 dB  |
| Peaking | 4344 Hz  | 2.17 | -2.5 dB |
| Peaking | 5825 Hz  | 1.64 | 3.3 dB  |
| Peaking | 6754 Hz  | 5.54 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -7.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)