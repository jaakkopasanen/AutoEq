# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.5; 31 -7.8; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.5; 72 -9.7; 79 -9.9; 87 -10.1; 96 -10.2; 106 -10.7; 116 -10.9; 128 -10.8; 141 -11.2; 155 -11.3; 170 -10.5; 187 -10.4; 206 -9.6; 227 -8.6; 249 -7.5; 274 -6.2; 302 -4.6; 332 -3.8; 365 -2.8; 402 -2.6; 442 -2.5; 486 -2.6; 535 -2.2; 588 -2.2; 647 -2.8; 712 -4.0; 783 -5.0; 861 -6.0; 947 -6.4; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -8.0; 1526 -8.3; 1678 -8.5; 1846 -8.3; 2031 -7.9; 2234 -7.9; 2457 -7.7; 2703 -7.4; 2973 -7.3; 3270 -7.8; 3597 -7.9; 3957 -7.6; 4353 -6.8; 4788 -6.6; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.52 | -2.6 dB |
| Peaking | 173 Hz  | 0.96 | -4.3 dB |
| Peaking | 462 Hz  | 0.76 | 7.1 dB  |
| Peaking | 1521 Hz | 0.27 | -2.6 dB |
| Peaking | 5928 Hz | 3.21 | 7.9 dB  |
| Peaking | 479 Hz  | 6.54 | -0.8 dB |
| Peaking | 615 Hz  | 4.87 | 0.8 dB  |
| Peaking | 1655 Hz | 1.42 | -0.9 dB |
| Peaking | 2852 Hz | 1.05 | 1.4 dB  |
| Peaking | 3890 Hz | 1.91 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 5.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Inspiration/Monster%20Inspiration.png)