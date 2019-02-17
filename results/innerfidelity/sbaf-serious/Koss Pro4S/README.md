# Koss Pro4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.7; 25 -4.2; 28 -4.9; 31 -5.4; 34 -5.8; 37 -6.1; 41 -6.5; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.5; 66 -7.7; 72 -7.9; 79 -8.1; 87 -8.3; 96 -8.3; 106 -8.1; 116 -7.6; 128 -6.5; 141 -5.8; 155 -6.4; 170 -5.1; 187 -3.4; 206 -3.3; 227 -2.5; 249 -0.9; 274 -2.1; 302 -4.1; 332 -5.6; 365 -5.7; 402 -5.9; 442 -6.0; 486 -6.5; 535 -6.7; 588 -6.4; 647 -6.6; 712 -6.8; 783 -6.7; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.6; 1261 -7.1; 1387 -7.5; 1526 -7.7; 1678 -8.0; 1846 -8.2; 2031 -8.6; 2234 -8.4; 2457 -9.4; 2703 -9.8; 2973 -9.1; 3270 -7.8; 3597 -6.6; 3957 -4.0; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.67 | 3.5 dB  |
| Peaking | 85 Hz   |  1.36 | -2.2 dB |
| Peaking | 241 Hz  |  2.2  | 5.4 dB  |
| Peaking | 2788 Hz |  1.17 | -4.4 dB |
| Peaking | 5019 Hz |  1.7  | 8.2 dB  |
| Peaking | 182 Hz  | 12.72 | 1.4 dB  |
| Peaking | 507 Hz  |  0.66 | -0.3 dB |
| Peaking | 1062 Hz |  5.64 | 0.6 dB  |
| Peaking | 6478 Hz |  5.05 | 3.3 dB  |
| Peaking | 7479 Hz |  1.84 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4S/Koss%20Pro4S.png)