# FLC Technology FLC8 C C Gn Strin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.7; 49 -1.0; 54 -1.3; 60 -1.7; 66 -2.1; 72 -2.4; 79 -2.9; 87 -3.4; 96 -4.0; 106 -4.3; 116 -4.6; 128 -5.0; 141 -5.4; 155 -5.5; 170 -5.7; 187 -5.9; 206 -6.0; 227 -6.0; 249 -6.1; 274 -5.9; 302 -5.9; 332 -5.8; 365 -5.6; 402 -5.5; 442 -5.2; 486 -5.2; 535 -5.0; 588 -4.6; 647 -4.6; 712 -4.9; 783 -4.8; 861 -5.1; 947 -5.9; 1042 -6.9; 1146 -7.7; 1261 -8.0; 1387 -8.0; 1526 -7.2; 1678 -6.2; 1846 -4.9; 2031 -4.2; 2234 -4.2; 2457 -4.5; 2703 -5.2; 2973 -2.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.9; 4788 -2.1; 5267 -0.5; 5793 -0.8; 6373 -5.8; 7010 -13.1; 7711 -13.3; 8482 -10.9; 9330 -11.1; 10263 -12.6; 11289 -10.3; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technology FLC8 C C Gn Strin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Gn Strin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.43 | 6.3 dB   |
| Peaking | 3523 Hz  | 2.18 | 6.0 dB   |
| Peaking | 5756 Hz  | 2.65 | 8.8 dB   |
| Peaking | 7239 Hz  | 2.74 | -10.5 dB |
| Peaking | 10302 Hz | 3.79 | -5.7 dB  |
| Peaking | 738 Hz   | 1.14 | 2.5 dB   |
| Peaking | 1327 Hz  | 1.44 | -3.5 dB  |
| Peaking | 1965 Hz  | 1.88 | 2.5 dB   |
| Peaking | 2734 Hz  | 8.96 | -2.3 dB  |
| Peaking | 12810 Hz | 5.82 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin.png)