# AudioFly AF160
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.8; 28 -4.0; 31 -4.1; 34 -4.3; 37 -4.4; 41 -4.6; 45 -4.8; 49 -5.0; 54 -5.3; 60 -5.5; 66 -5.8; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.4; 106 -7.7; 116 -7.9; 128 -8.3; 141 -8.6; 155 -8.9; 170 -9.0; 187 -9.1; 206 -9.2; 227 -9.2; 249 -9.2; 274 -9.2; 302 -9.1; 332 -9.0; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.5; 535 -8.3; 588 -7.8; 647 -7.7; 712 -7.6; 783 -7.5; 861 -7.8; 947 -8.1; 1042 -8.5; 1146 -8.8; 1261 -9.1; 1387 -9.6; 1526 -10.1; 1678 -10.3; 1846 -10.0; 2031 -9.5; 2234 -8.9; 2457 -7.5; 2703 -6.6; 2973 -5.2; 3270 -4.5; 3597 -5.0; 3957 -4.5; 4353 -2.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioFly AF160 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.44 | 3.0 dB  |
| Peaking | 57 Hz   | 1.08 | 0.7 dB  |
| Peaking | 221 Hz  | 0.49 | -2.9 dB |
| Peaking | 1665 Hz | 1.56 | -4.0 dB |
| Peaking | 5252 Hz | 1.86 | 6.8 dB  |
| Peaking | 2210 Hz | 6.94 | -0.7 dB |
| Peaking | 3110 Hz | 5.52 | 1.6 dB  |
| Peaking | 6454 Hz | 4.65 | 3.7 dB  |
| Peaking | 7209 Hz | 1.68 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF160/AudioFly%20AF160.png)