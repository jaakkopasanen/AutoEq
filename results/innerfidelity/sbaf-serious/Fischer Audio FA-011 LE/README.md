# Fischer Audio FA-011 LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.5; 28 -3.7; 31 -4.8; 34 -5.7; 37 -6.4; 41 -7.2; 45 -7.8; 49 -8.2; 54 -8.5; 60 -8.8; 66 -9.0; 72 -9.0; 79 -9.2; 87 -9.3; 96 -9.4; 106 -9.4; 116 -9.3; 128 -9.3; 141 -9.2; 155 -9.1; 170 -9.1; 187 -8.6; 206 -8.9; 227 -8.8; 249 -8.8; 274 -8.5; 302 -8.6; 332 -8.7; 365 -8.7; 402 -8.7; 442 -8.6; 486 -8.6; 535 -8.7; 588 -8.3; 647 -7.6; 712 -7.0; 783 -6.9; 861 -7.3; 947 -7.1; 1042 -6.5; 1146 -5.8; 1261 -4.9; 1387 -4.5; 1526 -4.4; 1678 -4.1; 1846 -3.3; 2031 -2.4; 2234 -1.6; 2457 -1.1; 2703 -0.8; 2973 -0.8; 3270 -0.8; 3597 -0.8; 3957 -0.9; 4353 -1.5; 4788 -0.8; 5267 -1.5; 5793 -1.6; 6373 -2.3; 7010 -4.3; 7711 -6.5; 8482 -6.8; 9330 -6.8; 10263 -6.8; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -6.8; 18182 -6.8; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-011 LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-011 LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.02 | 7.6 dB  |
| Peaking | 48 Hz   | 0.99 | -1.4 dB |
| Peaking | 107 Hz  | 0.56 | -2.3 dB |
| Peaking | 477 Hz  | 0.78 | -1.7 dB |
| Peaking | 3306 Hz | 0.7  | 6.6 dB  |
| Peaking | 959 Hz  | 5.53 | -0.9 dB |
| Peaking | 2411 Hz | 0.42 | 0.3 dB  |
| Peaking | 3487 Hz | 2.48 | -0.9 dB |
| Peaking | 6336 Hz | 2    | 4.3 dB  |
| Peaking | 7506 Hz | 1.43 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20FA-011%20LE/Fischer%20Audio%20FA-011%20LE.png)