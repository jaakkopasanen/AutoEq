# Sennheiser HD 218
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.8; 25 -1.2; 28 -2.0; 31 -2.6; 34 -3.2; 37 -3.7; 41 -4.4; 45 -5.0; 49 -5.6; 54 -6.2; 60 -6.9; 66 -7.6; 72 -8.3; 79 -8.9; 87 -9.6; 96 -10.3; 106 -10.3; 116 -9.8; 128 -10.5; 141 -11.9; 155 -12.9; 170 -12.7; 187 -12.9; 206 -12.5; 227 -11.8; 249 -10.7; 274 -9.7; 302 -9.6; 332 -9.9; 365 -8.9; 402 -8.3; 442 -7.0; 486 -6.8; 535 -6.9; 588 -5.7; 647 -5.4; 712 -5.6; 783 -5.6; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.2; 1387 -5.8; 1526 -5.4; 1678 -6.0; 1846 -6.1; 2031 -5.3; 2234 -4.4; 2457 -3.6; 2703 -3.0; 2973 -2.4; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -2.6; 4788 -8.0; 5267 -5.6; 5793 -6.0; 6373 -4.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -9.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 218 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  0.82 | 6.0 dB  |
| Peaking | 86 Hz    |  1.79 | -2.4 dB |
| Peaking | 183 Hz   |  1.16 | -6.5 dB |
| Peaking | 3427 Hz  |  1.83 | 6.0 dB  |
| Peaking | 22049 Hz |  2.27 | 0.5 dB  |
| Peaking | 340 Hz   |  5.81 | -1.5 dB |
| Peaking | 661 Hz   |  2.46 | 1.5 dB  |
| Peaking | 4871 Hz  | 12.53 | -4.0 dB |
| Peaking | 6762 Hz  |  9.92 | 2.9 dB  |
| Peaking | 18280 Hz |  2.25 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)