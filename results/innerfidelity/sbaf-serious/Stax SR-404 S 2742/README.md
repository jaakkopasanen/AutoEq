# Stax SR-404 S 2742
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.3; 31 -1.5; 34 -1.7; 37 -1.8; 41 -1.9; 45 -2.0; 49 -2.1; 54 -2.1; 60 -2.4; 66 -2.8; 72 -3.1; 79 -3.4; 87 -3.6; 96 -4.0; 106 -4.4; 116 -4.6; 128 -4.8; 141 -5.0; 155 -5.1; 170 -5.1; 187 -5.3; 206 -5.3; 227 -5.3; 249 -5.5; 274 -5.4; 302 -5.4; 332 -5.4; 365 -5.3; 402 -5.3; 442 -5.3; 486 -5.6; 535 -5.7; 588 -5.4; 647 -5.7; 712 -6.0; 783 -6.0; 861 -6.5; 947 -7.0; 1042 -7.5; 1146 -8.0; 1261 -9.1; 1387 -9.9; 1526 -10.6; 1678 -11.4; 1846 -9.9; 2031 -7.0; 2234 -4.6; 2457 -3.2; 2703 -4.5; 2973 -6.5; 3270 -6.3; 3597 -5.7; 3957 -4.3; 4353 -4.3; 4788 -5.2; 5267 -5.2; 5793 -6.9; 6373 -7.0; 7010 -4.0; 7711 -5.9; 8482 -9.6; 9330 -11.6; 10263 -8.6; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -8.0; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 S 2742 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 S 2742 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.31 | 5.0 dB  |
| Peaking | 133 Hz   | 0    | 0.7 dB  |
| Peaking | 1715 Hz  | 1.72 | -7.9 dB |
| Peaking | 2244 Hz  | 2    | 5.1 dB  |
| Peaking | 9319 Hz  | 5.62 | -6.2 dB |
| Peaking | 1207 Hz  | 4.27 | -0.7 dB |
| Peaking | 3114 Hz  | 6.56 | -1.9 dB |
| Peaking | 4186 Hz  | 5.93 | 1.8 dB  |
| Peaking | 7927 Hz  | 4.06 | -1.1 dB |
| Peaking | 19770 Hz | 1.28 | -6.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-404%20S%202742/Stax%20SR-404%20S%202742.png)