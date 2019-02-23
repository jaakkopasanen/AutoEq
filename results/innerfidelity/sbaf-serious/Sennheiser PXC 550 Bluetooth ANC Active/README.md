# Sennheiser PXC 550 Bluetooth ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -4.5; 25 -5.4; 28 -5.9; 31 -6.0; 34 -5.9; 37 -5.7; 41 -5.5; 45 -5.2; 49 -5.0; 54 -4.8; 60 -4.6; 66 -4.5; 72 -4.4; 79 -4.5; 87 -4.7; 96 -5.0; 106 -5.5; 116 -5.7; 128 -6.1; 141 -6.4; 155 -6.5; 170 -6.3; 187 -6.3; 206 -6.0; 227 -5.8; 249 -5.5; 274 -5.0; 302 -4.7; 332 -4.5; 365 -4.5; 402 -4.7; 442 -4.8; 486 -5.2; 535 -5.5; 588 -5.4; 647 -5.6; 712 -6.0; 783 -6.1; 861 -6.9; 947 -7.7; 1042 -8.3; 1146 -8.8; 1261 -7.9; 1387 -9.6; 1526 -10.1; 1678 -10.6; 1846 -8.8; 2031 -8.9; 2234 -8.2; 2457 -6.9; 2703 -5.2; 2973 -4.5; 3270 -3.7; 3597 -4.9; 3957 -4.4; 4353 -0.5; 4788 -9.3; 5267 -10.2; 5793 -4.3; 6373 -3.2; 7010 -4.9; 7711 -8.2; 8482 -11.3; 9330 -12.6; 10263 -9.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Bluetooth ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Bluetooth ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.02 | 1.3 dB  |
| Peaking | 1610 Hz |  1.18 | -4.7 dB |
| Peaking | 3320 Hz |  1.97 | 3.6 dB  |
| Peaking | 6516 Hz |  6.7  | 4.4 dB  |
| Peaking | 9077 Hz |  3.41 | -6.8 dB |
| Peaking | 19 Hz   |  2.93 | 2.8 dB  |
| Peaking | 166 Hz  |  2.06 | -1.4 dB |
| Peaking | 363 Hz  |  1.87 | 1.1 dB  |
| Peaking | 4357 Hz | 10.31 | 6.3 dB  |
| Peaking | 5008 Hz |  9.63 | -7.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active.png)