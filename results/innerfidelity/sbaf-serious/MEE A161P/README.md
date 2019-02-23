# MEE A161P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.5; 45 -4.7; 49 -4.8; 54 -5.0; 60 -5.3; 66 -5.6; 72 -6.0; 79 -6.3; 87 -6.8; 96 -7.2; 106 -7.5; 116 -7.7; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.7; 187 -8.8; 206 -8.9; 227 -8.8; 249 -8.8; 274 -8.7; 302 -8.5; 332 -8.4; 365 -8.1; 402 -7.9; 442 -7.5; 486 -7.3; 535 -7.0; 588 -6.4; 647 -6.1; 712 -5.9; 783 -5.6; 861 -5.8; 947 -6.0; 1042 -6.2; 1146 -6.4; 1261 -6.7; 1387 -7.2; 1526 -7.7; 1678 -8.1; 1846 -8.3; 2031 -8.7; 2234 -9.4; 2457 -9.5; 2703 -8.1; 2973 -3.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -4.1; 5267 -7.3; 5793 -10.1; 6373 -4.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE A161P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE A161P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.49 | 2.7 dB  |
| Peaking | 192 Hz  | 0.78 | -2.7 dB |
| Peaking | 2429 Hz | 2.06 | -5.4 dB |
| Peaking | 3499 Hz | 2.25 | 8.6 dB  |
| Peaking | 794 Hz  | 2.42 | 1.3 dB  |
| Peaking | 1609 Hz | 5.01 | -0.8 dB |
| Peaking | 4305 Hz | 7.13 | 2.4 dB  |
| Peaking | 5648 Hz | 6.12 | -5.7 dB |
| Peaking | 6614 Hz | 7.31 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MEE%20A161P/MEE%20A161P.png)