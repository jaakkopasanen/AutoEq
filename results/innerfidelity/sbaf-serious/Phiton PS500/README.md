# Phiton PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.9; 34 -2.8; 37 -3.6; 41 -4.3; 45 -4.8; 49 -5.3; 54 -5.6; 60 -6.1; 66 -6.5; 72 -6.7; 79 -7.5; 87 -8.0; 96 -8.6; 106 -8.9; 116 -9.2; 128 -9.7; 141 -9.8; 155 -9.7; 170 -9.4; 187 -9.4; 206 -9.0; 227 -8.4; 249 -7.7; 274 -6.4; 302 -5.0; 332 -4.1; 365 -3.7; 402 -3.7; 442 -3.7; 486 -4.0; 535 -4.0; 588 -3.9; 647 -4.3; 712 -5.0; 783 -5.2; 861 -4.9; 947 -5.9; 1042 -6.8; 1146 -7.4; 1261 -7.9; 1387 -8.6; 1526 -8.9; 1678 -9.1; 1846 -8.7; 2031 -7.3; 2234 -5.2; 2457 -2.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiton PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiton PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 17 Hz   |  0.26 | 7.2 dB  |
| Peaking | 507 Hz  |  0.49 | 12.4 dB |
| Peaking | 638 Hz  |  0.09 | -9.4 dB |
| Peaking | 2926 Hz |  1.65 | 10.1 dB |
| Peaking | 5257 Hz |  1.2  | 9.5 dB  |
| Peaking | 191 Hz  |  3.48 | -0.7 dB |
| Peaking | 917 Hz  |  5.24 | 1.2 dB  |
| Peaking | 1775 Hz |  3.52 | -1.1 dB |
| Peaking | 2507 Hz | 10.03 | 1.6 dB  |
| Peaking | 7824 Hz |  8.5  | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiton%20PS500/Phiton%20PS500.png)