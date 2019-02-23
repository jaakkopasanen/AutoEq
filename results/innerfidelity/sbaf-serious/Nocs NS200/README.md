# Nocs NS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.6; 25 -12.3; 28 -12.0; 31 -11.7; 34 -11.5; 37 -11.2; 41 -11.0; 45 -10.7; 49 -10.6; 54 -10.4; 60 -10.3; 66 -10.2; 72 -10.2; 79 -10.3; 87 -10.3; 96 -10.4; 106 -10.4; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.2; 170 -10.1; 187 -9.9; 206 -9.7; 227 -9.4; 249 -9.1; 274 -8.7; 302 -8.3; 332 -7.8; 365 -7.4; 402 -6.9; 442 -6.3; 486 -5.9; 535 -5.5; 588 -4.7; 647 -4.3; 712 -4.1; 783 -3.8; 861 -3.9; 947 -4.1; 1042 -4.4; 1146 -4.8; 1261 -5.2; 1387 -5.9; 1526 -6.4; 1678 -7.1; 1846 -7.3; 2031 -7.6; 2234 -8.0; 2457 -7.7; 2703 -7.1; 2973 -4.7; 3270 -2.1; 3597 -0.5; 3957 -1.0; 4353 -3.3; 4788 -5.0; 5267 -6.4; 5793 -9.6; 6373 -8.6; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.48 | -6.1 dB |
| Peaking | 154 Hz  | 0.43 | -3.6 dB |
| Peaking | 833 Hz  | 0.73 | 4.0 dB  |
| Peaking | 3021 Hz | 0.64 | -4.9 dB |
| Peaking | 3654 Hz | 2.2  | 10.9 dB |
| Peaking | 5108 Hz | 3.46 | 1.2 dB  |
| Peaking | 6047 Hz | 4.44 | -5.0 dB |
| Peaking | 6924 Hz | 2.82 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)