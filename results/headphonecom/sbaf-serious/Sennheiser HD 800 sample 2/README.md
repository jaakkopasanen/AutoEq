# Sennheiser HD 800 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.1; 37 -2.3; 41 -2.6; 45 -2.7; 49 -2.4; 54 -2.2; 60 -3.1; 66 -2.7; 72 -3.5; 79 -4.5; 87 -5.0; 96 -5.4; 106 -5.7; 116 -6.0; 128 -6.2; 141 -6.4; 155 -6.6; 170 -6.6; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.8; 274 -6.7; 302 -6.6; 332 -6.2; 365 -6.0; 402 -5.9; 442 -5.6; 486 -5.4; 535 -5.1; 588 -4.9; 647 -4.4; 712 -4.1; 783 -3.8; 861 -3.7; 947 -2.8; 1042 -2.4; 1146 -1.4; 1261 -1.4; 1387 -1.6; 1526 -2.1; 1678 -1.5; 1846 -1.6; 2031 -1.3; 2234 -2.3; 2457 -1.1; 2703 -0.8; 2973 -2.6; 3270 -2.2; 3597 -2.5; 3957 -5.5; 4353 -5.8; 4788 -5.8; 5267 -7.0; 5793 -9.1; 6373 -12.2; 7010 -7.3; 7711 -7.1; 8482 -9.3; 9330 -12.0; 10263 -8.5; 11289 -2.6; 12418 -2.6; 13660 -3.7; 15026 -6.3; 16529 -6.3; 18182 -7.6; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.22 | 2.1 dB  |
| Peaking | 201 Hz   | 0.35 | -4.7 dB |
| Peaking | 2545 Hz  | 0.49 | 3.0 dB  |
| Peaking | 6647 Hz  | 0.85 | -8.2 dB |
| Peaking | 19186 Hz | 0.77 | -6.0 dB |
| Peaking | 6236 Hz  | 9.03 | -5.5 dB |
| Peaking | 7293 Hz  | 2.73 | 4.0 dB  |
| Peaking | 9589 Hz  | 2.97 | -9.5 dB |
| Peaking | 11218 Hz | 1.67 | 6.3 dB  |
| Peaking | 15115 Hz | 2.47 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | -7.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20sample%202/Sennheiser%20HD%20800%20sample%202.png)