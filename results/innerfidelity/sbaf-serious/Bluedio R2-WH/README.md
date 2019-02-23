# Bluedio R2-WH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -8.0; 25 -8.7; 28 -9.7; 31 -10.5; 34 -11.1; 37 -11.5; 41 -12.0; 45 -12.3; 49 -12.4; 54 -12.6; 60 -12.8; 66 -12.9; 72 -12.9; 79 -12.9; 87 -12.8; 96 -12.9; 106 -13.5; 116 -13.6; 128 -13.7; 141 -14.1; 155 -14.3; 170 -14.0; 187 -14.1; 206 -13.7; 227 -13.6; 249 -13.0; 274 -13.5; 302 -13.0; 332 -12.3; 365 -12.3; 402 -11.4; 442 -10.6; 486 -10.3; 535 -9.3; 588 -7.5; 647 -6.4; 712 -5.4; 783 -4.9; 861 -5.9; 947 -7.4; 1042 -8.2; 1146 -8.1; 1261 -7.9; 1387 -7.9; 1526 -7.9; 1678 -8.3; 1846 -8.9; 2031 -9.1; 2234 -8.2; 2457 -8.1; 2703 -7.9; 2973 -6.5; 3270 -4.5; 3597 -4.1; 3957 -2.1; 4353 -1.7; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio R2-WH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio R2-WH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.38 | -6.4 dB |
| Peaking | 263 Hz  | 0.94 | -4.3 dB |
| Peaking | 1916 Hz | 2.31 | -2.8 dB |
| Peaking | 2660 Hz | 5.78 | -1.8 dB |
| Peaking | 5126 Hz | 1.49 | 6.0 dB  |
| Peaking | 20 Hz   | 2.67 | 1.5 dB  |
| Peaking | 730 Hz  | 2.38 | 6.0 dB  |
| Peaking | 748 Hz  | 1.07 | -3.0 dB |
| Peaking | 6394 Hz | 4.59 | 3.2 dB  |
| Peaking | 7634 Hz | 1.92 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bluedio%20R2-WH/Bluedio%20R2-WH.png)