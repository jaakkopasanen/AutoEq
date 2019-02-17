# Audiofly Adagio Club Life
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.9; 34 -1.3; 37 -1.7; 41 -2.2; 45 -2.6; 49 -3.0; 54 -3.4; 60 -3.9; 66 -4.3; 72 -4.7; 79 -5.3; 87 -5.6; 96 -6.1; 106 -6.4; 116 -6.6; 128 -7.0; 141 -7.2; 155 -7.4; 170 -7.7; 187 -7.7; 206 -7.8; 227 -7.6; 249 -7.7; 274 -7.5; 302 -7.3; 332 -7.2; 365 -6.9; 402 -6.6; 442 -6.2; 486 -6.0; 535 -5.7; 588 -5.3; 647 -5.1; 712 -5.3; 783 -5.2; 861 -5.5; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.3; 1387 -8.9; 1526 -8.9; 1678 -8.4; 1846 -7.3; 2031 -6.0; 2234 -5.1; 2457 -4.4; 2703 -4.4; 2973 -5.1; 3270 -4.6; 3597 -2.3; 3957 -0.5; 4353 -0.8; 4788 -1.3; 5267 -1.5; 5793 -3.2; 6373 -5.0; 7010 -7.2; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audiofly Adagio Club Life GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audiofly Adagio Club Life ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.23 | 6.2 dB  |
| Peaking | 48 Hz   | 1.81 | 2.4 dB  |
| Peaking | 1490 Hz | 3.1  | -3.1 dB |
| Peaking | 2413 Hz | 4.34 | 1.6 dB  |
| Peaking | 4372 Hz | 2.09 | 6.4 dB  |
| Peaking | 216 Hz  | 1.09 | -1.5 dB |
| Peaking | 700 Hz  | 1.42 | 1.7 dB  |
| Peaking | 1172 Hz | 3.65 | -1.0 dB |
| Peaking | 5469 Hz | 6.54 | 1.7 dB  |
| Peaking | 7215 Hz | 4.62 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audiofly%20Adagio%20Club%20Life/Audiofly%20Adagio%20Club%20Life.png)