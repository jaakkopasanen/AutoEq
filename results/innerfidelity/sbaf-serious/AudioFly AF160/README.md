# AudioFly AF160
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -1.9; 25 -2.1; 28 -2.2; 31 -2.4; 34 -2.5; 37 -2.6; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.5; 60 -3.8; 66 -4.1; 72 -4.4; 79 -4.8; 87 -5.2; 96 -5.6; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.8; 155 -7.1; 170 -7.3; 187 -7.3; 206 -7.4; 227 -7.4; 249 -7.5; 274 -7.4; 302 -7.3; 332 -7.2; 365 -7.2; 402 -7.0; 442 -6.7; 486 -6.7; 535 -6.5; 588 -6.0; 647 -5.9; 712 -5.8; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.3; 1387 -7.8; 1526 -8.3; 1678 -8.5; 1846 -8.2; 2031 -7.8; 2234 -7.1; 2457 -5.8; 2703 -4.8; 2973 -3.4; 3270 -2.7; 3597 -3.3; 3957 -2.7; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioFly AF160 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.65 | 4.3 dB  |
| Peaking | 52 Hz   | 0.88 | 1.9 dB  |
| Peaking | 203 Hz  | 1.07 | -1.3 dB |
| Peaking | 1716 Hz | 2.53 | -2.8 dB |
| Peaking | 4874 Hz | 1.38 | 6.5 dB  |
| Peaking | 739 Hz  | 1.82 | 1.3 dB  |
| Peaking | 2017 Hz | 0.16 | -0.4 dB |
| Peaking | 3070 Hz | 4.7  | 2.1 dB  |
| Peaking | 6342 Hz | 3.62 | 4.2 dB  |
| Peaking | 7251 Hz | 1.65 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF160/AudioFly%20AF160.png)