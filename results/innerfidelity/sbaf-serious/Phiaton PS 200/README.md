# Phiaton PS 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.8; 25 -2.9; 28 -3.0; 31 -3.1; 34 -3.1; 37 -3.2; 41 -3.4; 45 -3.6; 49 -3.7; 54 -3.9; 60 -4.2; 66 -4.5; 72 -4.8; 79 -5.2; 87 -5.6; 96 -6.1; 106 -6.4; 116 -6.6; 128 -7.0; 141 -7.3; 155 -7.4; 170 -7.5; 187 -7.7; 206 -7.9; 227 -7.7; 249 -7.8; 274 -7.7; 302 -7.6; 332 -7.5; 365 -7.3; 402 -7.2; 442 -6.9; 486 -6.8; 535 -6.6; 588 -6.1; 647 -6.0; 712 -6.0; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.7; 1526 -8.3; 1678 -8.6; 1846 -8.5; 2031 -8.3; 2234 -7.7; 2457 -5.9; 2703 -3.8; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -4.1; 4788 -6.0; 5267 -6.8; 5793 -7.3; 6373 -7.0; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -10.9; 11289 -7.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.18 | 3.7 dB  |
| Peaking | 51 Hz    |  1.95 | 2.1 dB  |
| Peaking | 1909 Hz  |  1.81 | -3.1 dB |
| Peaking | 3336 Hz  |  2.37 | 7.5 dB  |
| Peaking | 10249 Hz |  4.93 | -4.9 dB |
| Peaking | 78 Hz    |  1.96 | 0.9 dB  |
| Peaking | 220 Hz   |  0.71 | -1.4 dB |
| Peaking | 747 Hz   |  2.05 | 1.2 dB  |
| Peaking | 3973 Hz  | 10.67 | 2.1 dB  |
| Peaking | 5431 Hz  |  3.67 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)