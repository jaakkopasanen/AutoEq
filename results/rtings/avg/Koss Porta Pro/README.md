# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -1.8; 37 -2.6; 41 -3.6; 45 -4.5; 49 -5.2; 54 -6.0; 60 -6.8; 66 -7.5; 72 -8.0; 79 -8.5; 87 -9.1; 96 -9.5; 106 -9.9; 116 -10.2; 128 -10.4; 141 -10.5; 155 -10.4; 170 -10.3; 187 -10.0; 206 -9.6; 227 -9.2; 249 -8.9; 274 -8.6; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.5; 442 -7.3; 486 -7.1; 535 -6.7; 588 -6.4; 647 -6.1; 712 -5.7; 783 -5.3; 861 -4.9; 947 -4.8; 1042 -4.9; 1146 -5.2; 1261 -5.7; 1387 -6.3; 1526 -7.1; 1678 -7.8; 1846 -8.6; 2031 -9.2; 2234 -9.2; 2457 -8.1; 2703 -6.4; 2973 -5.8; 3270 -5.9; 3597 -5.3; 3957 -1.1; 4353 -0.5; 4788 -3.9; 5267 -8.9; 5793 -4.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.66 | 7.0 dB  |
| Peaking | 126 Hz  |  0.44 | -4.6 dB |
| Peaking | 1922 Hz |  0.37 | 3.7 dB  |
| Peaking | 2058 Hz |  1.35 | -6.4 dB |
| Peaking | 4216 Hz |  6.49 | 5.5 dB  |
| Peaking | 4593 Hz | 10.42 | 3.4 dB  |
| Peaking | 5265 Hz |  4.66 | -6.4 dB |
| Peaking | 6250 Hz |  3.87 | 6.5 dB  |
| Peaking | 7608 Hz |  3.96 | -1.2 dB |
| Peaking | 9166 Hz |  1.15 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)