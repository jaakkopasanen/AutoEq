# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -4.9; 28 -5.0; 31 -5.0; 34 -5.0; 37 -5.1; 41 -5.1; 45 -5.0; 49 -5.0; 54 -5.0; 60 -5.1; 66 -5.2; 72 -5.3; 79 -5.4; 87 -5.4; 96 -5.8; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.9; 155 -7.0; 170 -6.1; 187 -6.6; 206 -6.5; 227 -5.9; 249 -5.3; 274 -4.6; 302 -3.9; 332 -3.5; 365 -3.5; 402 -3.7; 442 -4.1; 486 -4.8; 535 -5.4; 588 -5.5; 647 -5.9; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.0; 1387 -7.6; 1526 -8.2; 1678 -8.7; 1846 -9.6; 2031 -9.3; 2234 -9.6; 2457 -8.6; 2703 -7.8; 2973 -6.7; 3270 -6.0; 3597 -6.0; 3957 -5.8; 4353 -5.5; 4788 -3.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.71 | 1.7 dB  |
| Peaking | 367 Hz  | 1.79 | 3.2 dB  |
| Peaking | 1991 Hz | 2.03 | -3.5 dB |
| Peaking | 5268 Hz | 4.1  | 5.3 dB  |
| Peaking | 6250 Hz | 4.73 | 4.6 dB  |
| Peaking | 83 Hz   | 1.67 | 0.9 dB  |
| Peaking | 131 Hz  | 1.12 | -1.0 dB |
| Peaking | 286 Hz  | 5.24 | 0.7 dB  |
| Peaking | 3276 Hz | 7.43 | 0.9 dB  |
| Peaking | 8133 Hz | 4.63 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3/Oppo%20PM3.png)