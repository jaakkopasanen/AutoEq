# HiFiMAN Sundara
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.6; 41 -1.7; 45 -1.7; 49 -1.7; 54 -2.0; 60 -2.4; 66 -3.0; 72 -3.3; 79 -3.5; 87 -3.7; 96 -4.0; 106 -4.3; 116 -4.3; 128 -4.6; 141 -4.8; 155 -4.9; 170 -5.0; 187 -5.1; 206 -5.3; 227 -5.3; 249 -5.5; 274 -5.5; 302 -5.5; 332 -5.7; 365 -5.7; 402 -5.8; 442 -5.5; 486 -4.9; 535 -4.7; 588 -4.8; 647 -5.4; 712 -5.8; 783 -5.5; 861 -5.8; 947 -6.0; 1042 -3.9; 1146 -3.9; 1261 -3.7; 1387 -3.9; 1526 -3.9; 1678 -3.1; 1846 -3.1; 2031 -3.1; 2234 -3.4; 2457 -3.4; 2703 -5.2; 2973 -5.2; 3270 -6.5; 3597 -5.4; 3957 -6.1; 4353 -7.8; 4788 -7.3; 5267 -6.3; 5793 -6.8; 6373 -3.1; 7010 -6.4; 7711 -6.4; 8482 -7.7; 9330 -6.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.8  | 4.4 dB  |
| Peaking | 49 Hz   |  1.05 | 2.4 dB  |
| Peaking | 1864 Hz |  1.7  | 2.4 dB  |
| Peaking | 4531 Hz |  2.95 | -2.6 dB |
| Peaking | 8549 Hz |  5.76 | -2.7 dB |
| Peaking | 328 Hz  |  2.12 | -0.6 dB |
| Peaking | 957 Hz  |  3.43 | -2.3 dB |
| Peaking | 1064 Hz |  4.15 | 2.5 dB  |
| Peaking | 3202 Hz | 10.56 | -1.4 dB |
| Peaking | 6312 Hz | 19.25 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Sundara/HiFiMAN%20Sundara.png)