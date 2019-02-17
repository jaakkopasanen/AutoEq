# Apple iPod Ear Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -1.3; 170 -2.8; 187 -4.1; 206 -5.3; 227 -6.3; 249 -7.0; 274 -7.5; 302 -7.7; 332 -7.8; 365 -7.6; 402 -7.2; 442 -6.6; 486 -6.4; 535 -6.3; 588 -6.1; 647 -6.4; 712 -6.6; 783 -6.5; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.5; 1387 -6.9; 1526 -7.4; 1678 -7.7; 1846 -7.5; 2031 -6.6; 2234 -5.5; 2457 -6.2; 2703 -9.0; 2973 -11.7; 3270 -10.6; 3597 -7.6; 3957 -6.5; 4353 -7.5; 4788 -7.7; 5267 -6.9; 5793 -9.1; 6373 -12.1; 7010 -10.0; 7711 -8.9; 8482 -9.7; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.2  | 6.6 dB  |
| Peaking | 230 Hz  | 2.9  | -2.4 dB |
| Peaking | 327 Hz  | 1.29 | -4.1 dB |
| Peaking | 3036 Hz | 5.91 | -5.7 dB |
| Peaking | 6649 Hz | 2.78 | -4.9 dB |
| Peaking | 21 Hz   | 2.24 | 0.4 dB  |
| Peaking | 141 Hz  | 6.13 | 1.3 dB  |
| Peaking | 1630 Hz | 4.44 | -1.4 dB |
| Peaking | 6618 Hz | 0.34 | 0.4 dB  |
| Peaking | 8633 Hz | 7.44 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds/Apple%20iPod%20Ear%20Buds.png)