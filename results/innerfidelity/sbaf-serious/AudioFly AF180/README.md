# AudioFly AF180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.9; 25 -4.1; 28 -4.3; 31 -4.5; 34 -4.7; 37 -4.9; 41 -5.1; 45 -5.3; 49 -5.6; 54 -5.8; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.2; 87 -7.7; 96 -8.2; 106 -8.5; 116 -8.7; 128 -8.9; 141 -9.2; 155 -9.4; 170 -9.6; 187 -9.5; 206 -9.7; 227 -9.6; 249 -9.6; 274 -9.4; 302 -9.3; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.3; 486 -8.2; 535 -7.8; 588 -7.2; 647 -6.9; 712 -6.7; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.6; 1261 -6.6; 1387 -6.7; 1526 -6.8; 1678 -6.5; 1846 -5.8; 2031 -4.7; 2234 -3.9; 2457 -2.4; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -9.9; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioFly AF180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.81 | 0.6 dB  |
| Peaking | 17 Hz    | 0.25 | 2.5 dB  |
| Peaking | 189 Hz   | 0.45 | -3.5 dB |
| Peaking | 4281 Hz  | 0.84 | 6.9 dB  |
| Peaking | 10096 Hz | 2.56 | -4.2 dB |
| Peaking | 1642 Hz  | 2.62 | -1.6 dB |
| Peaking | 2864 Hz  | 2.55 | 2.0 dB  |
| Peaking | 4366 Hz  | 1.58 | -2.0 dB |
| Peaking | 6603 Hz  | 1.6  | 3.3 dB  |
| Peaking | 7516 Hz  | 3.84 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF180/AudioFly%20AF180.png)