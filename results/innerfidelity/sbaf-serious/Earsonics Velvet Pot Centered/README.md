# Earsonics Velvet Pot Centered
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.2; 28 -8.5; 31 -8.6; 34 -8.8; 37 -8.9; 41 -8.9; 45 -9.0; 49 -9.0; 54 -9.0; 60 -9.0; 66 -9.0; 72 -9.0; 79 -8.9; 87 -8.7; 96 -8.5; 106 -8.0; 116 -7.4; 128 -6.8; 141 -5.9; 155 -5.0; 170 -3.9; 187 -2.7; 206 -1.7; 227 -0.9; 249 -0.7; 274 -0.9; 302 -1.6; 332 -2.2; 365 -3.0; 402 -3.6; 442 -4.0; 486 -4.6; 535 -5.0; 588 -4.9; 647 -5.1; 712 -5.4; 783 -5.4; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.5; 1387 -7.9; 1526 -8.2; 1678 -8.1; 1846 -7.1; 2031 -5.0; 2234 -3.3; 2457 -1.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot Centered GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot Centered ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.68 | -1.6 dB |
| Peaking | 102 Hz  | 0.61 | -3.0 dB |
| Peaking | 239 Hz  | 0.95 | 7.1 dB  |
| Peaking | 1581 Hz | 1.8  | -4.6 dB |
| Peaking | 3509 Hz | 0.76 | 7.2 dB  |
| Peaking | 1871 Hz | 8.9  | -0.6 dB |
| Peaking | 2655 Hz | 3.24 | 1.2 dB  |
| Peaking | 3447 Hz | 2.54 | -1.0 dB |
| Peaking | 6131 Hz | 2.53 | 5.2 dB  |
| Peaking | 7307 Hz | 1.39 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 6.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20Centered/Earsonics%20Velvet%20Pot%20Centered.png)