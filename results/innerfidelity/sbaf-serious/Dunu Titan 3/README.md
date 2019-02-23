# Dunu Titan 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.0; 25 -5.0; 28 -5.1; 31 -5.2; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.6; 49 -5.7; 54 -5.7; 60 -5.9; 66 -6.2; 72 -6.5; 79 -6.7; 87 -6.9; 96 -7.3; 106 -7.2; 116 -7.3; 128 -7.5; 141 -7.4; 155 -7.3; 170 -7.2; 187 -7.0; 206 -6.8; 227 -6.4; 249 -6.2; 274 -5.7; 302 -5.5; 332 -5.1; 365 -4.8; 402 -4.3; 442 -3.3; 486 -3.5; 535 -3.3; 588 -2.8; 647 -2.6; 712 -2.6; 783 -2.6; 861 -2.9; 947 -3.3; 1042 -3.8; 1146 -4.2; 1261 -4.8; 1387 -5.6; 1526 -6.5; 1678 -7.3; 1846 -7.8; 2031 -8.2; 2234 -8.7; 2457 -8.3; 2703 -7.3; 2973 -4.9; 3270 -2.4; 3597 -1.3; 3957 -2.5; 4353 -6.2; 4788 -10.6; 5267 -11.9; 5793 -5.1; 6373 -0.5; 7010 -2.4; 7711 -4.7; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 123 Hz  | 1.04 | -2.8 dB |
| Peaking | 2287 Hz | 2.3  | -4.6 dB |
| Peaking | 3629 Hz | 2.85 | 5.7 dB  |
| Peaking | 5086 Hz | 3.84 | -9.7 dB |
| Peaking | 6373 Hz | 4.58 | 6.7 dB  |
| Peaking | 236 Hz  | 1.61 | -1.0 dB |
| Peaking | 699 Hz  | 0.91 | 2.7 dB  |
| Peaking | 1617 Hz | 2.86 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%203/Dunu%20Titan%203.png)