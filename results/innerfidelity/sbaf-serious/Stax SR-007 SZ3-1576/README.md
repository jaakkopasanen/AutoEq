# Stax SR-007 SZ3-1576
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -1.9; 41 -2.5; 45 -2.7; 49 -2.5; 54 -1.8; 60 -1.7; 66 -2.6; 72 -4.0; 79 -4.0; 87 -3.5; 96 -3.4; 106 -3.4; 116 -3.3; 128 -3.3; 141 -3.3; 155 -3.3; 170 -3.5; 187 -3.5; 206 -3.5; 227 -3.5; 249 -3.6; 274 -3.5; 302 -3.7; 332 -3.8; 365 -3.9; 402 -4.0; 442 -4.1; 486 -4.3; 535 -2.8; 588 -2.9; 647 -4.2; 712 -4.9; 783 -5.4; 861 -6.2; 947 -6.5; 1042 -6.0; 1146 -5.8; 1261 -2.7; 1387 -1.4; 1526 -5.6; 1678 -6.4; 1846 -3.9; 2031 -2.2; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -2.6; 5267 -1.8; 5793 -0.6; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 SZ3-1576 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 SZ3-1576 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.25 | 6.3 dB  |
| Peaking | 221 Hz  | 0.57 | 2.7 dB  |
| Peaking | 563 Hz  | 5.47 | 2.9 dB  |
| Peaking | 3089 Hz | 1    | 6.5 dB  |
| Peaking | 5809 Hz | 4.35 | 3.9 dB  |
| Peaking | 1038 Hz | 2.08 | -3.0 dB |
| Peaking | 1339 Hz | 1.01 | 2.1 dB  |
| Peaking | 1359 Hz | 5.85 | 4.0 dB  |
| Peaking | 1626 Hz | 4.83 | -4.6 dB |
| Peaking | 8630 Hz | 2.89 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.3 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007%20SZ3-1576/Stax%20SR-007%20SZ3-1576.png)