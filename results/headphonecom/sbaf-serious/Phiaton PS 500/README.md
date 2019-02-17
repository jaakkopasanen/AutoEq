# Phiaton PS 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.4; 34 -2.3; 37 -2.7; 41 -2.9; 45 -3.9; 49 -4.9; 54 -4.7; 60 -4.4; 66 -5.6; 72 -6.8; 79 -7.6; 87 -8.2; 96 -8.7; 106 -9.0; 116 -9.4; 128 -9.6; 141 -9.9; 155 -9.9; 170 -9.7; 187 -9.9; 206 -9.5; 227 -9.3; 249 -8.5; 274 -7.3; 302 -5.6; 332 -4.4; 365 -3.7; 402 -3.6; 442 -3.9; 486 -4.2; 535 -4.4; 588 -4.4; 647 -4.7; 712 -5.1; 783 -5.6; 861 -4.9; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -7.2; 1387 -7.1; 1526 -7.0; 1678 -7.7; 1846 -8.6; 2031 -7.5; 2234 -5.2; 2457 -1.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -1.6; 6373 -3.6; 7010 -4.3; 7711 -6.2; 8482 -7.3; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.41 | 7.7 dB   |
| Peaking | 526 Hz  | 0.46 | 12.5 dB  |
| Peaking | 544 Hz  | 0.1  | -10.0 dB |
| Peaking | 2973 Hz | 1.39 | 10.5 dB  |
| Peaking | 5120 Hz | 1.52 | 7.8 dB   |
| Peaking | 230 Hz  | 1.09 | -4.1 dB  |
| Peaking | 402 Hz  | 0.62 | 6.4 dB   |
| Peaking | 533 Hz  | 1.16 | -5.7 dB  |
| Peaking | 1924 Hz | 7.11 | -2.3 dB  |
| Peaking | 4577 Hz | 4.99 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20500/Phiaton%20PS%20500.png)