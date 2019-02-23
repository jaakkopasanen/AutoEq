# Phiaton Chord MS530 NC on
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.8; 34 -2.7; 37 -3.3; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.3; 60 -4.4; 66 -4.6; 72 -5.0; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.3; 116 -6.8; 128 -7.0; 141 -7.1; 155 -7.3; 170 -7.5; 187 -7.6; 206 -7.9; 227 -8.1; 249 -8.4; 274 -8.6; 302 -8.8; 332 -9.3; 365 -9.6; 402 -10.0; 442 -10.3; 486 -10.9; 535 -10.6; 588 -11.6; 647 -12.8; 712 -13.3; 783 -12.4; 861 -13.0; 947 -14.2; 1042 -14.4; 1146 -14.5; 1261 -13.6; 1387 -13.8; 1526 -11.2; 1678 -11.6; 1846 -12.0; 2031 -10.0; 2234 -8.5; 2457 -6.7; 2703 -4.9; 2973 -2.7; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 NC on GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 NC on ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  1.04 | 6.2 dB  |
| Peaking | 63 Hz   |  1.79 | 1.3 dB  |
| Peaking | 877 Hz  |  0.34 | -3.3 dB |
| Peaking | 1248 Hz |  0.67 | -5.4 dB |
| Peaking | 3972 Hz |  0.98 | 9.0 dB  |
| Peaking | 1602 Hz | 11.51 | 4.2 dB  |
| Peaking | 1749 Hz |  4.4  | -2.0 dB |
| Peaking | 4307 Hz |  5.64 | -1.3 dB |
| Peaking | 6395 Hz |  2.26 | 4.9 dB  |
| Peaking | 7492 Hz |  1.76 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -7.7 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530%20NC%20on/Phiaton%20Chord%20MS530%20NC%20on.png)