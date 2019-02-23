# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.5; 28 -7.9; 31 -8.1; 34 -8.3; 37 -8.5; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.4; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.2; 87 -10.5; 96 -10.6; 106 -11.1; 116 -11.3; 128 -11.2; 141 -11.6; 155 -11.6; 170 -10.8; 187 -10.7; 206 -10.0; 227 -8.9; 249 -7.9; 274 -6.6; 302 -4.9; 332 -4.2; 365 -3.2; 402 -3.0; 442 -2.8; 486 -2.9; 535 -2.6; 588 -2.6; 647 -3.2; 712 -4.3; 783 -5.3; 861 -6.4; 947 -6.7; 1042 -7.0; 1146 -7.4; 1261 -7.8; 1387 -8.3; 1526 -8.7; 1678 -8.8; 1846 -8.6; 2031 -8.3; 2234 -8.3; 2457 -8.1; 2703 -7.7; 2973 -7.7; 3270 -8.1; 3597 -8.3; 3957 -7.9; 4353 -7.2; 4788 -7.0; 5267 -2.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.48 | -2.8 dB |
| Peaking | 172 Hz  | 0.92 | -4.5 dB |
| Peaking | 462 Hz  | 0.75 | 7.1 dB  |
| Peaking | 1530 Hz | 0.27 | -3.0 dB |
| Peaking | 5954 Hz | 3.25 | 8.1 dB  |
| Peaking | 475 Hz  | 6.37 | -0.8 dB |
| Peaking | 611 Hz  | 4.75 | 0.8 dB  |
| Peaking | 1723 Hz | 1.13 | -1.1 dB |
| Peaking | 2858 Hz | 0.87 | 1.7 dB  |
| Peaking | 3916 Hz | 1.81 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 5.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Inspiration/Monster%20Inspiration.png)