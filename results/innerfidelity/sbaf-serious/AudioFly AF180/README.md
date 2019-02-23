# AudioFly AF180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.8; 28 -6.1; 31 -6.2; 34 -6.4; 37 -6.6; 41 -6.8; 45 -7.0; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.6; 79 -8.9; 87 -9.4; 96 -9.9; 106 -10.2; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.2; 170 -11.4; 187 -11.3; 206 -11.5; 227 -11.3; 249 -11.4; 274 -11.2; 302 -11.1; 332 -10.9; 365 -10.7; 402 -10.5; 442 -10.1; 486 -9.9; 535 -9.6; 588 -9.0; 647 -8.7; 712 -8.5; 783 -8.1; 861 -8.1; 947 -8.3; 1042 -8.4; 1146 -8.4; 1261 -8.3; 1387 -8.5; 1526 -8.5; 1678 -8.2; 1846 -7.6; 2031 -6.5; 2234 -5.6; 2457 -4.1; 2703 -3.1; 2973 -1.9; 3270 -1.3; 3597 -1.9; 3957 -2.5; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.8; 10263 -11.7; 11289 -8.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioFly AF180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 216 Hz   | 0.44 | -5.0 dB |
| Peaking | 1590 Hz  | 1.34 | -2.3 dB |
| Peaking | 3095 Hz  | 1.59 | 4.6 dB  |
| Peaking | 5452 Hz  | 1.85 | 5.9 dB  |
| Peaking | 10294 Hz | 4.28 | -6.1 dB |
| Peaking | 21 Hz    | 1.11 | 1.3 dB  |
| Peaking | 6532 Hz  | 8.61 | 1.5 dB  |
| Peaking | 7582 Hz  | 6.31 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF180/AudioFly%20AF180.png)