# Monster Beats Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.3; 25 -3.0; 28 -4.0; 31 -4.8; 34 -5.5; 37 -6.1; 41 -6.8; 45 -7.4; 49 -7.7; 54 -8.1; 60 -8.3; 66 -8.4; 72 -8.4; 79 -8.6; 87 -8.8; 96 -9.2; 106 -9.3; 116 -9.4; 128 -9.5; 141 -9.7; 155 -9.8; 170 -9.7; 187 -9.5; 206 -9.5; 227 -9.3; 249 -9.0; 274 -8.6; 302 -8.2; 332 -7.7; 365 -6.9; 402 -6.6; 442 -6.5; 486 -6.4; 535 -6.3; 588 -5.7; 647 -5.5; 712 -5.4; 783 -4.8; 861 -4.4; 947 -3.4; 1042 -3.1; 1146 -3.2; 1261 -3.0; 1387 -2.8; 1526 -3.6; 1678 -4.7; 1846 -6.0; 2031 -7.4; 2234 -9.2; 2457 -10.6; 2703 -11.1; 2973 -10.0; 3270 -8.3; 3597 -6.1; 3957 -4.7; 4353 -7.1; 4788 -7.4; 5267 -2.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -7.8; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.69 | 5.3 dB  |
| Peaking | 140 Hz  | 0.52 | -3.4 dB |
| Peaking | 1256 Hz | 0.9  | 4.2 dB  |
| Peaking | 2546 Hz | 2.23 | -6.3 dB |
| Peaking | 5977 Hz | 4.2  | 6.9 dB  |
| Peaking | 22 Hz   | 1.34 | 0.5 dB  |
| Peaking | 385 Hz  | 6.13 | 0.7 dB  |
| Peaking | 3806 Hz | 8.32 | 1.9 dB  |
| Peaking | 9596 Hz | 5.46 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Pro/Monster%20Beats%20Pro.png)