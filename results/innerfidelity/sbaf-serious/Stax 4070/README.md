# Stax 4070
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.8; 25 -2.7; 28 -3.3; 31 -3.4; 34 -3.2; 37 -3.0; 41 -2.6; 45 -2.2; 49 -1.9; 54 -1.7; 60 -1.6; 66 -1.7; 72 -1.9; 79 -2.0; 87 -2.2; 96 -2.4; 106 -2.5; 116 -2.6; 128 -2.9; 141 -3.0; 155 -3.2; 170 -3.1; 187 -3.4; 206 -3.5; 227 -3.5; 249 -3.7; 274 -3.8; 302 -3.8; 332 -3.8; 365 -2.9; 402 -1.3; 442 -0.7; 486 -1.4; 535 -1.5; 588 -0.9; 647 -0.9; 712 -1.4; 783 -1.6; 861 -2.3; 947 -2.7; 1042 -3.1; 1146 -3.4; 1261 -3.9; 1387 -4.6; 1526 -6.0; 1678 -6.9; 1846 -6.8; 2031 -6.3; 2234 -5.5; 2457 -4.9; 2703 -5.4; 2973 -6.5; 3270 -6.8; 3597 -7.9; 3957 -9.2; 4353 -9.8; 4788 -7.3; 5267 -4.4; 5793 -4.1; 6373 -3.4; 7010 -0.5; 7711 -2.5; 8482 -4.2; 9330 -5.8; 10263 -4.1; 11289 -3.4; 12418 -3.4; 13660 -3.0; 15026 -2.8; 16529 -2.8; 18182 -2.8; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax 4070 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax 4070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 61 Hz    | 2.3  | 1.4 dB  |
| Peaking | 620 Hz   | 1.8  | 2.3 dB  |
| Peaking | 1783 Hz  | 1.95 | -4.0 dB |
| Peaking | 4055 Hz  | 2.49 | -6.9 dB |
| Peaking | 19783 Hz | 1.93 | -3.1 dB |
| Peaking | 307 Hz   | 1.41 | -1.5 dB |
| Peaking | 421 Hz   | 5.02 | 2.4 dB  |
| Peaking | 2984 Hz  | 8.79 | -1.2 dB |
| Peaking | 6993 Hz  | 6.93 | 3.6 dB  |
| Peaking | 9317 Hz  | 4.99 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%204070/Stax%204070.png)