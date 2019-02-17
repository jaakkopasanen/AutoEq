# Sennheiser HD 598 Cs
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.6; 28 -2.8; 31 -2.9; 34 -2.9; 37 -2.9; 41 -2.9; 45 -3.0; 49 -3.0; 54 -3.2; 60 -3.6; 66 -3.9; 72 -4.2; 79 -4.4; 87 -4.9; 96 -5.4; 106 -5.8; 116 -6.3; 128 -6.5; 141 -6.4; 155 -6.3; 170 -6.0; 187 -5.6; 206 -4.8; 227 -4.0; 249 -3.2; 274 -2.8; 302 -2.7; 332 -3.3; 365 -4.0; 402 -5.0; 442 -6.0; 486 -6.9; 535 -6.9; 588 -6.8; 647 -6.7; 712 -6.8; 783 -6.8; 861 -6.7; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.2; 1387 -6.2; 1526 -6.4; 1678 -6.5; 1846 -6.6; 2031 -6.7; 2234 -5.9; 2457 -4.5; 2703 -3.6; 2973 -4.1; 3270 -5.8; 3597 -6.9; 3957 -4.9; 4353 -3.9; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -10.7; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 Cs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 Cs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.83 | 4.0 dB  |
| Peaking | 53 Hz   |  1.37 | 2.5 dB  |
| Peaking | 286 Hz  |  2.36 | 4.1 dB  |
| Peaking | 2723 Hz |  5.4  | 2.8 dB  |
| Peaking | 5556 Hz |  2.78 | 6.8 dB  |
| Peaking | 131 Hz  |  4.17 | -0.8 dB |
| Peaking | 533 Hz  |  3.59 | -1.0 dB |
| Peaking | 3507 Hz | 12.51 | -1.9 dB |
| Peaking | 6605 Hz |  7.87 | 1.6 dB  |
| Peaking | 8852 Hz |  3.36 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598%20Cs/Sennheiser%20HD%20598%20Cs.png)