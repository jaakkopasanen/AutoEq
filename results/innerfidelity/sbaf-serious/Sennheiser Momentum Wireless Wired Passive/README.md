# Sennheiser Momentum Wireless Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.6; 25 -5.0; 28 -5.4; 31 -5.8; 34 -6.0; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.0; 60 -7.3; 66 -7.5; 72 -7.7; 79 -8.0; 87 -8.3; 96 -8.7; 106 -8.8; 116 -8.8; 128 -8.7; 141 -8.4; 155 -8.7; 170 -8.2; 187 -7.7; 206 -7.4; 227 -6.8; 249 -6.2; 274 -5.8; 302 -5.0; 332 -4.4; 365 -4.4; 402 -5.0; 442 -5.3; 486 -5.7; 535 -6.0; 588 -6.0; 647 -6.0; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.7; 1526 -8.3; 1678 -8.3; 1846 -8.6; 2031 -8.1; 2234 -7.1; 2457 -5.5; 2703 -4.1; 2973 -2.1; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.8; 5267 -3.0; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum Wireless Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.99 | 3.2 dB  |
| Peaking | 119 Hz  | 0.71 | -2.5 dB |
| Peaking | 341 Hz  | 1.88 | 2.8 dB  |
| Peaking | 3714 Hz | 2.49 | 6.8 dB  |
| Peaking | 6048 Hz | 4.24 | 5.6 dB  |
| Peaking | 1811 Hz | 2.11 | -2.8 dB |
| Peaking | 2964 Hz | 4.7  | 2.0 dB  |
| Peaking | 6675 Hz | 8.12 | 1.5 dB  |
| Peaking | 7771 Hz | 2.64 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Passive/Sennheiser%20Momentum%20Wireless%20Wired%20Passive.png)