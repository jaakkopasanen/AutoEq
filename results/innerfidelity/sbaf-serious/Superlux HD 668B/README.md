# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.2; 37 -3.4; 41 -4.9; 45 -6.1; 49 -7.3; 54 -8.6; 60 -9.7; 66 -10.4; 72 -10.4; 79 -10.6; 87 -11.2; 96 -12.2; 106 -12.0; 116 -11.3; 128 -11.4; 141 -11.4; 155 -10.9; 170 -10.4; 187 -10.2; 206 -9.9; 227 -9.2; 249 -9.4; 274 -9.2; 302 -9.0; 332 -8.7; 365 -8.1; 402 -7.9; 442 -7.4; 486 -7.3; 535 -7.3; 588 -6.7; 647 -6.1; 712 -6.4; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.8; 1261 -7.1; 1387 -8.0; 1526 -9.4; 1678 -10.9; 1846 -12.2; 2031 -12.9; 2234 -12.8; 2457 -12.5; 2703 -11.5; 2973 -10.5; 3270 -9.5; 3597 -8.3; 3957 -7.8; 4353 -7.6; 4788 -7.0; 5267 -10.3; 5793 -16.8; 6373 -12.3; 7010 -11.9; 7711 -14.7; 8482 -18.0; 9330 -17.9; 10263 -14.2; 11289 -10.6; 12418 -8.8; 13660 -9.9; 15026 -12.5; 16529 -11.9; 18182 -8.8; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.86 | 8.2 dB   |
| Peaking | 91 Hz    | 0.49 | -6.3 dB  |
| Peaking | 2169 Hz  | 1.94 | -6.7 dB  |
| Peaking | 8618 Hz  | 1.5  | -11.1 dB |
| Peaking | 16057 Hz | 1.92 | -5.9 dB  |
| Peaking | 827 Hz   | 1.84 | 1.1 dB   |
| Peaking | 5067 Hz  | 5.3  | 5.9 dB   |
| Peaking | 5621 Hz  | 6.26 | -11.5 dB |
| Peaking | 8682 Hz  | 1.25 | 4.4 dB   |
| Peaking | 9068 Hz  | 2.86 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB   |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20668B/Superlux%20HD%20668B.png)