# Koss Pro4AA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.6; 25 -6.1; 28 -6.8; 31 -7.3; 34 -7.7; 37 -8.2; 41 -8.6; 45 -9.0; 49 -9.3; 54 -9.8; 60 -10.2; 66 -10.5; 72 -10.8; 79 -11.2; 87 -12.3; 96 -13.2; 106 -13.2; 116 -13.8; 128 -14.8; 141 -15.2; 155 -15.4; 170 -15.4; 187 -15.9; 206 -15.9; 227 -15.6; 249 -15.1; 274 -14.2; 302 -13.8; 332 -14.1; 365 -13.5; 402 -12.6; 442 -11.6; 486 -10.9; 535 -9.9; 588 -8.8; 647 -8.0; 712 -7.7; 783 -7.3; 861 -6.8; 947 -6.3; 1042 -6.1; 1146 -5.7; 1261 -5.5; 1387 -5.9; 1526 -6.4; 1678 -7.1; 1846 -7.8; 2031 -8.6; 2234 -10.1; 2457 -11.0; 2703 -11.4; 2973 -11.7; 3270 -9.3; 3597 -6.9; 3957 -5.1; 4353 -7.1; 4788 -3.1; 5267 -0.5; 5793 -4.2; 6373 -6.5; 7010 -3.9; 7711 -6.0; 8482 -6.2; 9330 -6.2; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4AA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  2.85 | 2.0 dB  |
| Peaking | 155 Hz  |  0.6  | -9.0 dB |
| Peaking | 342 Hz  |  1.53 | -3.3 dB |
| Peaking | 2712 Hz |  2.71 | -5.9 dB |
| Peaking | 5191 Hz |  5.56 | 6.5 dB  |
| Peaking | 487 Hz  |  4.75 | -0.7 dB |
| Peaking | 1183 Hz |  1.46 | 2.1 dB  |
| Peaking | 2492 Hz |  0.42 | -0.8 dB |
| Peaking | 3846 Hz |  7.49 | 2.2 dB  |
| Peaking | 6974 Hz | 10.61 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA/Koss%20Pro4AA.png)