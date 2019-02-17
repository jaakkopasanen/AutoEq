# Bose QuietComfort 35 Wired Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.3; 25 -7.3; 28 -7.4; 31 -7.6; 34 -7.9; 37 -8.0; 41 -8.2; 45 -8.3; 49 -8.3; 54 -8.2; 60 -8.0; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.9; 96 -8.1; 106 -8.0; 116 -7.8; 128 -7.7; 141 -7.7; 155 -7.6; 170 -7.2; 187 -7.3; 206 -7.2; 227 -6.9; 249 -6.8; 274 -6.5; 302 -6.2; 332 -6.1; 365 -5.8; 402 -5.6; 442 -5.4; 486 -5.5; 535 -5.5; 588 -5.3; 647 -5.4; 712 -5.6; 783 -5.6; 861 -5.9; 947 -6.1; 1042 -6.0; 1146 -5.5; 1261 -5.2; 1387 -6.1; 1526 -5.5; 1678 -6.7; 1846 -7.7; 2031 -8.0; 2234 -8.0; 2457 -8.3; 2703 -8.6; 2973 -8.2; 3270 -6.9; 3597 -7.5; 3957 -8.2; 4353 -7.7; 4788 -5.6; 5267 -0.5; 5793 -5.5; 6373 -5.7; 7010 -4.3; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wired Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 44 Hz   |  0.65 | -2.0 dB |
| Peaking | 127 Hz  |  1.17 | -1.3 dB |
| Peaking | 2511 Hz |  2.29 | -2.7 dB |
| Peaking | 4143 Hz |  4.29 | -2.2 dB |
| Peaking | 5316 Hz |  8.61 | 6.6 dB  |
| Peaking | 543 Hz  |  1.73 | 0.8 dB  |
| Peaking | 1443 Hz |  1.73 | 0.9 dB  |
| Peaking | 1874 Hz |  4.89 | -1.4 dB |
| Peaking | 5958 Hz | 12.22 | -2.0 dB |
| Peaking | 6917 Hz |  7.09 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wired%20Active/Bose%20QuietComfort%2035%20Wired%20Active.png)