# Phiaton PS 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.1; 28 -3.2; 31 -3.3; 34 -3.4; 37 -3.4; 41 -3.6; 45 -3.8; 49 -3.9; 54 -4.1; 60 -4.4; 66 -4.7; 72 -5.1; 79 -5.4; 87 -5.9; 96 -6.3; 106 -6.6; 116 -6.8; 128 -7.2; 141 -7.5; 155 -7.7; 170 -7.8; 187 -7.9; 206 -8.1; 227 -7.9; 249 -8.0; 274 -7.9; 302 -7.8; 332 -7.7; 365 -7.5; 402 -7.4; 442 -7.1; 486 -7.0; 535 -6.9; 588 -6.4; 647 -6.3; 712 -6.2; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.8; 1146 -7.0; 1261 -7.4; 1387 -7.9; 1526 -8.5; 1678 -8.8; 1846 -8.7; 2031 -8.5; 2234 -7.9; 2457 -6.2; 2703 -4.1; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -4.3; 4788 -6.2; 5267 -7.0; 5793 -7.6; 6373 -7.3; 7010 -6.2; 7711 -6.2; 8482 -6.6; 9330 -8.7; 10263 -11.1; 11289 -8.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.3  | 3.5 dB  |
| Peaking | 50 Hz    |  2.1  | 2.1 dB  |
| Peaking | 1903 Hz  |  1.58 | -3.3 dB |
| Peaking | 3330 Hz  |  2.47 | 7.7 dB  |
| Peaking | 10246 Hz |  4.74 | -5.1 dB |
| Peaking | 76 Hz    |  1.7  | 0.9 dB  |
| Peaking | 219 Hz   |  0.65 | -1.7 dB |
| Peaking | 753 Hz   |  1.98 | 1.1 dB  |
| Peaking | 3972 Hz  | 10.54 | 2.3 dB  |
| Peaking | 5452 Hz  |  3.55 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)