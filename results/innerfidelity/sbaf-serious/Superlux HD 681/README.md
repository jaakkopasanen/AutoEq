# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.7; 31 -2.7; 34 -3.5; 37 -4.2; 41 -4.9; 45 -5.5; 49 -5.9; 54 -6.4; 60 -6.8; 66 -6.8; 72 -6.7; 79 -7.0; 87 -7.0; 96 -6.9; 106 -7.4; 116 -7.8; 128 -8.2; 141 -8.4; 155 -8.5; 170 -8.2; 187 -7.6; 206 -7.1; 227 -7.7; 249 -7.8; 274 -7.6; 302 -7.4; 332 -7.2; 365 -7.0; 402 -6.9; 442 -6.7; 486 -6.8; 535 -6.8; 588 -6.5; 647 -5.5; 712 -6.1; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -7.2; 1261 -8.0; 1387 -9.0; 1526 -10.1; 1678 -10.6; 1846 -11.5; 2031 -12.2; 2234 -12.8; 2457 -12.3; 2703 -11.5; 2973 -10.6; 3270 -9.5; 3597 -8.0; 3957 -6.8; 4353 -8.9; 4788 -11.1; 5267 -11.0; 5793 -11.0; 6373 -9.1; 7010 -8.4; 7711 -13.7; 8482 -16.7; 9330 -16.3; 10263 -14.0; 11289 -8.0; 12418 -6.5; 13660 -7.5; 15026 -9.5; 16529 -6.6; 18182 -6.5; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.4  | 6.3 dB   |
| Peaking | 150 Hz   | 1.03 | -1.9 dB  |
| Peaking | 2225 Hz  | 1.44 | -6.2 dB  |
| Peaking | 8886 Hz  | 2.22 | -10.8 dB |
| Peaking | 19978 Hz | 2.44 | -2.9 dB  |
| Peaking | 790 Hz   | 2.15 | 1.2 dB   |
| Peaking | 3910 Hz  | 4.83 | 3.7 dB   |
| Peaking | 4863 Hz  | 1.86 | -2.9 dB  |
| Peaking | 5780 Hz  | 2.94 | -1.0 dB  |
| Peaking | 6755 Hz  | 7.32 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)