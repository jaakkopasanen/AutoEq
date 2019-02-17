# Yamaha HP1 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.6; 25 -2.0; 28 -2.5; 31 -3.0; 34 -3.3; 37 -3.5; 41 -3.8; 45 -4.0; 49 -4.1; 54 -4.4; 60 -4.7; 66 -5.0; 72 -5.2; 79 -5.5; 87 -5.7; 96 -6.1; 106 -6.3; 116 -6.4; 128 -6.8; 141 -7.1; 155 -7.3; 170 -7.4; 187 -7.5; 206 -7.6; 227 -7.6; 249 -7.7; 274 -7.4; 302 -7.4; 332 -7.3; 365 -7.2; 402 -7.3; 442 -7.1; 486 -7.2; 535 -7.2; 588 -6.8; 647 -6.9; 712 -7.0; 783 -6.6; 861 -6.6; 947 -6.5; 1042 -6.2; 1146 -5.5; 1261 -4.3; 1387 -4.0; 1526 -4.1; 1678 -3.3; 1846 -3.2; 2031 -4.4; 2234 -6.2; 2457 -4.8; 2703 -5.7; 2973 -3.1; 3270 -1.3; 3597 -0.6; 3957 -1.4; 4353 -3.0; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.21 | 5.2 dB  |
| Peaking | 51 Hz   |  1.9  | 1.6 dB  |
| Peaking | 1639 Hz |  2.56 | 3.1 dB  |
| Peaking | 3568 Hz |  3.26 | 5.4 dB  |
| Peaking | 5665 Hz |  2.74 | 6.2 dB  |
| Peaking | 209 Hz  |  1.45 | -1.1 dB |
| Peaking | 495 Hz  |  0.76 | -0.6 dB |
| Peaking | 1267 Hz |  6.9  | 1.2 dB  |
| Peaking | 2258 Hz | 11.55 | -1.1 dB |
| Peaking | 8190 Hz |  4.77 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1%20sample%201/Yamaha%20HP1%20sample%201.png)