# Acoustic Research AR H1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.7; 25 -2.9; 28 -3.1; 31 -3.2; 34 -3.3; 37 -3.3; 41 -3.4; 45 -3.4; 49 -3.5; 54 -3.7; 60 -3.8; 66 -4.0; 72 -4.2; 79 -4.5; 87 -4.9; 96 -5.4; 106 -5.8; 116 -6.2; 128 -6.7; 141 -7.1; 155 -7.4; 170 -7.5; 187 -7.7; 206 -7.5; 227 -6.5; 249 -6.5; 274 -6.9; 302 -7.3; 332 -7.7; 365 -8.3; 402 -8.0; 442 -7.4; 486 -5.9; 535 -7.2; 588 -7.8; 647 -8.8; 712 -6.1; 783 -3.9; 861 -6.0; 947 -6.7; 1042 -6.4; 1146 -6.5; 1261 -6.4; 1387 -6.2; 1526 -5.3; 1678 -7.2; 1846 -7.5; 2031 -6.6; 2234 -5.9; 2457 -4.9; 2703 -3.7; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.1; 4788 -6.2; 5267 -3.9; 5793 -2.3; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -8.4; 9330 -10.0; 10263 -8.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustic Research AR H1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustic Research AR H1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.98 | 3.8 dB  |
| Peaking | 60 Hz   | 1.81 | 2.2 dB  |
| Peaking | 3451 Hz | 2.72 | 6.7 dB  |
| Peaking | 6295 Hz | 3.52 | 4.4 dB  |
| Peaking | 9097 Hz | 3.93 | -4.3 dB |
| Peaking | 174 Hz  | 2.85 | -1.4 dB |
| Peaking | 371 Hz  | 4.72 | -2.0 dB |
| Peaking | 673 Hz  | 5.03 | -4.0 dB |
| Peaking | 751 Hz  | 6.7  | 5.0 dB  |
| Peaking | 1810 Hz | 8.9  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Acoustic%20Research%20AR%20H1/Acoustic%20Research%20AR%20H1.png)