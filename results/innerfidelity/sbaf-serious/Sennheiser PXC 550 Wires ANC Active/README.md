# Sennheiser PXC 550 Wires ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.2; 28 -2.2; 31 -3.0; 34 -3.5; 37 -3.8; 41 -4.1; 45 -4.1; 49 -3.9; 54 -3.8; 60 -3.7; 66 -3.5; 72 -3.5; 79 -3.5; 87 -3.7; 96 -3.9; 106 -4.2; 116 -4.6; 128 -5.1; 141 -5.4; 155 -5.7; 170 -5.5; 187 -5.6; 206 -5.5; 227 -5.2; 249 -4.9; 274 -4.4; 302 -3.9; 332 -3.5; 365 -3.3; 402 -3.3; 442 -3.3; 486 -3.7; 535 -4.0; 588 -3.9; 647 -4.2; 712 -4.6; 783 -4.7; 861 -5.4; 947 -6.1; 1042 -6.7; 1146 -7.0; 1261 -5.9; 1387 -7.7; 1526 -8.3; 1678 -8.6; 1846 -6.9; 2031 -7.2; 2234 -6.7; 2457 -5.4; 2703 -3.7; 2973 -3.0; 3270 -2.6; 3597 -4.3; 3957 -3.4; 4353 -0.7; 4788 -9.5; 5267 -8.9; 5793 -2.9; 6373 -2.0; 7010 -4.7; 7711 -7.2; 8482 -9.9; 9330 -10.9; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wires ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wires ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 426 Hz  |  1.23 | 3.3 dB  |
| Peaking | 3318 Hz |  2.76 | 4.1 dB  |
| Peaking | 6329 Hz |  6.55 | 5.4 dB  |
| Peaking | 9023 Hz |  4.16 | -5.1 dB |
| Peaking | 21 Hz   |  1.19 | 5.9 dB  |
| Peaking | 76 Hz   |  1.03 | 2.7 dB  |
| Peaking | 1625 Hz |  3.64 | -2.6 dB |
| Peaking | 4318 Hz |  9.24 | 5.9 dB  |
| Peaking | 4979 Hz | 10.02 | -7.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wires%20ANC%20Active/Sennheiser%20PXC%20550%20Wires%20ANC%20Active.png)