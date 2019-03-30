# Monster Beats Solo with ControlTalk Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.4; 45 -2.1; 49 -2.5; 54 -2.9; 60 -3.3; 66 -3.9; 72 -4.7; 79 -5.6; 87 -6.5; 96 -7.5; 106 -8.3; 116 -9.0; 128 -9.6; 141 -10.0; 155 -10.3; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.6; 249 -10.6; 274 -10.9; 302 -10.7; 332 -10.3; 365 -9.2; 402 -7.5; 442 -5.6; 486 -4.8; 535 -5.5; 588 -6.0; 647 -6.4; 712 -6.8; 783 -7.0; 861 -7.0; 947 -6.7; 1042 -6.3; 1146 -5.6; 1261 -4.7; 1387 -3.6; 1526 -2.5; 1678 -1.7; 1846 -1.2; 2031 -1.0; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -2.0; 3597 -4.3; 3957 -7.2; 4353 -10.1; 4788 -12.7; 5267 -13.9; 5793 -13.0; 6373 -9.9; 7010 -5.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo with ControlTalk Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo with ControlTalk Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.39 | 7.5 dB   |
| Peaking | 341 Hz   | 0.19 | -7.0 dB  |
| Peaking | 493 Hz   | 1.7  | 6.6 dB   |
| Peaking | 2493 Hz  | 0.48 | 10.2 dB  |
| Peaking | 5040 Hz  | 1.84 | -13.4 dB |
| Peaking | 334 Hz   | 7.13 | -0.5 dB  |
| Peaking | 3050 Hz  | 8.85 | 0.9 dB   |
| Peaking | 6090 Hz  | 6.73 | -2.0 dB  |
| Peaking | 7079 Hz  | 6.26 | 3.2 dB   |
| Peaking | 10689 Hz | 0.73 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Beats%20Solo%20with%20ControlTalk%20Headphones/Monster%20Beats%20Solo%20with%20ControlTalk%20Headphones.png)