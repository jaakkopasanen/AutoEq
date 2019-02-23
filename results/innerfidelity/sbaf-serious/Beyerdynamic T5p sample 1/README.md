# Beyerdynamic T5p sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -8.8; 25 -8.7; 28 -8.4; 31 -8.1; 34 -7.8; 37 -7.5; 41 -7.2; 45 -6.9; 49 -6.8; 54 -6.5; 60 -5.8; 66 -5.1; 72 -4.7; 79 -5.6; 87 -7.6; 96 -9.6; 106 -10.3; 116 -10.4; 128 -10.1; 141 -9.5; 155 -8.5; 170 -8.2; 187 -8.6; 206 -8.1; 227 -7.5; 249 -7.0; 274 -6.5; 302 -6.1; 332 -5.9; 365 -5.6; 402 -5.6; 442 -5.4; 486 -5.6; 535 -5.3; 588 -4.4; 647 -2.3; 712 -5.1; 783 -5.9; 861 -6.3; 947 -6.6; 1042 -8.0; 1146 -7.5; 1261 -8.0; 1387 -10.2; 1526 -8.7; 1678 -8.8; 1846 -8.1; 2031 -8.6; 2234 -10.0; 2457 -8.5; 2703 -7.0; 2973 -6.2; 3270 -4.8; 3597 -3.9; 3957 -3.7; 4353 -4.7; 4788 -0.5; 5267 -1.5; 5793 -6.9; 6373 -7.8; 7010 -4.4; 7711 -6.2; 8482 -7.1; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 122 Hz  |  2.06 | -4.1 dB |
| Peaking | 638 Hz  |  3.98 | 3.9 dB  |
| Peaking | 1426 Hz |  2.58 | -3.1 dB |
| Peaking | 2242 Hz |  6.38 | -3.6 dB |
| Peaking | 4825 Hz |  4.27 | 6.3 dB  |
| Peaking | 22 Hz   |  1    | -2.4 dB |
| Peaking | 73 Hz   |  2.76 | 2.9 dB  |
| Peaking | 95 Hz   |  5.01 | -1.8 dB |
| Peaking | 3554 Hz |  5.73 | 2.3 dB  |
| Peaking | 6049 Hz | 11.72 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sample%201/Beyerdynamic%20T5p%20sample%201.png)