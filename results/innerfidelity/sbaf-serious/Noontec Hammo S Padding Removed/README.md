# Noontec Hammo S Padding Removed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.7; 34 -5.8; 37 -6.0; 41 -6.1; 45 -6.2; 49 -6.3; 54 -6.5; 60 -6.7; 66 -6.8; 72 -7.0; 79 -7.1; 87 -7.2; 96 -7.3; 106 -7.2; 116 -7.5; 128 -8.1; 141 -8.7; 155 -9.1; 170 -8.4; 187 -8.9; 206 -8.9; 227 -8.8; 249 -8.3; 274 -7.6; 302 -7.1; 332 -6.6; 365 -6.5; 402 -6.2; 442 -6.1; 486 -5.9; 535 -5.9; 588 -6.4; 647 -7.3; 712 -7.9; 783 -7.7; 861 -7.6; 947 -7.7; 1042 -8.6; 1146 -9.2; 1261 -9.7; 1387 -10.2; 1526 -10.4; 1678 -10.3; 1846 -9.7; 2031 -8.5; 2234 -7.2; 2457 -5.3; 2703 -3.9; 2973 -3.3; 3270 -3.7; 3597 -7.6; 3957 -5.1; 4353 -6.7; 4788 -3.1; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.2; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo S Padding Removed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S Padding Removed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.36 | 1.7 dB  |
| Peaking | 173 Hz  | 1.37 | -2.6 dB |
| Peaking | 1546 Hz | 1.36 | -4.4 dB |
| Peaking | 2820 Hz | 3.56 | 4.2 dB  |
| Peaking | 5776 Hz | 3.26 | 6.9 dB  |
| Peaking | 237 Hz  | 5    | -0.8 dB |
| Peaking | 509 Hz  | 1.63 | 1.3 dB  |
| Peaking | 695 Hz  | 3.95 | -1.3 dB |
| Peaking | 9533 Hz | 3.22 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S%20Padding%20Removed/Noontec%20Hammo%20S%20Padding%20Removed.png)