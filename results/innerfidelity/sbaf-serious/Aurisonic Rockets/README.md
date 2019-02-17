# Aurisonic Rockets
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.8; 25 -4.9; 28 -5.0; 31 -5.1; 34 -5.3; 37 -5.4; 41 -5.6; 45 -5.7; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.0; 79 -7.4; 87 -7.8; 96 -8.3; 106 -8.5; 116 -8.7; 128 -9.0; 141 -9.3; 155 -9.5; 170 -9.5; 187 -9.7; 206 -9.7; 227 -9.5; 249 -9.6; 274 -9.4; 302 -9.3; 332 -9.0; 365 -8.8; 402 -8.5; 442 -8.0; 486 -7.8; 535 -7.5; 588 -6.9; 647 -6.6; 712 -6.4; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.3; 1526 -7.9; 1678 -8.3; 1846 -8.1; 2031 -7.5; 2234 -6.8; 2457 -5.3; 2703 -3.6; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aurisonic Rockets GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurisonic Rockets ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.22 | 2.0 dB  |
| Peaking | 181 Hz  | 0.43 | -3.7 dB |
| Peaking | 731 Hz  | 1.58 | 1.3 dB  |
| Peaking | 1880 Hz | 1.64 | -3.7 dB |
| Peaking | 3989 Hz | 0.96 | 7.3 dB  |
| Peaking | 3052 Hz | 6.7  | 1.7 dB  |
| Peaking | 4122 Hz | 3.31 | -0.8 dB |
| Peaking | 6361 Hz | 2.25 | 4.8 dB  |
| Peaking | 7058 Hz | 0.66 | -1.4 dB |
| Peaking | 7466 Hz | 2.72 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurisonic%20Rockets/Aurisonic%20Rockets.png)