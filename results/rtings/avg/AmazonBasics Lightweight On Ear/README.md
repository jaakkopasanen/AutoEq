# AmazonBasics Lightweight On Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.5; 25 -9.8; 28 -10.2; 31 -10.6; 34 -10.9; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.4; 72 -11.4; 79 -11.5; 87 -11.4; 96 -11.1; 106 -10.6; 116 -10.0; 128 -9.5; 141 -9.0; 155 -8.6; 170 -7.9; 187 -7.2; 206 -6.5; 227 -5.8; 249 -5.0; 274 -4.6; 302 -4.5; 332 -4.8; 365 -5.9; 402 -7.0; 442 -8.2; 486 -9.5; 535 -10.4; 588 -10.8; 647 -10.7; 712 -10.2; 783 -9.7; 861 -9.0; 947 -8.5; 1042 -8.2; 1146 -7.7; 1261 -7.1; 1387 -6.4; 1526 -5.9; 1678 -5.5; 1846 -5.0; 2031 -4.7; 2234 -4.1; 2457 -3.5; 2703 -3.6; 2973 -4.1; 3270 -4.3; 3597 -3.6; 3957 -2.1; 4353 -0.5; 4788 -0.5; 5267 -2.8; 5793 -4.5; 6373 -6.8; 7010 -11.3; 7711 -10.9; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AmazonBasics Lightweight On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AmazonBasics Lightweight On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.64 | -5.6 dB |
| Peaking | 663 Hz  | 1.99 | -4.6 dB |
| Peaking | 2391 Hz | 2.11 | 2.6 dB  |
| Peaking | 4623 Hz | 2.25 | 6.5 dB  |
| Peaking | 7270 Hz | 4.29 | -6.8 dB |
| Peaking | 24 Hz   | 2.22 | -0.8 dB |
| Peaking | 112 Hz  | 2.06 | -1.1 dB |
| Peaking | 247 Hz  | 2.73 | 1.7 dB  |
| Peaking | 317 Hz  | 2.77 | 2.4 dB  |
| Peaking | 500 Hz  | 4.19 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AmazonBasics%20Lightweight%20On%20Ear/AmazonBasics%20Lightweight%20On%20Ear.png)