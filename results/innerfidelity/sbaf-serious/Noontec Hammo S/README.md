# Noontec Hammo S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.6; 28 -6.8; 31 -7.0; 34 -7.2; 37 -7.3; 41 -7.3; 45 -7.4; 49 -7.5; 54 -7.7; 60 -7.7; 66 -7.9; 72 -8.0; 79 -8.0; 87 -8.1; 96 -8.0; 106 -7.6; 116 -7.5; 128 -8.4; 141 -9.5; 155 -10.1; 170 -8.9; 187 -9.9; 206 -9.8; 227 -9.6; 249 -9.0; 274 -8.3; 302 -7.7; 332 -7.0; 365 -6.2; 402 -5.4; 442 -5.2; 486 -5.0; 535 -4.9; 588 -5.2; 647 -6.0; 712 -6.6; 783 -6.2; 861 -6.1; 947 -6.3; 1042 -7.4; 1146 -8.0; 1261 -8.7; 1387 -9.2; 1526 -9.6; 1678 -9.6; 1846 -9.3; 2031 -8.4; 2234 -7.4; 2457 -5.7; 2703 -4.6; 2973 -3.7; 3270 -4.2; 3597 -7.6; 3957 -5.7; 4353 -7.1; 4788 -3.8; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 245 Hz  | 0.6  | -5.4 dB |
| Peaking | 418 Hz  | 0.81 | 5.0 dB  |
| Peaking | 1619 Hz | 1.28 | -3.6 dB |
| Peaking | 2839 Hz | 3.82 | 3.6 dB  |
| Peaking | 5801 Hz | 3.5  | 7.0 dB  |
| Peaking | 66 Hz   | 0.64 | -0.6 dB |
| Peaking | 112 Hz  | 4.79 | 1.5 dB  |
| Peaking | 4473 Hz | 4.83 | -2.6 dB |
| Peaking | 4904 Hz | 5.2  | 2.4 dB  |
| Peaking | 9413 Hz | 4.89 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S/Noontec%20Hammo%20S.png)