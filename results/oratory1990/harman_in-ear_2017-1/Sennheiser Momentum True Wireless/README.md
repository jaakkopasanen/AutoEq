# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.5; 28 -8.9; 31 -9.2; 34 -9.5; 37 -9.7; 41 -10.0; 45 -10.2; 49 -10.4; 54 -10.6; 60 -10.9; 66 -11.1; 72 -11.3; 79 -11.5; 87 -11.7; 96 -11.8; 106 -11.8; 116 -11.7; 128 -12.6; 141 -12.6; 155 -12.3; 170 -12.1; 187 -11.8; 206 -11.4; 227 -11.0; 249 -10.5; 274 -10.2; 302 -10.2; 332 -9.6; 365 -9.0; 402 -8.6; 442 -8.2; 486 -7.8; 535 -7.4; 588 -7.0; 647 -6.7; 712 -6.3; 783 -6.1; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.7; 1261 -6.5; 1387 -6.4; 1526 -6.0; 1678 -5.5; 1846 -4.6; 2031 -3.2; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -4.2; 7010 -7.0; 7711 -6.3; 8482 -7.3; 9330 -12.3; 10263 -14.1; 11289 -10.2; 12418 -10.0; 13660 -19.1; 15026 -29.1; 16529 -30.2; 18182 -21.9; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.55 | -2.7 dB  |
| Peaking | 160 Hz   | 0.58 | -5.0 dB  |
| Peaking | 3829 Hz  | 0.82 | 7.5 dB   |
| Peaking | 15657 Hz | 1.42 | -21.8 dB |
| Peaking | 17571 Hz | 1.5  | -10.0 dB |
| Peaking | 2351 Hz  | 1.03 | -3.5 dB  |
| Peaking | 2374 Hz  | 2.33 | 5.4 dB   |
| Peaking | 5610 Hz  | 5.96 | 3.0 dB   |
| Peaking | 9905 Hz  | 4.85 | -5.5 dB  |
| Peaking | 12108 Hz | 4.97 | 6.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -28.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)