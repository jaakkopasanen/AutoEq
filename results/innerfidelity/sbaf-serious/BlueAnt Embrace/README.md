# BlueAnt Embrace
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -2.0; 60 -2.8; 66 -3.5; 72 -4.3; 79 -5.0; 87 -5.9; 96 -6.7; 106 -7.3; 116 -7.7; 128 -8.4; 141 -8.9; 155 -9.2; 170 -9.1; 187 -9.3; 206 -9.2; 227 -8.4; 249 -7.8; 274 -7.7; 302 -7.5; 332 -6.7; 365 -5.7; 402 -4.3; 442 -3.0; 486 -2.0; 535 -1.4; 588 -0.6; 647 -0.7; 712 -1.5; 783 -3.2; 861 -4.9; 947 -6.0; 1042 -6.8; 1146 -7.1; 1261 -7.2; 1387 -7.4; 1526 -7.8; 1678 -7.8; 1846 -7.2; 2031 -6.2; 2234 -4.0; 2457 -3.1; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.1; 5267 -6.9; 5793 -5.7; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BlueAnt Embrace GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BlueAnt Embrace ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.44 | 6.9 dB  |
| Peaking | 144 Hz  |  0.64 | -4.6 dB |
| Peaking | 577 Hz  |  1.92 | 6.9 dB  |
| Peaking | 3535 Hz |  1.76 | 7.1 dB  |
| Peaking | 4446 Hz |  2.56 | -0.5 dB |
| Peaking | 1440 Hz |  0.45 | 2.8 dB  |
| Peaking | 1504 Hz |  0.86 | -5.0 dB |
| Peaking | 2638 Hz |  4.66 | 2.3 dB  |
| Peaking | 5377 Hz |  9.89 | -3.1 dB |
| Peaking | 6691 Hz | 10.05 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 6.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BlueAnt%20Embrace/BlueAnt%20Embrace.png)