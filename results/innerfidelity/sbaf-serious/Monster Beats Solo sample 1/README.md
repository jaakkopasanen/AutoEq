# Monster Beats Solo sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.6; 25 -12.8; 28 -13.0; 31 -13.1; 34 -13.2; 37 -13.3; 41 -13.5; 45 -13.5; 49 -13.6; 54 -13.8; 60 -14.0; 66 -14.2; 72 -14.3; 79 -14.3; 87 -14.2; 96 -15.1; 106 -15.9; 116 -15.8; 128 -15.3; 141 -15.7; 155 -16.7; 170 -16.2; 187 -16.6; 206 -16.1; 227 -15.2; 249 -14.1; 274 -12.8; 302 -11.0; 332 -9.3; 365 -7.8; 402 -6.3; 442 -4.7; 486 -3.7; 535 -3.4; 588 -4.0; 647 -5.4; 712 -6.6; 783 -7.2; 861 -7.6; 947 -7.7; 1042 -7.2; 1146 -6.5; 1261 -5.8; 1387 -5.6; 1526 -5.5; 1678 -5.3; 1846 -5.2; 2031 -4.6; 2234 -4.6; 2457 -4.1; 2703 -3.8; 2973 -3.1; 3270 -3.3; 3597 -3.1; 3957 -3.7; 4353 -5.2; 4788 -5.5; 5267 -3.1; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Solo sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Solo sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.47 | -6.9 dB |
| Peaking | 112 Hz  | 1.32 | -5.6 dB |
| Peaking | 180 Hz  | 2.36 | -6.4 dB |
| Peaking | 245 Hz  | 3.19 | -4.9 dB |
| Peaking | 4183 Hz | 0.63 | 3.2 dB  |
| Peaking | 519 Hz  | 2.95 | 4.1 dB  |
| Peaking | 898 Hz  | 2.54 | -1.9 dB |
| Peaking | 4756 Hz | 3.22 | -5.9 dB |
| Peaking | 6151 Hz | 1.48 | 8.8 dB  |
| Peaking | 7422 Hz | 1.4  | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Solo%20sample%201/Monster%20Beats%20Solo%20sample%201.png)