# Sennheiser IE 800 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.8; 34 -2.3; 37 -2.9; 41 -3.5; 45 -4.0; 49 -4.6; 54 -5.1; 60 -5.7; 66 -6.3; 72 -6.8; 79 -7.4; 87 -7.9; 96 -8.5; 106 -8.9; 116 -9.1; 128 -9.6; 141 -9.8; 155 -10.1; 170 -10.2; 187 -10.3; 206 -10.4; 227 -10.2; 249 -10.2; 274 -10.0; 302 -9.8; 332 -9.6; 365 -9.3; 402 -9.0; 442 -8.6; 486 -8.4; 535 -8.1; 588 -7.5; 647 -7.2; 712 -7.1; 783 -6.8; 861 -6.9; 947 -7.2; 1042 -7.5; 1146 -7.7; 1261 -7.9; 1387 -8.2; 1526 -8.4; 1678 -8.2; 1846 -7.2; 2031 -6.0; 2234 -4.5; 2457 -2.3; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.3; 5267 -3.4; 5793 -5.5; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -9.3; 10263 -10.9; 11289 -12.5; 12418 -12.4; 13660 -10.5; 15026 -9.5; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.31 | 6.8 dB  |
| Peaking | 164 Hz   | 0.35 | -4.3 dB |
| Peaking | 3587 Hz  | 1.48 | 7.2 dB  |
| Peaking | 6732 Hz  | 6.87 | 3.8 dB  |
| Peaking | 11901 Hz | 1.39 | -6.6 dB |
| Peaking | 725 Hz   | 1.71 | 1.1 dB  |
| Peaking | 1600 Hz  | 1.5  | -2.7 dB |
| Peaking | 2648 Hz  | 3.21 | 3.1 dB  |
| Peaking | 3560 Hz  | 2.79 | -1.6 dB |
| Peaking | 4417 Hz  | 4.37 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20B/Sennheiser%20IE%20800%20sample%20B.png)