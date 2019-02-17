# Monster Beats Solo sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.5; 31 -2.1; 34 -2.6; 37 -3.3; 41 -4.1; 45 -4.1; 49 -3.8; 54 -3.8; 60 -4.5; 66 -5.2; 72 -6.1; 79 -7.8; 87 -9.3; 96 -10.4; 106 -11.4; 116 -12.1; 128 -12.4; 141 -12.6; 155 -12.7; 170 -12.7; 187 -12.5; 206 -11.4; 227 -11.2; 249 -12.0; 274 -11.7; 302 -9.7; 332 -7.3; 365 -5.1; 402 -4.4; 442 -3.4; 486 -2.9; 535 -3.6; 588 -4.2; 647 -5.1; 712 -6.0; 783 -6.3; 861 -6.6; 947 -6.6; 1042 -6.3; 1146 -6.0; 1261 -5.6; 1387 -5.6; 1526 -5.2; 1678 -4.5; 1846 -3.4; 2031 -2.2; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.6; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.27 | 6.7 dB  |
| Peaking | 135 Hz  | 1.26 | -7.5 dB |
| Peaking | 254 Hz  | 4.42 | -4.3 dB |
| Peaking | 2882 Hz | 1.11 | 6.3 dB  |
| Peaking | 5766 Hz | 3.33 | 5.1 dB  |
| Peaking | 97 Hz   | 4.17 | -1.4 dB |
| Peaking | 143 Hz  | 2.3  | 2.0 dB  |
| Peaking | 176 Hz  | 2.12 | -2.3 dB |
| Peaking | 471 Hz  | 2.59 | 4.3 dB  |
| Peaking | 8384 Hz | 3.72 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo%20sample%202/Monster%20Beats%20Solo%20sample%202.png)