# Massdrop Nobel X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.4; 25 -7.5; 28 -7.6; 31 -7.7; 34 -7.8; 37 -8.0; 41 -8.1; 45 -8.3; 49 -8.4; 54 -8.7; 60 -9.0; 66 -9.3; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.8; 106 -11.1; 116 -11.2; 128 -11.5; 141 -11.6; 155 -11.8; 170 -11.9; 187 -11.8; 206 -11.8; 227 -11.6; 249 -11.5; 274 -11.2; 302 -10.9; 332 -10.5; 365 -10.1; 402 -9.7; 442 -9.1; 486 -8.8; 535 -8.4; 588 -7.6; 647 -7.2; 712 -6.9; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.8; 1387 -7.2; 1526 -7.6; 1678 -7.8; 1846 -7.6; 2031 -7.3; 2234 -7.0; 2457 -5.9; 2703 -4.9; 2973 -3.1; 3270 -1.2; 3597 -0.5; 3957 -1.4; 4353 -4.4; 4788 -6.1; 5267 -4.5; 5793 -2.7; 6373 -2.2; 7010 -4.0; 7711 -7.3; 8482 -10.9; 9330 -10.9; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Nobel X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Nobel X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 134 Hz   | 0.52 | -4.6 dB |
| Peaking | 284 Hz   | 1.05 | -2.1 dB |
| Peaking | 3532 Hz  | 3.53 | 6.6 dB  |
| Peaking | 6390 Hz  | 3.51 | 5.2 dB  |
| Peaking | 8822 Hz  | 3.52 | -6.0 dB |
| Peaking | 864 Hz   | 2.26 | 1.0 dB  |
| Peaking | 1934 Hz  | 1.46 | -2.4 dB |
| Peaking | 2596 Hz  | 1.03 | 1.3 dB  |
| Peaking | 4725 Hz  | 9.7  | -1.8 dB |
| Peaking | 11065 Hz | 7.55 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20Nobel%20X/Massdrop%20Nobel%20X.png)