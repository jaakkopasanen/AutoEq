# Audeze SINE DX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -0.7; 45 -0.7; 49 -0.7; 54 -0.9; 60 -1.1; 66 -1.3; 72 -1.5; 79 -1.7; 87 -2.0; 96 -2.3; 106 -2.5; 116 -2.7; 128 -2.9; 141 -3.2; 155 -3.4; 170 -3.5; 187 -3.4; 206 -3.5; 227 -3.5; 249 -3.6; 274 -3.7; 302 -3.8; 332 -3.8; 365 -3.9; 402 -4.0; 442 -4.0; 486 -4.3; 535 -4.4; 588 -4.0; 647 -3.9; 712 -4.5; 783 -4.8; 861 -5.5; 947 -6.1; 1042 -6.9; 1146 -7.6; 1261 -8.3; 1387 -8.6; 1526 -10.2; 1678 -9.7; 1846 -8.0; 2031 -5.6; 2234 -3.5; 2457 -1.9; 2703 -1.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze SINE DX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE DX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.27 | 4.9 dB  |
| Peaking | 126 Hz  | 0.19 | 2.6 dB  |
| Peaking | 635 Hz  | 2.36 | 1.1 dB  |
| Peaking | 1562 Hz | 1.89 | -6.4 dB |
| Peaking | 3603 Hz | 0.77 | 7.2 dB  |
| Peaking | 1069 Hz | 6.68 | -0.6 dB |
| Peaking | 2404 Hz | 5.74 | 1.1 dB  |
| Peaking | 3767 Hz | 3.67 | -0.9 dB |
| Peaking | 6279 Hz | 2.34 | 5.2 dB  |
| Peaking | 7358 Hz | 1.43 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE%20DX/Audeze%20SINE%20DX.png)