# Sennheiser HD 660 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.1; 41 -1.8; 45 -2.3; 49 -2.8; 54 -3.3; 60 -3.7; 66 -4.3; 72 -4.6; 79 -4.1; 87 -4.6; 96 -5.8; 106 -6.3; 116 -6.8; 128 -7.2; 141 -7.8; 155 -8.2; 170 -8.5; 187 -8.4; 206 -8.6; 227 -8.6; 249 -8.6; 274 -8.4; 302 -8.1; 332 -7.6; 365 -7.2; 402 -6.9; 442 -6.9; 486 -6.7; 535 -6.4; 588 -6.2; 647 -6.1; 712 -6.3; 783 -6.7; 861 -6.8; 947 -6.3; 1042 -6.9; 1146 -7.1; 1261 -7.1; 1387 -6.6; 1526 -5.5; 1678 -4.5; 1846 -3.5; 2031 -2.4; 2234 -2.2; 2457 -3.0; 2703 -3.9; 2973 -4.6; 3270 -5.0; 3597 -5.1; 3957 -4.5; 4353 -3.1; 4788 -2.8; 5267 -7.8; 5793 -6.9; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 660 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 660 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.44 | 6.2 dB  |
| Peaking | 191 Hz   | 0.94 | -2.8 dB |
| Peaking | 2285 Hz  | 1.73 | 4.2 dB  |
| Peaking | 6546 Hz  | 7.61 | 5.0 dB  |
| Peaking | 22050 Hz | 2.27 | 1.1 dB  |
| Peaking | 628 Hz   | 1.97 | 0.9 dB  |
| Peaking | 1661 Hz  | 0.93 | -2.7 dB |
| Peaking | 1841 Hz  | 1.95 | 3.1 dB  |
| Peaking | 4635 Hz  | 4.32 | 4.8 dB  |
| Peaking | 5355 Hz  | 6.53 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20660%20S/Sennheiser%20HD%20660%20S.png)