# Read Heath Audio MA600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.5; 25 -12.6; 28 -12.7; 31 -12.8; 34 -12.9; 37 -13.0; 41 -13.0; 45 -13.2; 49 -13.3; 54 -13.4; 60 -13.6; 66 -13.8; 72 -14.0; 79 -14.2; 87 -14.4; 96 -14.6; 106 -14.6; 116 -14.5; 128 -14.5; 141 -14.4; 155 -14.2; 170 -14.0; 187 -13.6; 206 -13.2; 227 -12.6; 249 -12.1; 274 -11.6; 302 -10.9; 332 -10.3; 365 -9.5; 402 -8.8; 442 -7.8; 486 -7.2; 535 -6.3; 588 -5.3; 647 -4.5; 712 -3.8; 783 -3.0; 861 -2.5; 947 -2.1; 1042 -1.9; 1146 -1.5; 1261 -1.2; 1387 -1.4; 1526 -0.5; 1678 -0.5; 1846 -1.1; 2031 -2.4; 2234 -3.2; 2457 -2.7; 2703 -2.6; 2973 -2.9; 3270 -3.8; 3597 -5.3; 3957 -7.1; 4353 -10.5; 4788 -13.7; 5267 -11.5; 5793 -5.6; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -11.1; 16529 -9.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read Heath Audio MA600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Audio MA600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.45 | -4.4 dB  |
| Peaking | 159 Hz   | 0.28 | -8.5 dB  |
| Peaking | 1130 Hz  | 0.34 | 6.8 dB   |
| Peaking | 4708 Hz  | 4.59 | -10.4 dB |
| Peaking | 1638 Hz  | 7.73 | 0.8 dB   |
| Peaking | 5276 Hz  | 7.93 | -3.5 dB  |
| Peaking | 6444 Hz  | 4.22 | 5.9 dB   |
| Peaking | 7536 Hz  | 2.49 | -1.5 dB  |
| Peaking | 15365 Hz | 2.94 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Audio%20MA600/Read%20Heath%20Audio%20MA600.png)