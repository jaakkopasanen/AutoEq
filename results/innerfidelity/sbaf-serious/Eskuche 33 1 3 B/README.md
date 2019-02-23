# Eskuche 33 1 3 B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.4; 31 -2.8; 34 -4.1; 37 -5.2; 41 -6.4; 45 -7.3; 49 -7.9; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.0; 79 -9.2; 87 -9.3; 96 -9.5; 106 -9.4; 116 -9.2; 128 -9.3; 141 -9.6; 155 -9.9; 170 -10.0; 187 -10.1; 206 -10.3; 227 -10.4; 249 -10.6; 274 -10.7; 302 -10.7; 332 -10.5; 365 -10.5; 402 -10.7; 442 -10.9; 486 -11.3; 535 -11.6; 588 -11.3; 647 -11.2; 712 -11.1; 783 -10.8; 861 -10.4; 947 -9.1; 1042 -8.2; 1146 -7.4; 1261 -7.1; 1387 -5.7; 1526 -5.4; 1678 -4.9; 1846 -4.5; 2031 -4.3; 2234 -4.1; 2457 -4.4; 2703 -4.4; 2973 -3.5; 3270 -1.9; 3597 -1.8; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -3.8; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eskuche 33 1 3 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eskuche 33 1 3 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.24 | 8.5 dB  |
| Peaking | 107 Hz  | 0.16 | -3.2 dB |
| Peaking | 775 Hz  | 0.66 | -4.3 dB |
| Peaking | 1452 Hz | 0.93 | 3.4 dB  |
| Peaking | 4385 Hz | 1.17 | 5.8 dB  |
| Peaking | 3936 Hz | 2.93 | 0.6 dB  |
| Peaking | 5198 Hz | 6.72 | -4.1 dB |
| Peaking | 6151 Hz | 2.43 | 5.1 dB  |
| Peaking | 7181 Hz | 0.78 | -1.3 dB |
| Peaking | 7626 Hz | 3.18 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Eskuche%2033%201%203%20B/Eskuche%2033%201%203%20B.png)