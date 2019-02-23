# Sennheiser PXC 550 Wires ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.6; 28 -3.7; 31 -4.5; 34 -5.0; 37 -5.4; 41 -5.6; 45 -5.6; 49 -5.5; 54 -5.3; 60 -5.2; 66 -5.1; 72 -5.0; 79 -5.0; 87 -5.2; 96 -5.5; 106 -5.8; 116 -6.1; 128 -6.6; 141 -7.0; 155 -7.2; 170 -7.1; 187 -7.2; 206 -7.1; 227 -6.7; 249 -6.4; 274 -5.9; 302 -5.4; 332 -5.0; 365 -4.8; 402 -4.8; 442 -4.8; 486 -5.2; 535 -5.5; 588 -5.4; 647 -5.8; 712 -6.1; 783 -6.2; 861 -7.0; 947 -7.6; 1042 -8.3; 1146 -8.5; 1261 -7.4; 1387 -9.2; 1526 -9.9; 1678 -10.2; 1846 -8.4; 2031 -8.7; 2234 -8.2; 2457 -6.9; 2703 -5.2; 2973 -4.6; 3270 -4.2; 3597 -5.8; 3957 -4.9; 4353 -1.2; 4788 -11.0; 5267 -10.4; 5793 -4.5; 6373 -3.6; 7010 -6.3; 7711 -8.7; 8482 -11.4; 9330 -12.4; 10263 -9.0; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -6.8; 18182 -7.3; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wires ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wires ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 1646 Hz |  2.18 | -3.4 dB |
| Peaking | 3213 Hz |  2.57 | 3.1 dB  |
| Peaking | 6331 Hz |  7.92 | 4.4 dB  |
| Peaking | 8999 Hz |  3.58 | -6.2 dB |
| Peaking | 18 Hz   |  1.42 | 7.1 dB  |
| Peaking | 74 Hz   |  1.97 | 1.7 dB  |
| Peaking | 420 Hz  |  1.61 | 2.3 dB  |
| Peaking | 4318 Hz | 11.11 | 6.7 dB  |
| Peaking | 4981 Hz |  9.6  | -8.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wires%20ANC%20Active/Sennheiser%20PXC%20550%20Wires%20ANC%20Active.png)