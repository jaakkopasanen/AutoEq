# Ultrasone Edition 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.2; 41 -2.1; 45 -2.8; 49 -3.4; 54 -3.7; 60 -4.0; 66 -4.3; 72 -4.8; 79 -5.2; 87 -5.2; 96 -5.3; 106 -5.8; 116 -6.2; 128 -6.7; 141 -7.1; 155 -7.1; 170 -7.2; 187 -8.3; 206 -8.9; 227 -8.7; 249 -8.5; 274 -8.0; 302 -8.5; 332 -8.4; 365 -8.2; 402 -8.1; 442 -7.9; 486 -8.0; 535 -7.8; 588 -7.3; 647 -7.1; 712 -7.1; 783 -7.1; 861 -7.5; 947 -8.2; 1042 -8.0; 1146 -7.4; 1261 -6.8; 1387 -6.2; 1526 -5.9; 1678 -5.3; 1846 -3.6; 2031 -1.5; 2234 -0.5; 2457 -5.5; 2703 -7.0; 2973 -5.2; 3270 -3.7; 3597 -5.5; 3957 -5.8; 4353 -2.3; 4788 -0.7; 5267 -0.6; 5793 -8.2; 6373 -12.7; 7010 -10.0; 7711 -6.7; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -12.7; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  0.44 | 6.3 dB  |
| Peaking | 914 Hz   |  0.07 | -1.7 dB |
| Peaking | 2088 Hz  |  2.55 | 7.2 dB  |
| Peaking | 4756 Hz  |  4.5  | 8.2 dB  |
| Peaking | 14648 Hz |  3.95 | -7.3 dB |
| Peaking | 215 Hz   |  4.39 | -1.4 dB |
| Peaking | 2606 Hz  | 10.19 | -3.2 dB |
| Peaking | 3256 Hz  |  8.56 | 2.6 dB  |
| Peaking | 6458 Hz  |  4.73 | -9.6 dB |
| Peaking | 6678 Hz  |  1.18 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%208/Ultrasone%20Edition%208.png)