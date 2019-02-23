# Phiaton Chord MS530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.6; 25 -5.8; 28 -6.1; 31 -6.4; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.6; 60 -8.0; 66 -8.3; 72 -8.5; 79 -8.8; 87 -8.7; 96 -8.7; 106 -9.4; 116 -9.6; 128 -9.7; 141 -10.0; 155 -10.0; 170 -9.4; 187 -9.5; 206 -8.9; 227 -8.5; 249 -8.0; 274 -7.5; 302 -7.1; 332 -6.9; 365 -6.8; 402 -7.2; 442 -7.2; 486 -7.2; 535 -7.6; 588 -7.8; 647 -8.4; 712 -9.0; 783 -9.2; 861 -10.0; 947 -10.5; 1042 -11.5; 1146 -12.2; 1261 -12.3; 1387 -12.9; 1526 -10.8; 1678 -12.4; 1846 -12.8; 2031 -11.4; 2234 -10.2; 2457 -8.3; 2703 -6.9; 2973 -5.1; 3270 -3.6; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 1.46 | -1.4 dB |
| Peaking | 149 Hz  | 1.27 | -3.3 dB |
| Peaking | 1184 Hz | 1.29 | -5.4 dB |
| Peaking | 1955 Hz | 2.24 | -5.0 dB |
| Peaking | 4573 Hz | 1.29 | 7.3 dB  |
| Peaking | 19 Hz   | 1.71 | 1.2 dB  |
| Peaking | 3756 Hz | 3.97 | 1.5 dB  |
| Peaking | 4472 Hz | 2.35 | -1.2 dB |
| Peaking | 6307 Hz | 3.04 | 4.5 dB  |
| Peaking | 7390 Hz | 1.63 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530/Phiaton%20Chord%20MS530.png)