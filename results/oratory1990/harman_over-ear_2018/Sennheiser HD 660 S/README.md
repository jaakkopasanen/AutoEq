# Sennheiser HD 660 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.3; 37 -1.9; 41 -2.6; 45 -3.1; 49 -3.6; 54 -4.0; 60 -4.6; 66 -5.1; 72 -5.3; 79 -5.0; 87 -5.4; 96 -6.6; 106 -7.1; 116 -7.6; 128 -8.0; 141 -8.6; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.4; 227 -9.5; 249 -9.4; 274 -9.2; 302 -8.9; 332 -8.4; 365 -8.0; 402 -7.8; 442 -7.7; 486 -7.5; 535 -7.2; 588 -7.0; 647 -6.9; 712 -7.1; 783 -7.5; 861 -7.6; 947 -7.2; 1042 -7.7; 1146 -8.0; 1261 -7.9; 1387 -7.4; 1526 -6.3; 1678 -5.3; 1846 -4.3; 2031 -3.2; 2234 -3.1; 2457 -3.8; 2703 -4.7; 2973 -5.4; 3270 -5.8; 3597 -5.9; 3957 -5.4; 4353 -3.8; 4788 -3.9; 5267 -8.4; 5793 -7.7; 6373 -2.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 660 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 660 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.38 | 6.4 dB  |
| Peaking | 199 Hz   | 0.63 | -3.3 dB |
| Peaking | 2220 Hz  | 2.77 | 3.8 dB  |
| Peaking | 6600 Hz  | 8.76 | 5.1 dB  |
| Peaking | 22050 Hz | 2.27 | 0.9 dB  |
| Peaking | 84 Hz    | 7.39 | 0.9 dB  |
| Peaking | 1224 Hz  | 2.47 | -1.7 dB |
| Peaking | 1774 Hz  | 4.21 | 0.9 dB  |
| Peaking | 4572 Hz  | 5.45 | 3.8 dB  |
| Peaking | 5397 Hz  | 7.46 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20660%20S/Sennheiser%20HD%20660%20S.png)