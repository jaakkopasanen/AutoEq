# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.7; 25 -8.0; 28 -8.4; 31 -8.8; 34 -9.0; 37 -9.3; 41 -9.5; 45 -9.7; 49 -9.9; 54 -10.1; 60 -10.4; 66 -10.6; 72 -10.8; 79 -11.0; 87 -11.2; 96 -11.3; 106 -11.3; 116 -11.2; 128 -12.1; 141 -12.1; 155 -11.9; 170 -11.6; 187 -11.3; 206 -11.0; 227 -10.5; 249 -10.0; 274 -9.8; 302 -9.8; 332 -9.3; 365 -8.8; 402 -8.4; 442 -8.1; 486 -7.7; 535 -7.3; 588 -7.0; 647 -6.7; 712 -6.4; 783 -6.1; 861 -6.0; 947 -6.2; 1042 -6.5; 1146 -6.7; 1261 -6.7; 1387 -6.9; 1526 -6.8; 1678 -6.3; 1846 -5.5; 2031 -4.4; 2234 -3.0; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.0; 6373 -6.4; 7010 -10.1; 7711 -9.5; 8482 -9.7; 9330 -12.0; 10263 -12.5; 11289 -9.5; 12418 -8.1; 13660 -10.8; 15026 -13.5; 16529 -12.0; 18182 -7.0; 20000 -6.5
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
| Peaking | 48 Hz    | 0.68 | -2.0 dB |
| Peaking | 151 Hz   | 0.56 | -4.9 dB |
| Peaking | 4443 Hz  | 0.82 | 9.0 dB  |
| Peaking | 8378 Hz  | 1.05 | -7.9 dB |
| Peaking | 15552 Hz | 2.02 | -7.1 dB |
| Peaking | 1567 Hz  | 2.52 | -1.9 dB |
| Peaking | 2654 Hz  | 3.32 | 2.2 dB  |
| Peaking | 4358 Hz  | 2.13 | -2.4 dB |
| Peaking | 5851 Hz  | 1.67 | 3.4 dB  |
| Peaking | 6756 Hz  | 5.54 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)