# Sennheiser IE 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.6; 28 -7.9; 31 -8.1; 34 -8.3; 37 -8.5; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.4; 60 -9.7; 66 -9.9; 72 -10.2; 79 -10.4; 87 -10.7; 96 -11.0; 106 -11.0; 116 -11.0; 128 -11.2; 141 -11.1; 155 -11.2; 170 -11.0; 187 -10.8; 206 -10.7; 227 -10.3; 249 -10.1; 274 -9.8; 302 -9.5; 332 -9.1; 365 -8.8; 402 -8.5; 442 -8.0; 486 -7.8; 535 -7.5; 588 -6.9; 647 -6.8; 712 -6.7; 783 -6.5; 861 -6.7; 947 -6.9; 1042 -7.3; 1146 -7.5; 1261 -7.7; 1387 -7.8; 1526 -8.1; 1678 -7.9; 1846 -7.0; 2031 -5.7; 2234 -4.1; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -2.9; 5267 -4.2; 5793 -5.2; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -10.3; 10263 -11.8; 11289 -10.2; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.55 | -0.8 dB |
| Peaking | 144 Hz   | 0.45 | -4.4 dB |
| Peaking | 3453 Hz  | 1.57 | 7.1 dB  |
| Peaking | 6613 Hz  | 7.43 | 4.3 dB  |
| Peaking | 10251 Hz | 3.08 | -6.1 dB |
| Peaking | 709 Hz   | 1.83 | 0.9 dB  |
| Peaking | 1564 Hz  | 1.55 | -2.4 dB |
| Peaking | 2569 Hz  | 5.13 | 2.8 dB  |
| Peaking | 11455 Hz | 5.69 | -1.3 dB |
| Peaking | 12423 Hz | 2.71 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800/Sennheiser%20IE%20800.png)