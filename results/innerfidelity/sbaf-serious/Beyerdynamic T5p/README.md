# Beyerdynamic T5p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.7; 28 -6.7; 31 -6.6; 34 -6.5; 37 -6.4; 41 -6.3; 45 -6.2; 49 -6.1; 54 -5.9; 60 -5.5; 66 -5.1; 72 -4.8; 79 -5.1; 87 -6.2; 96 -7.8; 106 -9.1; 116 -9.7; 128 -10.1; 141 -9.8; 155 -9.0; 170 -8.2; 187 -9.0; 206 -8.5; 227 -7.9; 249 -7.4; 274 -6.8; 302 -6.3; 332 -6.0; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.9; 535 -5.9; 588 -4.8; 647 -2.3; 712 -5.0; 783 -5.3; 861 -6.4; 947 -6.6; 1042 -6.9; 1146 -7.4; 1261 -8.5; 1387 -9.0; 1526 -9.1; 1678 -9.4; 1846 -8.9; 2031 -8.8; 2234 -10.0; 2457 -7.9; 2703 -6.2; 2973 -5.5; 3270 -4.3; 3597 -3.3; 3957 -2.3; 4353 -4.6; 4788 -0.5; 5267 -1.4; 5793 -6.2; 6373 -6.8; 7010 -4.3; 7711 -6.5; 8482 -9.2; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 127 Hz  | 3.13 | -3.9 dB |
| Peaking | 195 Hz  | 3.66 | -2.1 dB |
| Peaking | 651 Hz  | 3.84 | 4.0 dB  |
| Peaking | 1824 Hz | 1.31 | -3.5 dB |
| Peaking | 4325 Hz | 1.77 | 5.1 dB  |
| Peaking | 72 Hz   | 3.77 | 2.2 dB  |
| Peaking | 3716 Hz | 2.39 | 3.7 dB  |
| Peaking | 4543 Hz | 2.01 | -6.2 dB |
| Peaking | 4927 Hz | 5.49 | 7.2 dB  |
| Peaking | 8615 Hz | 8.28 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)