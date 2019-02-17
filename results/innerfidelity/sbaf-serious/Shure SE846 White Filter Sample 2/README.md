# Shure SE846 White Filter Sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -8.9; 25 -8.9; 28 -8.9; 31 -8.9; 34 -8.9; 37 -8.9; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.8; 60 -8.8; 66 -8.8; 72 -8.8; 79 -8.9; 87 -8.9; 96 -9.0; 106 -8.9; 116 -8.7; 128 -8.6; 141 -8.5; 155 -8.4; 170 -8.2; 187 -8.0; 206 -7.8; 227 -7.5; 249 -7.3; 274 -7.1; 302 -6.9; 332 -6.7; 365 -6.6; 402 -6.5; 442 -6.2; 486 -6.3; 535 -6.2; 588 -5.8; 647 -5.7; 712 -5.7; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -7.8; 1526 -8.4; 1678 -8.8; 1846 -8.9; 2031 -8.6; 2234 -7.9; 2457 -5.7; 2703 -3.2; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -3.4; 4788 -2.9; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.1; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 White Filter Sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.19 | -2.5 dB |
| Peaking | 719 Hz  | 0.59 | 1.5 dB  |
| Peaking | 2003 Hz | 1.1  | -5.0 dB |
| Peaking | 3185 Hz | 1.73 | 8.4 dB  |
| Peaking | 5802 Hz | 3.52 | 5.8 dB  |
| Peaking | 57 Hz   | 1.45 | 0.3 dB  |
| Peaking | 96 Hz   | 1.9  | -0.3 dB |
| Peaking | 6628 Hz | 8.08 | 2.1 dB  |
| Peaking | 7938 Hz | 3.82 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20White%20Filter%20Sample%202/Shure%20SE846%20White%20Filter%20Sample%202.png)