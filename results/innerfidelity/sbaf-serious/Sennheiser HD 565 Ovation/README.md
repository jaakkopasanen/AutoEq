# Sennheiser HD 565 Ovation
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.2; 72 -1.6; 79 -2.4; 87 -3.2; 96 -4.2; 106 -4.7; 116 -5.2; 128 -5.8; 141 -6.3; 155 -6.6; 170 -6.8; 187 -7.1; 206 -7.3; 227 -7.3; 249 -7.5; 274 -7.5; 302 -7.5; 332 -7.5; 365 -7.4; 402 -7.4; 442 -7.2; 486 -7.4; 535 -7.4; 588 -7.2; 647 -7.3; 712 -7.5; 783 -7.4; 861 -7.8; 947 -7.9; 1042 -7.9; 1146 -8.5; 1261 -8.9; 1387 -9.2; 1526 -9.4; 1678 -9.7; 1846 -9.3; 2031 -9.2; 2234 -9.6; 2457 -9.0; 2703 -8.1; 2973 -6.7; 3270 -6.4; 3597 -7.2; 3957 -8.0; 4353 -8.2; 4788 -5.6; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 565 Ovation GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 565 Ovation ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.3  | 7.6 dB  |
| Peaking | 149 Hz  | 0.52 | -4.4 dB |
| Peaking | 1717 Hz | 1.04 | -3.2 dB |
| Peaking | 4298 Hz | 5.77 | -3.1 dB |
| Peaking | 5811 Hz | 3.05 | 7.1 dB  |
| Peaking | 59 Hz   | 0.99 | -1.1 dB |
| Peaking | 64 Hz   | 1.85 | 1.5 dB  |
| Peaking | 2368 Hz | 7.05 | -1.0 dB |
| Peaking | 3114 Hz | 6.61 | 1.3 dB  |
| Peaking | 8071 Hz | 5.14 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20565%20Ovation/Sennheiser%20HD%20565%20Ovation.png)