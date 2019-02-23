# Sennheiser Momentum M2 OEBT Wired Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.2; 25 -2.7; 28 -3.5; 31 -4.3; 34 -5.0; 37 -5.5; 41 -6.2; 45 -7.1; 49 -7.9; 54 -9.0; 60 -10.1; 66 -10.9; 72 -11.2; 79 -11.6; 87 -12.5; 96 -12.7; 106 -12.0; 116 -11.2; 128 -10.2; 141 -9.1; 155 -8.0; 170 -7.2; 187 -6.6; 206 -6.2; 227 -5.6; 249 -5.0; 274 -4.3; 302 -3.6; 332 -2.9; 365 -2.8; 402 -3.1; 442 -3.3; 486 -3.6; 535 -3.8; 588 -3.9; 647 -4.4; 712 -5.0; 783 -5.4; 861 -6.0; 947 -6.5; 1042 -6.9; 1146 -7.0; 1261 -7.4; 1387 -8.2; 1526 -9.3; 1678 -10.2; 1846 -10.9; 2031 -11.3; 2234 -11.7; 2457 -10.8; 2703 -9.8; 2973 -7.8; 3270 -5.5; 3597 -3.7; 3957 -0.7; 4353 -0.5; 4788 -3.1; 5267 -5.1; 5793 -2.6; 6373 -3.9; 7010 -6.3; 7711 -7.2; 8482 -9.4; 9330 -10.7; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 OEBT Wired Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.86 | 5.3 dB  |
| Peaking | 90 Hz   | 0.94 | -7.0 dB |
| Peaking | 377 Hz  | 0.7  | 4.1 dB  |
| Peaking | 2214 Hz | 1.11 | -6.1 dB |
| Peaking | 4092 Hz | 2.21 | 7.9 dB  |
| Peaking | 5117 Hz | 9.26 | -2.3 dB |
| Peaking | 5940 Hz | 5.45 | 3.4 dB  |
| Peaking | 8982 Hz | 4.59 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active.png)