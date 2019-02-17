# MEE A161P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.2; 25 -4.3; 28 -4.4; 31 -4.4; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.7; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.6; 106 -7.8; 116 -8.1; 128 -8.4; 141 -8.8; 155 -9.0; 170 -9.0; 187 -9.2; 206 -9.2; 227 -9.2; 249 -9.2; 274 -9.1; 302 -8.9; 332 -8.7; 365 -8.5; 402 -8.3; 442 -7.9; 486 -7.7; 535 -7.3; 588 -6.7; 647 -6.4; 712 -6.3; 783 -5.9; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.5; 1526 -8.1; 1678 -8.5; 1846 -8.7; 2031 -9.0; 2234 -9.7; 2457 -9.9; 2703 -8.5; 2973 -3.9; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -4.5; 5267 -7.7; 5793 -10.4; 6373 -4.8; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE A161P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE A161P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.49 | 2.4 dB   |
| Peaking | 194 Hz  | 0.69 | -3.1 dB  |
| Peaking | 2543 Hz | 1.5  | -10.9 dB |
| Peaking | 3337 Hz | 1.27 | 12.4 dB  |
| Peaking | 5591 Hz | 6.69 | -7.3 dB  |
| Peaking | 784 Hz  | 2.85 | 1.1 dB   |
| Peaking | 1577 Hz | 4.91 | -0.8 dB  |
| Peaking | 6329 Hz | 6.3  | -1.4 dB  |
| Peaking | 6753 Hz | 6.2  | 3.7 dB   |
| Peaking | 8270 Hz | 1.93 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MEE%20A161P/MEE%20A161P.png)