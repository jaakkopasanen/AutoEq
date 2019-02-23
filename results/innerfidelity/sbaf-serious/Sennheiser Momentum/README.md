# Sennheiser Momentum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.8; 25 -6.0; 28 -6.2; 31 -6.4; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.4; 87 -8.9; 96 -9.3; 106 -9.4; 116 -9.4; 128 -9.4; 141 -9.4; 155 -10.2; 170 -10.0; 187 -10.1; 206 -10.4; 227 -10.4; 249 -10.2; 274 -9.8; 302 -9.5; 332 -9.0; 365 -8.4; 402 -7.9; 442 -7.6; 486 -7.7; 535 -7.7; 588 -7.6; 647 -8.0; 712 -8.4; 783 -8.5; 861 -8.9; 947 -9.2; 1042 -9.1; 1146 -9.0; 1261 -9.2; 1387 -9.9; 1526 -10.5; 1678 -10.5; 1846 -9.9; 2031 -8.9; 2234 -7.6; 2457 -5.4; 2703 -4.1; 2973 -2.4; 3270 -1.3; 3597 -1.7; 3957 -1.0; 4353 -0.5; 4788 -1.4; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 1.13 | -2.0 dB |
| Peaking | 221 Hz  | 1.07 | -3.5 dB |
| Peaking | 1718 Hz | 0.85 | -5.4 dB |
| Peaking | 3475 Hz | 1.16 | 7.5 dB  |
| Peaking | 5956 Hz | 4.13 | 4.5 dB  |
| Peaking | 20 Hz   | 1.5  | 1.0 dB  |
| Peaking | 3715 Hz | 5.17 | -2.8 dB |
| Peaking | 4053 Hz | 2.3  | 2.3 dB  |
| Peaking | 6639 Hz | 6.48 | 2.6 dB  |
| Peaking | 7101 Hz | 1.44 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)