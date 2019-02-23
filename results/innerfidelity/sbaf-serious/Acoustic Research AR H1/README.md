# Acoustic Research AR H1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.5; 25 -3.6; 28 -3.8; 31 -3.9; 34 -4.0; 37 -4.1; 41 -4.1; 45 -4.2; 49 -4.3; 54 -4.4; 60 -4.6; 66 -4.8; 72 -5.0; 79 -5.3; 87 -5.7; 96 -6.2; 106 -6.6; 116 -6.9; 128 -7.5; 141 -7.8; 155 -8.1; 170 -8.3; 187 -8.5; 206 -8.2; 227 -7.3; 249 -7.2; 274 -7.7; 302 -8.0; 332 -8.4; 365 -9.1; 402 -8.8; 442 -8.1; 486 -6.7; 535 -7.9; 588 -8.5; 647 -9.6; 712 -6.8; 783 -4.7; 861 -6.7; 947 -7.4; 1042 -7.1; 1146 -7.3; 1261 -7.2; 1387 -7.0; 1526 -6.0; 1678 -7.9; 1846 -8.3; 2031 -7.4; 2234 -6.6; 2457 -5.6; 2703 -4.5; 2973 -2.6; 3270 -0.8; 3597 -0.5; 3957 -0.9; 4353 -4.9; 4788 -6.9; 5267 -4.7; 5793 -3.1; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -9.1; 9330 -10.7; 10263 -8.9; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.38 | 3.3 dB  |
| Peaking | 217 Hz   | 0.31 | -2.1 dB |
| Peaking | 3490 Hz  | 3.3  | 6.8 dB  |
| Peaking | 6461 Hz  | 3.4  | 4.0 dB  |
| Peaking | 9259 Hz  | 3.43 | -5.0 dB |
| Peaking | 246 Hz   | 7.48 | 1.2 dB  |
| Peaking | 669 Hz   | 6.4  | -3.3 dB |
| Peaking | 753 Hz   | 7.25 | 4.6 dB  |
| Peaking | 1818 Hz  | 6.61 | -2.4 dB |
| Peaking | 12922 Hz | 2.57 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Acoustic%20Research%20AR%20H1/Acoustic%20Research%20AR%20H1.png)