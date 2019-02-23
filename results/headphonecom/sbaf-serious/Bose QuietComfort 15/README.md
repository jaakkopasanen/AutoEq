# Bose QuietComfort 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -10.3; 25 -11.6; 28 -12.0; 31 -11.3; 34 -10.1; 37 -9.2; 41 -8.5; 45 -8.1; 49 -7.8; 54 -7.6; 60 -7.3; 66 -7.3; 72 -7.5; 79 -7.6; 87 -7.5; 96 -7.4; 106 -7.3; 116 -7.1; 128 -7.0; 141 -6.9; 155 -6.6; 170 -6.3; 187 -6.2; 206 -5.9; 227 -5.7; 249 -5.7; 274 -5.4; 302 -5.1; 332 -4.7; 365 -4.2; 402 -3.8; 442 -3.4; 486 -3.0; 535 -2.7; 588 -2.2; 647 -1.5; 712 -1.3; 783 -0.8; 861 -0.5; 947 -0.8; 1042 -1.5; 1146 -2.2; 1261 -2.9; 1387 -3.4; 1526 -3.3; 1678 -5.2; 1846 -7.5; 2031 -9.9; 2234 -11.1; 2457 -10.6; 2703 -8.5; 2973 -5.6; 3270 -3.8; 3597 -4.1; 3957 -8.2; 4353 -11.4; 4788 -8.1; 5267 -4.9; 5793 -8.0; 6373 -4.7; 7010 -3.6; 7711 -4.8; 8482 -5.1; 9330 -6.6; 10263 -7.9; 11289 -5.2; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -6.3; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  1.84 | -6.3 dB |
| Peaking | 92 Hz    |  0.42 | -2.2 dB |
| Peaking | 852 Hz   |  0.78 | 4.5 dB  |
| Peaking | 2217 Hz  |  3.06 | -7.7 dB |
| Peaking | 4376 Hz  |  7.08 | -6.9 dB |
| Peaking | 2628 Hz  |  7.17 | -1.8 dB |
| Peaking | 3236 Hz  |  5.8  | 2.7 dB  |
| Peaking | 5961 Hz  | 11.31 | -4.9 dB |
| Peaking | 6614 Hz  |  3.36 | 2.2 dB  |
| Peaking | 10004 Hz |  5.86 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)