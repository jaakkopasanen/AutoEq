# Monster Beats Solo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.7; 25 -8.1; 28 -8.6; 31 -9.0; 34 -9.3; 37 -9.7; 41 -10.1; 45 -10.2; 49 -10.1; 54 -10.2; 60 -10.7; 66 -11.1; 72 -11.6; 79 -12.4; 87 -13.2; 96 -14.1; 106 -15.1; 116 -15.3; 128 -15.2; 141 -15.5; 155 -16.1; 170 -15.8; 187 -15.9; 206 -15.1; 227 -14.6; 249 -14.4; 274 -13.6; 302 -11.7; 332 -9.7; 365 -7.8; 402 -6.7; 442 -5.4; 486 -4.7; 535 -4.9; 588 -5.5; 647 -6.6; 712 -7.6; 783 -8.1; 861 -8.5; 947 -8.5; 1042 -8.1; 1146 -7.6; 1261 -7.1; 1387 -7.0; 1526 -6.7; 1678 -6.3; 1846 -5.7; 2031 -4.8; 2234 -4.4; 2457 -3.5; 2703 -3.3; 2973 -2.7; 3270 -2.7; 3597 -2.7; 3957 -3.7; 4353 -5.8; 4788 -5.0; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 110 Hz  | 0.78 | -7.8 dB |
| Peaking | 210 Hz  | 1.72 | -5.9 dB |
| Peaking | 968 Hz  | 3.59 | -2.2 dB |
| Peaking | 2997 Hz | 1.78 | 3.9 dB  |
| Peaking | 5941 Hz | 3.91 | 6.3 dB  |
| Peaking | 37 Hz   | 1.42 | -1.7 dB |
| Peaking | 75 Hz   | 2.33 | 0.8 dB  |
| Peaking | 281 Hz  | 5.7  | -2.2 dB |
| Peaking | 479 Hz  | 2.89 | 3.4 dB  |
| Peaking | 8261 Hz | 4.64 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo/Monster%20Beats%20Solo.png)