# Earsonics Velvet Pot CW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.1; 25 -10.4; 28 -10.6; 31 -10.8; 34 -10.9; 37 -10.9; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.3; 60 -11.4; 66 -11.5; 72 -11.5; 79 -11.5; 87 -11.5; 96 -11.4; 106 -11.0; 116 -10.5; 128 -10.1; 141 -9.4; 155 -8.6; 170 -7.7; 187 -6.6; 206 -5.4; 227 -4.2; 249 -3.3; 274 -2.7; 302 -2.4; 332 -2.6; 365 -2.9; 402 -3.4; 442 -3.8; 486 -4.4; 535 -4.7; 588 -4.7; 647 -4.9; 712 -5.3; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.6; 1146 -7.0; 1261 -7.4; 1387 -7.9; 1526 -8.2; 1678 -8.1; 1846 -7.1; 2031 -5.0; 2234 -3.2; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot CW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.4  | -3.3 dB |
| Peaking | 121 Hz  | 0.52 | -4.7 dB |
| Peaking | 279 Hz  | 0.85 | 6.5 dB  |
| Peaking | 1581 Hz | 1.8  | -4.7 dB |
| Peaking | 3521 Hz | 0.76 | 7.2 dB  |
| Peaking | 1870 Hz | 8.49 | -0.7 dB |
| Peaking | 2645 Hz | 2.98 | 1.2 dB  |
| Peaking | 3462 Hz | 2.49 | -1.1 dB |
| Peaking | 6177 Hz | 2.44 | 5.3 dB  |
| Peaking | 7309 Hz | 1.42 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CW/Earsonics%20Velvet%20Pot%20CW.png)