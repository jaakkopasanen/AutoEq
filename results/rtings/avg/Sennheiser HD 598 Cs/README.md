# Sennheiser HD 598 Cs
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.7; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.3; 37 -4.3; 41 -4.3; 45 -4.3; 49 -4.4; 54 -4.6; 60 -4.9; 66 -5.3; 72 -5.5; 79 -5.8; 87 -6.3; 96 -6.7; 106 -7.2; 116 -7.6; 128 -7.8; 141 -7.7; 155 -7.6; 170 -7.3; 187 -6.9; 206 -6.2; 227 -5.3; 249 -4.6; 274 -4.1; 302 -4.1; 332 -4.6; 365 -5.4; 402 -6.4; 442 -7.4; 486 -8.2; 535 -8.3; 588 -8.1; 647 -8.0; 712 -8.1; 783 -8.2; 861 -8.0; 947 -7.9; 1042 -7.8; 1146 -7.6; 1261 -7.5; 1387 -7.6; 1526 -7.7; 1678 -7.8; 1846 -8.0; 2031 -8.0; 2234 -7.2; 2457 -5.9; 2703 -5.0; 2973 -5.4; 3270 -7.2; 3597 -8.2; 3957 -6.2; 4353 -5.2; 4788 -3.3; 5267 -1.2; 5793 -0.5; 6373 -2.8; 7010 -4.1; 7711 -6.2; 8482 -8.2; 9330 -8.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -8.8; 18182 -12.1; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 Cs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 Cs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.4  | 3.4 dB  |
| Peaking | 252 Hz   | 0.28 | -4.3 dB |
| Peaking | 289 Hz   | 1.27 | 6.4 dB  |
| Peaking | 5642 Hz  | 3.48 | 6.8 dB  |
| Peaking | 19717 Hz | 0.9  | -9.4 dB |
| Peaking | 2074 Hz  | 2.34 | -2.8 dB |
| Peaking | 2738 Hz  | 1.45 | 3.3 dB  |
| Peaking | 3489 Hz  | 4.39 | -4.0 dB |
| Peaking | 8963 Hz  | 4.96 | -3.7 dB |
| Peaking | 11303 Hz | 0.77 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598%20Cs/Sennheiser%20HD%20598%20Cs.png)