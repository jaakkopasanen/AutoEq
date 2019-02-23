# Massdrop Nobel X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.3; 28 -6.4; 31 -6.5; 34 -6.6; 37 -6.8; 41 -6.9; 45 -7.1; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.5; 79 -8.8; 87 -9.2; 96 -9.6; 106 -9.9; 116 -10.0; 128 -10.3; 141 -10.4; 155 -10.7; 170 -10.7; 187 -10.6; 206 -10.6; 227 -10.4; 249 -10.3; 274 -10.0; 302 -9.7; 332 -9.4; 365 -9.0; 402 -8.5; 442 -8.0; 486 -7.6; 535 -7.2; 588 -6.5; 647 -6.0; 712 -5.7; 783 -5.2; 861 -5.2; 947 -5.2; 1042 -5.3; 1146 -5.5; 1261 -5.6; 1387 -6.0; 1526 -6.4; 1678 -6.6; 1846 -6.4; 2031 -6.1; 2234 -5.9; 2457 -4.7; 2703 -3.8; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.3; 4788 -4.9; 5267 -3.3; 5793 -1.5; 6373 -1.1; 7010 -4.0; 7711 -6.5; 8482 -9.7; 9330 -9.7; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Nobel X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Nobel X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 181 Hz  |  0.53 | -4.3 dB |
| Peaking | 808 Hz  |  1.53 | 2.1 dB  |
| Peaking | 3484 Hz |  2.45 | 6.5 dB  |
| Peaking | 6236 Hz |  3.53 | 5.7 dB  |
| Peaking | 8803 Hz |  3.7  | -4.7 dB |
| Peaking | 24 Hz   |  1.07 | 0.5 dB  |
| Peaking | 1860 Hz |  1.96 | -1.3 dB |
| Peaking | 2244 Hz |  0.62 | 0.6 dB  |
| Peaking | 4767 Hz | 10.79 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20Nobel%20X/Massdrop%20Nobel%20X.png)