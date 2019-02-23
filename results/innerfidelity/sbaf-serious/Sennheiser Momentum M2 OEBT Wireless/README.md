# Sennheiser Momentum M2 OEBT Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -11.1; 25 -11.5; 28 -12.1; 31 -12.5; 34 -12.8; 37 -13.0; 41 -13.4; 45 -13.6; 49 -13.6; 54 -13.7; 60 -13.9; 66 -9.9; 72 -11.0; 79 -12.4; 87 -11.6; 96 -11.1; 106 -10.2; 116 -9.5; 128 -9.1; 141 -8.4; 155 -7.8; 170 -7.2; 187 -6.8; 206 -6.4; 227 -5.9; 249 -5.2; 274 -4.2; 302 -3.4; 332 -2.8; 365 -2.7; 402 -2.7; 442 -2.8; 486 -3.2; 535 -3.5; 588 -3.6; 647 -4.2; 712 -4.9; 783 -5.4; 861 -6.1; 947 -6.7; 1042 -7.2; 1146 -7.5; 1261 -7.8; 1387 -8.7; 1526 -9.7; 1678 -10.8; 1846 -11.2; 2031 -11.7; 2234 -11.9; 2457 -10.9; 2703 -9.8; 2973 -7.9; 3270 -5.8; 3597 -4.0; 3957 -1.4; 4353 -0.5; 4788 -2.9; 5267 -5.3; 5793 -2.9; 6373 -2.9; 7010 -5.0; 7711 -6.0; 8482 -8.1; 9330 -9.7; 10263 -6.7; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 OEBT Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 1.12 | -5.6 dB |
| Peaking | 52 Hz   | 2.09 | -5.2 dB |
| Peaking | 91 Hz   | 2.19 | -4.2 dB |
| Peaking | 2147 Hz | 1.69 | -6.6 dB |
| Peaking | 4220 Hz | 2.37 | 6.6 dB  |
| Peaking | 190 Hz  | 0.89 | -3.6 dB |
| Peaking | 345 Hz  | 0.55 | 5.4 dB  |
| Peaking | 1132 Hz | 0.88 | -1.6 dB |
| Peaking | 6246 Hz | 7.17 | 3.3 dB  |
| Peaking | 9204 Hz | 5.38 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wireless/Sennheiser%20Momentum%20M2%20OEBT%20Wireless.png)