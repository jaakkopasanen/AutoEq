# Sennheiser IE 800 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.9; 34 -1.4; 37 -2.0; 41 -2.6; 45 -3.2; 49 -3.7; 54 -4.3; 60 -4.9; 66 -5.4; 72 -5.9; 79 -6.5; 87 -7.0; 96 -7.6; 106 -8.0; 116 -8.2; 128 -8.7; 141 -9.0; 155 -9.3; 170 -9.4; 187 -9.4; 206 -9.5; 227 -9.3; 249 -9.3; 274 -9.1; 302 -8.9; 332 -8.7; 365 -8.4; 402 -8.1; 442 -7.7; 486 -7.5; 535 -7.2; 588 -6.6; 647 -6.3; 712 -6.2; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.0; 1387 -7.4; 1526 -7.5; 1678 -7.3; 1846 -6.3; 2031 -5.1; 2234 -3.6; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -2.6; 5793 -4.6; 6373 -2.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -10.0; 11289 -11.6; 12418 -11.5; 13660 -9.6; 15026 -8.7; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.59 | 5.7 dB  |
| Peaking | 34 Hz    |  0.77 | 0.8 dB  |
| Peaking | 181 Hz   |  0.58 | -3.3 dB |
| Peaking | 3769 Hz  |  1.07 | 6.9 dB  |
| Peaking | 11827 Hz |  1.67 | -6.0 dB |
| Peaking | 757 Hz   |  1.49 | 1.6 dB  |
| Peaking | 1604 Hz  |  2.24 | -1.7 dB |
| Peaking | 1652 Hz  |  0.33 | -0.9 dB |
| Peaking | 2594 Hz  |  3.6  | 3.1 dB  |
| Peaking | 6655 Hz  | 10.17 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20B/Sennheiser%20IE%20800%20sample%20B.png)