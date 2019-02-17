# AmazonBasics Lightweight On Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.3; 28 -8.8; 31 -9.1; 34 -9.4; 37 -9.6; 41 -9.7; 45 -9.8; 49 -9.8; 54 -9.8; 60 -9.8; 66 -9.9; 72 -10.0; 79 -10.0; 87 -10.0; 96 -9.6; 106 -9.1; 116 -8.6; 128 -8.0; 141 -7.6; 155 -7.1; 170 -6.5; 187 -5.7; 206 -4.9; 227 -4.1; 249 -3.4; 274 -3.0; 302 -2.9; 332 -3.1; 365 -4.2; 402 -5.4; 442 -6.5; 486 -7.8; 535 -8.7; 588 -9.0; 647 -8.9; 712 -8.4; 783 -7.9; 861 -7.3; 947 -6.7; 1042 -6.3; 1146 -5.9; 1261 -5.2; 1387 -4.6; 1526 -4.0; 1678 -3.6; 1846 -3.0; 2031 -2.5; 2234 -1.6; 2457 -0.8; 2703 -1.4; 2973 -2.3; 3270 -2.9; 3597 -2.1; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -2.7; 6373 -5.9; 7010 -9.5; 7711 -8.6; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AmazonBasics Lightweight On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AmazonBasics Lightweight On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.42 | -3.9 dB |
| Peaking | 296 Hz  | 0.94 | 5.6 dB  |
| Peaking | 567 Hz  | 1.34 | -4.5 dB |
| Peaking | 2362 Hz | 1.26 | 5.1 dB  |
| Peaking | 4594 Hz | 2.93 | 5.7 dB  |
| Peaking | 1435 Hz | 5.29 | 0.5 dB  |
| Peaking | 2058 Hz | 7.11 | -0.8 dB |
| Peaking | 2524 Hz | 1.07 | 0.2 dB  |
| Peaking | 5875 Hz | 4.35 | 2.6 dB  |
| Peaking | 7056 Hz | 4.03 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AmazonBasics%20Lightweight%20On%20Ear/AmazonBasics%20Lightweight%20On%20Ear.png)