# Monster Beats Solo sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.7; 28 -11.9; 31 -12.1; 34 -12.2; 37 -12.3; 41 -12.4; 45 -12.5; 49 -12.6; 54 -12.7; 60 -13.0; 66 -13.1; 72 -13.2; 79 -13.2; 87 -13.2; 96 -14.0; 106 -14.9; 116 -14.7; 128 -14.2; 141 -14.6; 155 -15.6; 170 -15.2; 187 -15.6; 206 -15.1; 227 -14.2; 249 -13.1; 274 -11.7; 302 -9.9; 332 -8.3; 365 -6.8; 402 -5.2; 442 -3.6; 486 -2.7; 535 -2.3; 588 -3.0; 647 -4.3; 712 -5.5; 783 -6.1; 861 -6.5; 947 -6.6; 1042 -6.1; 1146 -5.4; 1261 -4.7; 1387 -4.6; 1526 -4.4; 1678 -4.3; 1846 -4.2; 2031 -3.6; 2234 -3.5; 2457 -3.0; 2703 -2.7; 2973 -2.1; 3270 -2.2; 3597 -2.0; 3957 -2.7; 4353 -4.1; 4788 -4.5; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.36 | -5.7 dB |
| Peaking | 133 Hz  | 0.94 | -6.0 dB |
| Peaking | 220 Hz  | 1.68 | -6.7 dB |
| Peaking | 1047 Hz | 0.09 | 3.0 dB  |
| Peaking | 521 Hz  | 2.82 | 3.7 dB  |
| Peaking | 884 Hz  | 1.5  | -3.0 dB |
| Peaking | 3396 Hz | 1.52 | 4.3 dB  |
| Peaking | 5632 Hz | 0.73 | -5.3 dB |
| Peaking | 5988 Hz | 2.66 | 8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo%20sample%201/Monster%20Beats%20Solo%20sample%201.png)