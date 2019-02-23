# Phiaton PS 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.8; 37 -2.3; 41 -2.9; 45 -3.4; 49 -3.8; 54 -4.4; 60 -5.0; 66 -5.5; 72 -6.1; 79 -6.6; 87 -7.2; 96 -7.8; 106 -8.3; 116 -8.6; 128 -9.0; 141 -9.4; 155 -9.8; 170 -10.0; 187 -10.1; 206 -10.4; 227 -10.5; 249 -10.7; 274 -10.7; 302 -10.8; 332 -10.8; 365 -11.0; 402 -11.1; 442 -10.7; 486 -10.9; 535 -10.5; 588 -9.6; 647 -8.8; 712 -7.7; 783 -6.2; 861 -5.1; 947 -4.1; 1042 -3.5; 1146 -3.3; 1261 -3.5; 1387 -4.4; 1526 -5.9; 1678 -7.3; 1846 -8.6; 2031 -9.4; 2234 -9.2; 2457 -6.2; 2703 -3.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.1; 4788 -5.7; 5267 -7.9; 5793 -5.1; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.58 | 6.3 dB  |
| Peaking | 636 Hz   | 0.19 | -5.7 dB |
| Peaking | 1054 Hz  | 1.4  | 8.9 dB  |
| Peaking | 3486 Hz  | 1.79 | 9.3 dB  |
| Peaking | 21175 Hz | 2.3  | 1.6 dB  |
| Peaking | 1405 Hz  | 4.86 | 1.5 dB  |
| Peaking | 2132 Hz  | 3.43 | -3.1 dB |
| Peaking | 2825 Hz  | 6.2  | 2.6 dB  |
| Peaking | 5260 Hz  | 6.8  | -3.6 dB |
| Peaking | 6442 Hz  | 5.76 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%2020/Phiaton%20PS%2020.png)