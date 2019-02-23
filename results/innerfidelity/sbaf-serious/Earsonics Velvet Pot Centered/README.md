# Earsonics Velvet Pot Centered
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.3; 25 -11.5; 28 -11.7; 31 -11.9; 34 -12.0; 37 -12.1; 41 -12.2; 45 -12.2; 49 -12.2; 54 -12.3; 60 -12.3; 66 -12.2; 72 -12.2; 79 -12.1; 87 -12.0; 96 -11.7; 106 -11.2; 116 -10.6; 128 -10.0; 141 -9.2; 155 -8.2; 170 -7.2; 187 -6.0; 206 -5.0; 227 -4.1; 249 -4.0; 274 -4.1; 302 -4.8; 332 -5.5; 365 -6.2; 402 -6.8; 442 -7.2; 486 -7.9; 535 -8.2; 588 -8.1; 647 -8.3; 712 -8.6; 783 -8.6; 861 -9.0; 947 -9.5; 1042 -9.9; 1146 -10.3; 1261 -10.7; 1387 -11.2; 1526 -11.5; 1678 -11.3; 1846 -10.3; 2031 -8.3; 2234 -6.5; 2457 -5.1; 2703 -3.5; 2973 -2.1; 3270 -1.3; 3597 -0.7; 3957 -0.5; 4353 -1.7; 4788 -4.2; 5267 -1.8; 5793 -0.6; 6373 -3.0; 7010 -7.8; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -6.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot Centered GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot Centered ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.75 | -5.9 dB |
| Peaking | 89 Hz   | 1.75 | -4.2 dB |
| Peaking | 1476 Hz | 1.05 | -5.9 dB |
| Peaking | 3403 Hz | 1.5  | 7.2 dB  |
| Peaking | 5740 Hz | 6.5  | 5.1 dB  |
| Peaking | 35 Hz   | 3.62 | 0.3 dB  |
| Peaking | 136 Hz  | 2.22 | -1.8 dB |
| Peaking | 246 Hz  | 1.51 | 3.6 dB  |
| Peaking | 533 Hz  | 1.64 | -1.3 dB |
| Peaking | 7108 Hz | 9.67 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20Centered/Earsonics%20Velvet%20Pot%20Centered.png)