# Sennheiser Momentum M2 OEBT Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.6; 25 -11.0; 28 -11.6; 31 -12.0; 34 -12.3; 37 -12.5; 41 -12.9; 45 -13.1; 49 -13.1; 54 -13.2; 60 -13.4; 66 -9.4; 72 -10.4; 79 -11.9; 87 -11.1; 96 -10.6; 106 -9.7; 116 -9.0; 128 -8.6; 141 -7.9; 155 -7.3; 170 -6.7; 187 -6.3; 206 -5.9; 227 -5.4; 249 -4.6; 274 -3.7; 302 -2.9; 332 -2.3; 365 -2.2; 402 -2.2; 442 -2.3; 486 -2.7; 535 -3.0; 588 -3.1; 647 -3.7; 712 -4.4; 783 -4.9; 861 -5.6; 947 -6.2; 1042 -6.7; 1146 -7.0; 1261 -7.3; 1387 -8.2; 1526 -9.2; 1678 -10.3; 1846 -10.7; 2031 -11.2; 2234 -11.3; 2457 -10.4; 2703 -9.3; 2973 -7.4; 3270 -5.3; 3597 -3.5; 3957 -0.9; 4353 -0.5; 4788 -2.4; 5267 -4.8; 5793 -2.4; 6373 -2.4; 7010 -4.5; 7711 -6.2; 8482 -7.6; 9330 -9.2; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 40 Hz   | 0.68 | -6.0 dB |
| Peaking | 94 Hz   | 0.8  | -2.2 dB |
| Peaking | 409 Hz  | 0.76 | 4.9 dB  |
| Peaking | 2229 Hz | 1.08 | -6.6 dB |
| Peaking | 4137 Hz | 1.56 | 7.7 dB  |
| Peaking | 68 Hz   | 3.43 | -2.5 dB |
| Peaking | 68 Hz   | 8.25 | 5.3 dB  |
| Peaking | 5209 Hz | 7.95 | -2.9 dB |
| Peaking | 6124 Hz | 4.34 | 3.2 dB  |
| Peaking | 9123 Hz | 4.74 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wireless/Sennheiser%20Momentum%20M2%20OEBT%20Wireless.png)