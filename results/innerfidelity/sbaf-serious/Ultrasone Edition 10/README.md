# Ultrasone Edition 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.7; 37 -2.4; 41 -3.2; 45 -3.7; 49 -4.0; 54 -4.5; 60 -5.3; 66 -5.7; 72 -6.2; 79 -6.4; 87 -6.7; 96 -7.1; 106 -7.4; 116 -7.3; 128 -7.4; 141 -7.4; 155 -7.3; 170 -7.0; 187 -6.9; 206 -6.6; 227 -6.3; 249 -6.1; 274 -5.8; 302 -5.7; 332 -5.4; 365 -5.2; 402 -5.0; 442 -4.8; 486 -4.9; 535 -4.9; 588 -4.9; 647 -5.0; 712 -5.1; 783 -5.1; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.4; 1261 -7.8; 1387 -7.5; 1526 -6.5; 1678 -4.9; 1846 -0.7; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -2.3; 3270 -5.8; 3597 -8.6; 3957 -10.6; 4353 -10.1; 4788 -5.0; 5267 -5.6; 5793 -11.6; 6373 -16.4; 7010 -8.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.1; 15026 -14.7; 16529 -12.8; 18182 -7.6; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.23 | 6.7 dB   |
| Peaking | 2401 Hz  | 1.89 | 7.2 dB   |
| Peaking | 3923 Hz  | 5.05 | -6.1 dB  |
| Peaking | 6261 Hz  | 8.16 | -11.1 dB |
| Peaking | 15644 Hz | 2.35 | -9.4 dB  |
| Peaking | 134 Hz   | 1.17 | -1.5 dB  |
| Peaking | 807 Hz   | 0.45 | 2.7 dB   |
| Peaking | 1346 Hz  | 1.11 | -4.7 dB  |
| Peaking | 1870 Hz  | 6.38 | 4.0 dB   |
| Peaking | 9687 Hz  | 1.11 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%2010/Ultrasone%20Edition%2010.png)