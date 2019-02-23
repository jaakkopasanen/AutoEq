# Oppo PM1 Velour Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.0; 25 -3.3; 28 -3.7; 31 -3.9; 34 -4.0; 37 -4.0; 41 -4.2; 45 -4.3; 49 -4.1; 54 -4.1; 60 -5.1; 66 -6.0; 72 -6.4; 79 -6.8; 87 -7.2; 96 -7.7; 106 -7.9; 116 -8.1; 128 -8.5; 141 -8.7; 155 -8.9; 170 -9.0; 187 -9.3; 206 -9.2; 227 -9.2; 249 -9.1; 274 -9.3; 302 -9.6; 332 -9.6; 365 -9.1; 402 -7.0; 442 -7.1; 486 -8.1; 535 -8.5; 588 -8.3; 647 -8.5; 712 -8.9; 783 -8.8; 861 -9.3; 947 -7.8; 1042 -6.1; 1146 -6.3; 1261 -6.3; 1387 -6.6; 1526 -6.9; 1678 -6.8; 1846 -6.2; 2031 -5.5; 2234 -4.8; 2457 -4.1; 2703 -3.8; 2973 -3.3; 3270 -3.2; 3597 -3.3; 3957 -2.8; 4353 -2.9; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -8.0; 9330 -9.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 Velour Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 Velour Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.24 | 3.7 dB  |
| Peaking | 177 Hz  | 0.46 | -3.4 dB |
| Peaking | 785 Hz  | 2.99 | -2.3 dB |
| Peaking | 6330 Hz | 0.81 | 8.7 dB  |
| Peaking | 8516 Hz | 1.49 | -8.1 dB |
| Peaking | 408 Hz  | 2.06 | -2.5 dB |
| Peaking | 419 Hz  | 4.83 | 4.1 dB  |
| Peaking | 1682 Hz | 2.27 | -2.3 dB |
| Peaking | 1929 Hz | 0.72 | 1.4 dB  |
| Peaking | 4370 Hz | 4.77 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%20Velour%20Pads/Oppo%20PM1%20Velour%20Pads.png)