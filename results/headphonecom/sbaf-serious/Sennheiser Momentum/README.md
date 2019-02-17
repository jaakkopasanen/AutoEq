# Sennheiser Momentum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.4; 28 -3.7; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.7; 54 -4.9; 60 -5.3; 66 -5.4; 72 -5.7; 79 -6.1; 87 -6.3; 96 -6.5; 106 -6.7; 116 -6.6; 128 -6.6; 141 -6.8; 155 -7.5; 170 -7.3; 187 -7.5; 206 -7.7; 227 -7.6; 249 -7.5; 274 -6.9; 302 -6.8; 332 -6.1; 365 -5.3; 402 -5.0; 442 -4.9; 486 -4.8; 535 -4.9; 588 -4.9; 647 -5.3; 712 -5.8; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.3; 1261 -6.7; 1387 -7.5; 1526 -8.0; 1678 -7.9; 1846 -7.8; 2031 -6.8; 2234 -5.2; 2457 -3.2; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.35 | 3.4 dB  |
| Peaking | 46 Hz   | 2.02 | 1.4 dB  |
| Peaking | 504 Hz  | 2.4  | 1.9 dB  |
| Peaking | 1751 Hz | 1.91 | -4.1 dB |
| Peaking | 3749 Hz | 0.84 | 7.2 dB  |
| Peaking | 203 Hz  | 2.03 | -1.4 dB |
| Peaking | 2797 Hz | 6.1  | 1.5 dB  |
| Peaking | 3816 Hz | 2.74 | -1.0 dB |
| Peaking | 6259 Hz | 2.29 | 5.8 dB  |
| Peaking | 7330 Hz | 1.47 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)