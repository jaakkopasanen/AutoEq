# Phiaton PS 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.9; 25 -5.0; 28 -5.0; 31 -5.1; 34 -5.3; 37 -5.4; 41 -5.5; 45 -5.6; 49 -5.8; 54 -6.0; 60 -6.3; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.5; 96 -7.8; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.8; 155 -8.9; 170 -9.1; 187 -9.2; 206 -9.3; 227 -9.1; 249 -9.1; 274 -9.0; 302 -8.8; 332 -8.5; 365 -8.2; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.1; 588 -6.8; 647 -6.4; 712 -6.2; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.3; 1846 -8.1; 2031 -7.6; 2234 -6.8; 2457 -5.4; 2703 -3.1; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -3.2; 5267 -3.4; 5793 -4.4; 6373 -6.2; 7010 -8.0; 7711 -9.4; 8482 -11.0; 9330 -13.6; 10263 -13.4; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.67 | 1.7 dB  |
| Peaking | 192 Hz   | 0.7  | -2.9 dB |
| Peaking | 2023 Hz  | 1.48 | -4.8 dB |
| Peaking | 3320 Hz  | 1.1  | 7.9 dB  |
| Peaking | 9395 Hz  | 2.51 | -8.4 dB |
| Peaking | 794 Hz   | 2.73 | 0.9 dB  |
| Peaking | 1457 Hz  | 5.07 | -0.6 dB |
| Peaking | 5571 Hz  | 6.98 | 0.9 dB  |
| Peaking | 7116 Hz  | 4.69 | -1.3 dB |
| Peaking | 11937 Hz | 5.58 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)