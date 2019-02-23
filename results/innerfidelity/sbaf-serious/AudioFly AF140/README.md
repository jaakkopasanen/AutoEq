# AudioFly AF140
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.4; 28 -8.7; 31 -8.9; 34 -9.1; 37 -9.3; 41 -9.5; 45 -9.8; 49 -9.9; 54 -10.2; 60 -10.5; 66 -10.7; 72 -11.1; 79 -11.4; 87 -11.7; 96 -12.0; 106 -12.2; 116 -12.3; 128 -12.5; 141 -12.5; 155 -12.6; 170 -12.4; 187 -12.3; 206 -12.1; 227 -11.7; 249 -11.4; 274 -10.9; 302 -10.4; 332 -9.8; 365 -9.2; 402 -8.6; 442 -7.7; 486 -7.5; 535 -6.7; 588 -5.7; 647 -5.0; 712 -3.8; 783 -3.1; 861 -3.3; 947 -3.8; 1042 -4.8; 1146 -5.6; 1261 -6.4; 1387 -7.6; 1526 -8.6; 1678 -9.4; 1846 -9.9; 2031 -9.8; 2234 -9.7; 2457 -8.6; 2703 -6.7; 2973 -3.6; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -4.9; 5793 -3.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.3; 11289 -6.8; 12418 -6.5; 13660 -6.7; 15026 -8.7; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioFly AF140 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF140 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 116 Hz   | 0.35 | -4.5 dB |
| Peaking | 505 Hz   | 0.21 | -2.6 dB |
| Peaking | 826 Hz   | 0.88 | 7.2 dB  |
| Peaking | 2226 Hz  | 0.95 | -7.8 dB |
| Peaking | 3601 Hz  | 1.13 | 10.7 dB |
| Peaking | 23 Hz    | 1.73 | -0.5 dB |
| Peaking | 5545 Hz  | 7.6  | -5.9 dB |
| Peaking | 6179 Hz  | 2.52 | 6.6 dB  |
| Peaking | 7453 Hz  | 1.48 | -3.3 dB |
| Peaking | 15028 Hz | 4.23 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF140/AudioFly%20AF140.png)