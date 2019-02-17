# Monster Beats Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.4; 25 -6.2; 28 -7.1; 31 -7.9; 34 -8.7; 37 -9.3; 41 -10.0; 45 -10.5; 49 -10.9; 54 -11.2; 60 -11.4; 66 -11.5; 72 -11.5; 79 -11.7; 87 -11.9; 96 -12.3; 106 -12.4; 116 -12.5; 128 -12.7; 141 -12.9; 155 -12.9; 170 -12.8; 187 -12.6; 206 -12.6; 227 -12.4; 249 -12.2; 274 -11.8; 302 -11.4; 332 -10.8; 365 -10.0; 402 -9.8; 442 -9.6; 486 -9.5; 535 -9.4; 588 -8.9; 647 -8.6; 712 -8.5; 783 -8.0; 861 -7.5; 947 -6.6; 1042 -6.3; 1146 -6.3; 1261 -6.1; 1387 -6.0; 1526 -6.7; 1678 -7.9; 1846 -9.1; 2031 -10.6; 2234 -12.4; 2457 -13.7; 2703 -14.2; 2973 -13.1; 3270 -11.4; 3597 -9.2; 3957 -7.9; 4353 -10.2; 4788 -10.5; 5267 -6.0; 5793 -0.5; 6373 -3.7; 7010 -6.0; 7711 -6.6; 8482 -8.3; 9330 -11.0; 10263 -10.1; 11289 -6.4; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 1.28 | -2.7 dB |
| Peaking | 169 Hz  | 0.47 | -6.6 dB |
| Peaking | 2704 Hz | 1.89 | -8.1 dB |
| Peaking | 5920 Hz | 8.14 | 7.6 dB  |
| Peaking | 9594 Hz | 4.41 | -5.4 dB |
| Peaking | 18 Hz   | 2.68 | 2.8 dB  |
| Peaking | 1328 Hz | 2.44 | 1.8 dB  |
| Peaking | 2156 Hz | 3.12 | -1.2 dB |
| Peaking | 4529 Hz | 1.74 | 2.5 dB  |
| Peaking | 4675 Hz | 5.05 | -6.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Pro/Monster%20Beats%20Pro.png)