# Beyerdynamic DJX-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.4; 37 -1.8; 41 -2.3; 45 -2.7; 49 -3.1; 54 -3.5; 60 -3.8; 66 -4.0; 72 -4.1; 79 -4.6; 87 -4.5; 96 -4.8; 106 -5.2; 116 -5.6; 128 -6.0; 141 -6.6; 155 -6.9; 170 -6.8; 187 -7.3; 206 -7.6; 227 -7.7; 249 -7.8; 274 -7.7; 302 -7.5; 332 -7.1; 365 -6.7; 402 -6.4; 442 -6.4; 486 -6.8; 535 -7.5; 588 -7.6; 647 -7.9; 712 -8.1; 783 -7.8; 861 -7.6; 947 -6.9; 1042 -6.9; 1146 -7.2; 1261 -6.9; 1387 -6.9; 1526 -6.7; 1678 -6.8; 1846 -6.4; 2031 -5.8; 2234 -5.5; 2457 -5.2; 2703 -4.5; 2973 -4.0; 3270 -3.7; 3597 -3.0; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -9.8; 9330 -9.6; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DJX-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DJX-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.56 | 6.3 dB  |
| Peaking | 88 Hz   |  1.75 | 1.4 dB  |
| Peaking | 913 Hz  |  0.1  | -1.1 dB |
| Peaking | 5258 Hz |  0.87 | 8.1 dB  |
| Peaking | 8644 Hz |  2.6  | -6.9 dB |
| Peaking | 257 Hz  |  1.32 | -0.8 dB |
| Peaking | 404 Hz  |  2.28 | 1.5 dB  |
| Peaking | 677 Hz  |  3.31 | -0.8 dB |
| Peaking | 5189 Hz |  7.16 | -0.7 dB |
| Peaking | 6343 Hz | 10.43 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DJX-1/Beyerdynamic%20DJX-1.png)