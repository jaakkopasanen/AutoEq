# Noontec Hammo S Padding Removed
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.4; 28 -3.7; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.3; 45 -4.4; 49 -4.5; 54 -4.7; 60 -4.9; 66 -5.1; 72 -5.2; 79 -5.4; 87 -5.4; 96 -5.5; 106 -5.4; 116 -5.7; 128 -6.3; 141 -6.9; 155 -7.3; 170 -6.6; 187 -7.1; 206 -7.1; 227 -7.0; 249 -6.5; 274 -5.8; 302 -5.3; 332 -4.9; 365 -4.7; 402 -4.4; 442 -4.3; 486 -4.1; 535 -4.1; 588 -4.6; 647 -5.5; 712 -6.1; 783 -5.9; 861 -5.8; 947 -5.9; 1042 -6.8; 1146 -7.4; 1261 -7.9; 1387 -8.4; 1526 -8.6; 1678 -8.5; 1846 -7.9; 2031 -6.7; 2234 -5.4; 2457 -3.6; 2703 -2.2; 2973 -1.5; 3270 -1.9; 3597 -5.8; 3957 -3.3; 4353 -4.9; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo S Padding Removed GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S Padding Removed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.45 | 3.3 dB  |
| Peaking | 479 Hz  | 1.68 | 2.6 dB  |
| Peaking | 1580 Hz | 1.93 | -2.9 dB |
| Peaking | 2850 Hz | 2.84 | 5.2 dB  |
| Peaking | 5594 Hz | 2.64 | 6.6 dB  |
| Peaking | 187 Hz  | 1.09 | -3.6 dB |
| Peaking | 196 Hz  | 0.63 | 2.5 dB  |
| Peaking | 463 Hz  | 4.38 | -0.7 dB |
| Peaking | 6563 Hz | 7.12 | 2.4 dB  |
| Peaking | 7628 Hz | 2.07 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S%20Padding%20Removed/Noontec%20Hammo%20S%20Padding%20Removed.png)