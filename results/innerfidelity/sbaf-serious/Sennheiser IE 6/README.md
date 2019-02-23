# Sennheiser IE 6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.2; 25 -7.5; 28 -7.8; 31 -8.1; 34 -8.4; 37 -8.7; 41 -9.1; 45 -9.3; 49 -9.6; 54 -9.9; 60 -10.2; 66 -10.5; 72 -10.9; 79 -11.2; 87 -11.5; 96 -11.8; 106 -11.9; 116 -12.0; 128 -12.1; 141 -12.1; 155 -12.1; 170 -11.9; 187 -11.7; 206 -11.4; 227 -10.9; 249 -10.6; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.3; 402 -7.7; 442 -6.9; 486 -6.4; 535 -5.8; 588 -4.9; 647 -4.3; 712 -3.9; 783 -3.3; 861 -3.2; 947 -3.2; 1042 -3.4; 1146 -3.4; 1261 -3.6; 1387 -4.0; 1526 -4.1; 1678 -4.5; 1846 -4.5; 2031 -4.5; 2234 -4.6; 2457 -4.5; 2703 -4.7; 2973 -4.0; 3270 -3.3; 3597 -3.4; 3957 -5.8; 4353 -10.8; 4788 -12.7; 5267 -6.1; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 104 Hz  | 0.43 | -5.3 dB |
| Peaking | 260 Hz  | 0.63 | -4.4 dB |
| Peaking | 643 Hz  | 0.27 | 3.7 dB  |
| Peaking | 4674 Hz | 6.14 | -9.8 dB |
| Peaking | 6056 Hz | 4.18 | 6.8 dB  |
| Peaking | 849 Hz  | 2.51 | 0.8 dB  |
| Peaking | 1939 Hz | 0.95 | -0.9 dB |
| Peaking | 3533 Hz | 3.22 | 2.7 dB  |
| Peaking | 4249 Hz | 7.98 | -1.9 dB |
| Peaking | 8283 Hz | 4.17 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%206/Sennheiser%20IE%206.png)