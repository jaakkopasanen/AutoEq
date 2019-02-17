# Sennheiser PXC 550 Bluetooth ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -3.0; 25 -3.8; 28 -4.4; 31 -4.4; 34 -4.3; 37 -4.2; 41 -3.9; 45 -3.7; 49 -3.5; 54 -3.3; 60 -3.0; 66 -2.9; 72 -2.9; 79 -2.9; 87 -3.1; 96 -3.5; 106 -3.9; 116 -4.1; 128 -4.5; 141 -4.8; 155 -5.0; 170 -4.7; 187 -4.7; 206 -4.5; 227 -4.2; 249 -3.9; 274 -3.5; 302 -3.1; 332 -3.0; 365 -2.9; 402 -3.1; 442 -3.2; 486 -3.6; 535 -3.9; 588 -3.8; 647 -4.1; 712 -4.4; 783 -4.5; 861 -5.4; 947 -6.1; 1042 -6.8; 1146 -7.2; 1261 -6.4; 1387 -8.0; 1526 -8.6; 1678 -9.1; 1846 -7.2; 2031 -7.4; 2234 -6.7; 2457 -5.4; 2703 -3.7; 2973 -3.0; 3270 -2.2; 3597 -3.3; 3957 -2.8; 4353 -0.5; 4788 -7.8; 5267 -8.7; 5793 -2.7; 6373 -1.7; 7010 -4.0; 7711 -6.7; 8482 -9.8; 9330 -11.1; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Bluetooth ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Bluetooth ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 41 Hz    |  0.07 | 3.0 dB  |
| Peaking | 3558 Hz  |  2.5  | 4.5 dB  |
| Peaking | 6473 Hz  |  4.86 | 6.1 dB  |
| Peaking | 9430 Hz  |  2.07 | -6.8 dB |
| Peaking | 10735 Hz |  2.55 | 3.8 dB  |
| Peaking | 172 Hz   |  0.92 | -4.6 dB |
| Peaking | 211 Hz   |  0.46 | 3.4 dB  |
| Peaking | 1559 Hz  |  2.26 | -3.1 dB |
| Peaking | 4371 Hz  |  8.51 | 5.1 dB  |
| Peaking | 4990 Hz  | 10.28 | -6.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active.png)