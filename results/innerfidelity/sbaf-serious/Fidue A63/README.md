# Fidue A63
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.6; 28 -6.3; 31 -6.9; 34 -7.4; 37 -7.9; 41 -8.4; 45 -8.8; 49 -9.2; 54 -9.6; 60 -10.0; 66 -10.5; 72 -11.0; 79 -11.5; 87 -11.8; 96 -12.3; 106 -12.5; 116 -12.6; 128 -12.7; 141 -12.9; 155 -12.9; 170 -12.8; 187 -12.6; 206 -12.4; 227 -12.0; 249 -11.7; 274 -11.2; 302 -10.8; 332 -10.2; 365 -9.6; 402 -9.1; 442 -8.4; 486 -8.0; 535 -7.3; 588 -6.5; 647 -5.9; 712 -5.8; 783 -5.4; 861 -5.2; 947 -4.5; 1042 -4.7; 1146 -5.3; 1261 -6.1; 1387 -6.8; 1526 -7.5; 1678 -8.0; 1846 -8.0; 2031 -7.7; 2234 -7.5; 2457 -6.7; 2703 -5.6; 2973 -3.8; 3270 -1.8; 3597 -0.5; 3957 -0.6; 4353 -2.0; 4788 -2.3; 5267 -1.3; 5793 -1.4; 6373 -1.1; 7010 -2.2; 7711 -4.3; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A63 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A63 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.48 | -7.3 dB |
| Peaking | 263 Hz  | 0.91 | -3.4 dB |
| Peaking | 1980 Hz | 1.66 | -3.9 dB |
| Peaking | 3655 Hz | 2.84 | 4.8 dB  |
| Peaking | 5957 Hz | 2.68 | 3.5 dB  |
| Peaking | 19 Hz   | 1.95 | 1.0 dB  |
| Peaking | 457 Hz  | 3.06 | -0.6 dB |
| Peaking | 987 Hz  | 1.85 | 1.3 dB  |
| Peaking | 1432 Hz | 3.52 | -1.1 dB |
| Peaking | 8392 Hz | 5.08 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A63/Fidue%20A63.png)