# Sennheiser RS 220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.3; 31 -1.9; 34 -2.5; 37 -2.9; 41 -3.4; 45 -3.8; 49 -4.2; 54 -4.6; 60 -5.1; 66 -4.9; 72 -4.9; 79 -5.9; 87 -6.8; 96 -7.4; 106 -7.8; 116 -8.1; 128 -8.4; 141 -8.5; 155 -8.6; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.2; 249 -8.0; 274 -7.9; 302 -7.8; 332 -7.8; 365 -7.5; 402 -7.5; 442 -7.2; 486 -7.2; 535 -6.9; 588 -6.5; 647 -6.4; 712 -6.6; 783 -6.0; 861 -6.5; 947 -6.9; 1042 -6.9; 1146 -7.1; 1261 -7.0; 1387 -5.7; 1526 -2.9; 1678 -2.6; 1846 -2.1; 2031 -5.2; 2234 -9.1; 2457 -11.1; 2703 -9.7; 2973 -7.6; 3270 -6.5; 3597 -5.0; 3957 -2.6; 4353 -0.5; 4788 -0.5; 5267 -2.9; 5793 -5.6; 6373 -3.1; 7010 -7.3; 7711 -8.1; 8482 -8.0; 9330 -9.0; 10263 -9.4; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.25 | 6.2 dB  |
| Peaking | 1807 Hz  | 3.26 | 6.8 dB  |
| Peaking | 2422 Hz  | 2.37 | -6.3 dB |
| Peaking | 4524 Hz  | 2.51 | 7.1 dB  |
| Peaking | 9464 Hz  | 2.36 | -3.2 dB |
| Peaking | 65 Hz    | 1.03 | 3.1 dB  |
| Peaking | 118 Hz   | 0.51 | -3.1 dB |
| Peaking | 1262 Hz  | 3.91 | -1.3 dB |
| Peaking | 1511 Hz  | 8.49 | 2.0 dB  |
| Peaking | 11984 Hz | 6.52 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)