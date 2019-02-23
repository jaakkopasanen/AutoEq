# Stax 4070
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.8; 25 -2.7; 28 -3.3; 31 -3.4; 34 -3.2; 37 -2.9; 41 -2.5; 45 -2.2; 49 -1.9; 54 -1.7; 60 -1.6; 66 -1.7; 72 -1.9; 79 -2.0; 87 -2.2; 96 -2.4; 106 -2.5; 116 -2.6; 128 -2.9; 141 -3.0; 155 -3.2; 170 -3.1; 187 -3.4; 206 -3.5; 227 -3.5; 249 -3.6; 274 -3.8; 302 -3.8; 332 -3.8; 365 -2.9; 402 -1.2; 442 -0.6; 486 -1.4; 535 -1.4; 588 -0.9; 647 -0.8; 712 -1.4; 783 -1.6; 861 -2.3; 947 -2.7; 1042 -3.0; 1146 -3.3; 1261 -3.8; 1387 -4.6; 1526 -6.0; 1678 -6.9; 1846 -6.8; 2031 -6.3; 2234 -5.5; 2457 -4.8; 2703 -5.4; 2973 -6.5; 3270 -6.8; 3597 -7.9; 3957 -9.2; 4353 -9.8; 4788 -7.3; 5267 -4.4; 5793 -4.0; 6373 -3.3; 7010 -1.4; 7711 -3.6; 8482 -4.3; 9330 -5.8; 10263 -4.1; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax 4070 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax 4070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.88 | 3.7 dB  |
| Peaking | 67 Hz   | 0.97 | 2.2 dB  |
| Peaking | 611 Hz  | 1.16 | 3.2 dB  |
| Peaking | 1772 Hz | 2.4  | -3.4 dB |
| Peaking | 4059 Hz | 3.07 | -6.2 dB |
| Peaking | 355 Hz  | 1.85 | -1.5 dB |
| Peaking | 415 Hz  | 4.83 | 2.6 dB  |
| Peaking | 3063 Hz | 8.5  | -1.3 dB |
| Peaking | 6882 Hz | 7.12 | 3.6 dB  |
| Peaking | 9254 Hz | 7.37 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%204070/Stax%204070.png)