# Sennheiser Momentum M2 OEBT Wired Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.0; 25 -2.5; 28 -3.3; 31 -4.1; 34 -4.8; 37 -5.3; 41 -6.0; 45 -6.9; 49 -7.7; 54 -8.8; 60 -9.9; 66 -10.7; 72 -11.0; 79 -11.4; 87 -12.3; 96 -12.5; 106 -11.8; 116 -11.0; 128 -10.0; 141 -8.9; 155 -7.8; 170 -7.0; 187 -6.4; 206 -6.0; 227 -5.4; 249 -4.8; 274 -4.1; 302 -3.4; 332 -2.7; 365 -2.6; 402 -2.9; 442 -3.1; 486 -3.4; 535 -3.6; 588 -3.7; 647 -4.2; 712 -4.8; 783 -5.2; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -7.2; 1387 -8.0; 1526 -9.1; 1678 -10.0; 1846 -10.7; 2031 -11.1; 2234 -11.5; 2457 -10.6; 2703 -9.5; 2973 -7.6; 3270 -5.3; 3597 -3.5; 3957 -0.6; 4353 -0.5; 4788 -2.9; 5267 -4.9; 5793 -2.4; 6373 -3.6; 7010 -6.1; 7711 -7.0; 8482 -9.2; 9330 -10.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 20 Hz   | 0.84 | 5.5 dB  |
| Peaking | 90 Hz   | 0.95 | -6.8 dB |
| Peaking | 380 Hz  | 0.68 | 4.3 dB  |
| Peaking | 2227 Hz | 1.14 | -6.1 dB |
| Peaking | 4092 Hz | 2.06 | 7.9 dB  |
| Peaking | 5127 Hz | 8.88 | -2.4 dB |
| Peaking | 5949 Hz | 5.27 | 3.4 dB  |
| Peaking | 8997 Hz | 4.67 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active.png)