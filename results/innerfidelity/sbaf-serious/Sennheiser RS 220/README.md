# Sennheiser RS 220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.4; 34 -1.9; 37 -2.4; 41 -2.9; 45 -3.3; 49 -3.6; 54 -4.1; 60 -4.5; 66 -4.4; 72 -4.3; 79 -5.4; 87 -6.3; 96 -6.9; 106 -7.3; 116 -7.6; 128 -7.8; 141 -7.9; 155 -8.1; 170 -7.9; 187 -8.0; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.3; 302 -7.2; 332 -7.2; 365 -7.0; 402 -7.0; 442 -6.7; 486 -6.6; 535 -6.3; 588 -6.0; 647 -5.8; 712 -6.0; 783 -5.5; 861 -6.0; 947 -6.3; 1042 -6.4; 1146 -6.5; 1261 -6.5; 1387 -5.1; 1526 -2.4; 1678 -2.1; 1846 -1.6; 2031 -4.7; 2234 -8.5; 2457 -10.5; 2703 -9.1; 2973 -7.0; 3270 -5.9; 3597 -4.4; 3957 -2.0; 4353 -0.5; 4788 -0.5; 5267 -2.5; 5793 -5.1; 6373 -2.6; 7010 -6.7; 7711 -7.5; 8482 -7.5; 9330 -8.5; 10263 -8.9; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.44 | 6.3 dB  |
| Peaking | 46 Hz   | 2.06 | 2.1 dB  |
| Peaking | 1784 Hz | 2.96 | 6.5 dB  |
| Peaking | 2419 Hz | 3.03 | -6.0 dB |
| Peaking | 4509 Hz | 2.71 | 6.9 dB  |
| Peaking | 18 Hz   | 0.49 | 0.6 dB  |
| Peaking | 71 Hz   | 4    | 1.8 dB  |
| Peaking | 155 Hz  | 0.83 | -1.8 dB |
| Peaking | 2002 Hz | 2.53 | 0.2 dB  |
| Peaking | 9678 Hz | 3.24 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)