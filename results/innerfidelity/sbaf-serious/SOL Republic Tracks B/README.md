# SOL Republic Tracks B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.9; 25 -8.4; 28 -9.2; 31 -9.9; 34 -10.4; 37 -10.9; 41 -11.3; 45 -11.6; 49 -11.7; 54 -11.9; 60 -11.9; 66 -12.0; 72 -12.1; 79 -11.9; 87 -11.5; 96 -11.6; 106 -11.7; 116 -11.8; 128 -12.0; 141 -12.1; 155 -12.1; 170 -11.5; 187 -11.7; 206 -11.3; 227 -10.5; 249 -9.3; 274 -7.9; 302 -5.4; 332 -3.2; 365 -0.9; 402 -0.5; 442 -0.5; 486 -0.5; 535 -1.4; 588 -3.0; 647 -4.6; 712 -5.9; 783 -6.4; 861 -6.6; 947 -6.4; 1042 -6.3; 1146 -5.5; 1261 -4.8; 1387 -4.3; 1526 -3.3; 1678 -3.1; 1846 -4.4; 2031 -3.9; 2234 -3.1; 2457 -1.7; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -2.7; 5267 -1.7; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SOL Republic Tracks B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SOL Republic Tracks B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 169 Hz  | 0.21 | -6.9 dB |
| Peaking | 427 Hz  | 1.25 | 12.6 dB |
| Peaking | 1510 Hz | 2.85 | 2.7 dB  |
| Peaking | 3192 Hz | 1.28 | 6.6 dB  |
| Peaking | 5959 Hz | 3.97 | 5.0 dB  |
| Peaking | 16 Hz   | 3.01 | 1.2 dB  |
| Peaking | 100 Hz  | 2.83 | 1.0 dB  |
| Peaking | 229 Hz  | 1.73 | -1.0 dB |
| Peaking | 330 Hz  | 4.92 | 1.5 dB  |
| Peaking | 8344 Hz | 3.82 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 7.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SOL%20Republic%20Tracks%20B/SOL%20Republic%20Tracks%20B.png)