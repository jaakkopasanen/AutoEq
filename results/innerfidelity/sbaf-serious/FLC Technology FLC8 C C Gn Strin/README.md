# FLC Technology FLC8 C C Gn Strin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.1; 31 -1.3; 34 -1.4; 37 -1.6; 41 -1.8; 45 -2.0; 49 -2.3; 54 -2.6; 60 -3.0; 66 -3.4; 72 -3.7; 79 -4.2; 87 -4.7; 96 -5.3; 106 -5.7; 116 -5.9; 128 -6.3; 141 -6.7; 155 -6.9; 170 -7.0; 187 -7.2; 206 -7.4; 227 -7.3; 249 -7.4; 274 -7.2; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.8; 442 -6.5; 486 -6.5; 535 -6.3; 588 -6.0; 647 -5.9; 712 -6.2; 783 -6.1; 861 -6.4; 947 -7.2; 1042 -8.2; 1146 -9.0; 1261 -9.3; 1387 -9.3; 1526 -8.5; 1678 -7.5; 1846 -6.2; 2031 -5.5; 2234 -5.5; 2457 -5.8; 2703 -6.5; 2973 -3.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.2; 4788 -3.4; 5267 -0.9; 5793 -1.9; 6373 -7.1; 7010 -14.4; 7711 -14.6; 8482 -12.3; 9330 -12.4; 10263 -13.9; 11289 -11.6; 12418 -7.3; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technology FLC8 C C Gn Strin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Gn Strin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.64 | 5.9 dB   |
| Peaking | 3569 Hz  | 3.57 | 6.8 dB   |
| Peaking | 5627 Hz  | 3.08 | 8.9 dB   |
| Peaking | 7256 Hz  | 2.54 | -10.6 dB |
| Peaking | 10366 Hz | 3.5  | -6.6 dB  |
| Peaking | 67 Hz    | 2.14 | 0.9 dB   |
| Peaking | 201 Hz   | 1.22 | -1.2 dB  |
| Peaking | 1293 Hz  | 3.13 | -3.4 dB  |
| Peaking | 13059 Hz | 4.87 | 1.1 dB   |
| Peaking | 14988 Hz | 2.64 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin.png)