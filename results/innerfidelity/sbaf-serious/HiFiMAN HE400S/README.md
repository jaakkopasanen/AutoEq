# HiFiMAN HE400S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.2; 45 -1.8; 49 -2.2; 54 -2.6; 60 -3.2; 66 -3.8; 72 -4.3; 79 -4.9; 87 -5.4; 96 -5.9; 106 -6.1; 116 -6.3; 128 -6.7; 141 -6.9; 155 -7.0; 170 -7.1; 187 -7.2; 206 -7.1; 227 -7.1; 249 -7.1; 274 -7.1; 302 -7.3; 332 -7.5; 365 -7.5; 402 -7.7; 442 -7.1; 486 -6.6; 535 -6.5; 588 -6.5; 647 -6.6; 712 -6.9; 783 -7.1; 861 -7.5; 947 -7.8; 1042 -7.8; 1146 -7.2; 1261 -7.3; 1387 -7.8; 1526 -7.6; 1678 -7.3; 1846 -6.7; 2031 -6.2; 2234 -5.7; 2457 -5.1; 2703 -5.1; 2973 -5.5; 3270 -5.2; 3597 -5.3; 3957 -5.5; 4353 -7.8; 4788 -6.4; 5267 -2.1; 5793 -2.6; 6373 -6.1; 7010 -5.2; 7711 -6.2; 8482 -7.4; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE400S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE400S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.41 | 6.8 dB  |
| Peaking | 105 Hz  |  0.44 | -2.1 dB |
| Peaking | 2471 Hz |  0.57 | -3.4 dB |
| Peaking | 2647 Hz |  1.21 | 4.9 dB  |
| Peaking | 5511 Hz |  6.19 | 6.3 dB  |
| Peaking | 385 Hz  |  3.85 | -0.8 dB |
| Peaking | 540 Hz  |  3    | 0.8 dB  |
| Peaking | 3795 Hz |  6.37 | 1.2 dB  |
| Peaking | 4465 Hz | 10.2  | -2.3 dB |
| Peaking | 7145 Hz | 11.81 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE400S/HiFiMAN%20HE400S.png)