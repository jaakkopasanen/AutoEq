# AmazonBasics Lightweight On Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.7; 25 -10.0; 28 -10.4; 31 -10.8; 34 -11.1; 37 -11.3; 41 -11.4; 45 -11.5; 49 -11.5; 54 -11.4; 60 -11.4; 66 -11.5; 72 -11.7; 79 -11.7; 87 -11.6; 96 -11.3; 106 -10.8; 116 -10.3; 128 -9.7; 141 -9.2; 155 -8.8; 170 -8.1; 187 -7.4; 206 -6.6; 227 -5.8; 249 -5.1; 274 -4.7; 302 -4.6; 332 -4.8; 365 -5.9; 402 -7.0; 442 -8.2; 486 -9.4; 535 -10.3; 588 -10.7; 647 -10.6; 712 -10.1; 783 -9.6; 861 -8.9; 947 -8.4; 1042 -8.0; 1146 -7.6; 1261 -6.9; 1387 -6.2; 1526 -5.7; 1678 -5.3; 1846 -4.7; 2031 -4.2; 2234 -3.3; 2457 -2.5; 2703 -3.0; 2973 -4.0; 3270 -4.6; 3597 -3.8; 3957 -2.5; 4353 -0.6; 4788 -0.5; 5267 -2.7; 5793 -4.3; 6373 -7.6; 7010 -11.2; 7711 -10.3; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.7; 20000 -6.5
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
| Peaking | 56 Hz   | 0.62 | -5.8 dB |
| Peaking | 657 Hz  | 2.05 | -4.5 dB |
| Peaking | 2383 Hz | 2.32 | 3.6 dB  |
| Peaking | 4693 Hz | 2.4  | 6.6 dB  |
| Peaking | 7181 Hz | 3.85 | -6.3 dB |
| Peaking | 23 Hz   | 0.91 | -0.9 dB |
| Peaking | 57 Hz   | 1.41 | 2.3 dB  |
| Peaking | 92 Hz   | 0.64 | -1.7 dB |
| Peaking | 287 Hz  | 1.48 | 3.4 dB  |
| Peaking | 489 Hz  | 3.19 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AmazonBasics%20Lightweight%20On%20Ear/AmazonBasics%20Lightweight%20On%20Ear.png)