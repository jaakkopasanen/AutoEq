# HiFiMAN HE400S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.0; 54 -1.4; 60 -2.0; 66 -2.6; 72 -3.1; 79 -3.7; 87 -4.2; 96 -4.7; 106 -4.9; 116 -5.1; 128 -5.5; 141 -5.7; 155 -5.8; 170 -5.9; 187 -6.0; 206 -5.9; 227 -5.9; 249 -5.9; 274 -5.9; 302 -6.1; 332 -6.3; 365 -6.3; 402 -6.5; 442 -5.9; 486 -5.4; 535 -5.3; 588 -5.3; 647 -5.4; 712 -5.7; 783 -5.9; 861 -6.3; 947 -6.6; 1042 -6.6; 1146 -6.0; 1261 -6.1; 1387 -6.6; 1526 -6.4; 1678 -6.1; 1846 -5.5; 2031 -5.0; 2234 -4.5; 2457 -3.9; 2703 -3.9; 2973 -4.3; 3270 -4.0; 3597 -4.1; 3957 -4.3; 4353 -6.6; 4788 -5.2; 5267 -0.9; 5793 -1.6; 6373 -4.9; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE400S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE400S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.35 | 6.6 dB  |
| Peaking | 102 Hz  |  0.74 | -1.9 dB |
| Peaking | 574 Hz  |  2.76 | 1.2 dB  |
| Peaking | 2751 Hz |  1.73 | 2.7 dB  |
| Peaking | 5506 Hz |  5.4  | 6.1 dB  |
| Peaking | 1477 Hz |  6.2  | -0.6 dB |
| Peaking | 3785 Hz |  6.15 | 1.2 dB  |
| Peaking | 4444 Hz |  9.64 | -2.3 dB |
| Peaking | 6908 Hz | 12.68 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE400S/HiFiMAN%20HE400S.png)