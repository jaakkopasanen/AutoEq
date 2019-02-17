# NAD RP18 Bass Light Version
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -1.1; 274 -2.3; 302 -3.1; 332 -4.2; 365 -4.4; 402 -4.9; 442 -5.5; 486 -6.1; 535 -5.5; 588 -5.6; 647 -6.3; 712 -6.7; 783 -6.6; 861 -7.1; 947 -6.6; 1042 -6.3; 1146 -6.0; 1261 -6.3; 1387 -6.4; 1526 -6.7; 1678 -7.3; 1846 -6.5; 2031 -6.1; 2234 -6.3; 2457 -7.2; 2703 -6.6; 2973 -5.2; 3270 -4.8; 3597 -3.3; 3957 -4.1; 4353 -5.3; 4788 -6.9; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD RP18 Bass Light Version GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD RP18 Bass Light Version ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.13 | 6.1 dB  |
| Peaking | 217 Hz  |  1.33 | 2.7 dB  |
| Peaking | 415 Hz  |  0.52 | -1.8 dB |
| Peaking | 3618 Hz |  5.62 | 3.2 dB  |
| Peaking | 5942 Hz |  3.96 | 6.8 dB  |
| Peaking | 1153 Hz |  8.6  | 0.7 dB  |
| Peaking | 2553 Hz | 14.13 | -1.5 dB |
| Peaking | 4836 Hz |  8.71 | -3.1 dB |
| Peaking | 5326 Hz |  8.05 | 2.5 dB  |
| Peaking | 8243 Hz |  4.74 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 4.9 dB  |
| Peaking | 250 Hz   | 1.41 | 4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NAD%20RP18%20Bass%20Light%20Version/NAD%20RP18%20Bass%20Light%20Version.png)