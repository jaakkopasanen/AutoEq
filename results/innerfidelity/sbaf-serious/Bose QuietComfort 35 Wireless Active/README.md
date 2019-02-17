# Bose QuietComfort 35 Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -9.5; 25 -8.9; 28 -8.4; 31 -8.1; 34 -8.1; 37 -8.0; 41 -8.0; 45 -7.9; 49 -7.8; 54 -7.6; 60 -7.3; 66 -7.2; 72 -7.1; 79 -7.2; 87 -7.3; 96 -7.4; 106 -7.3; 116 -7.2; 128 -7.1; 141 -7.0; 155 -6.8; 170 -6.3; 187 -6.4; 206 -6.3; 227 -6.1; 249 -5.9; 274 -5.6; 302 -5.3; 332 -5.1; 365 -4.8; 402 -4.7; 442 -4.3; 486 -4.4; 535 -4.3; 588 -4.1; 647 -4.3; 712 -4.6; 783 -4.6; 861 -5.0; 947 -5.3; 1042 -4.9; 1146 -4.1; 1261 -3.0; 1387 -2.8; 1526 -2.0; 1678 -3.2; 1846 -3.5; 2031 -5.2; 2234 -6.3; 2457 -6.6; 2703 -7.8; 2973 -7.2; 3270 -5.3; 3597 -5.2; 3957 -7.5; 4353 -7.3; 4788 -5.5; 5267 -0.5; 5793 -3.3; 6373 -6.1; 7010 -4.0; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 116 Hz  |  1.03 | -1.7 dB |
| Peaking | 1626 Hz |  1.41 | 5.1 dB  |
| Peaking | 2330 Hz |  0.96 | -3.9 dB |
| Peaking | 5430 Hz | 10.89 | 7.0 dB  |
| Peaking | 17 Hz   |  1.61 | -5.4 dB |
| Peaking | 38 Hz   |  0.63 | -2.1 dB |
| Peaking | 507 Hz  |  2.26 | 1.0 dB  |
| Peaking | 3467 Hz |  8.61 | 2.7 dB  |
| Peaking | 4138 Hz |  4.85 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wireless%20Active/Bose%20QuietComfort%2035%20Wireless%20Active.png)