# Tascam TH-02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.7; 25 -3.1; 28 -3.7; 31 -4.1; 34 -4.4; 37 -4.6; 41 -4.7; 45 -4.8; 49 -4.9; 54 -5.0; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.1; 87 -6.4; 96 -6.8; 106 -7.2; 116 -7.7; 128 -8.3; 141 -8.8; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.4; 227 -9.4; 249 -9.5; 274 -9.6; 302 -9.6; 332 -9.7; 365 -9.3; 402 -8.5; 442 -8.4; 486 -9.1; 535 -9.8; 588 -10.3; 647 -10.6; 712 -10.8; 783 -10.7; 861 -10.1; 947 -8.9; 1042 -8.5; 1146 -8.5; 1261 -9.0; 1387 -9.3; 1526 -9.8; 1678 -9.6; 1846 -8.2; 2031 -6.2; 2234 -4.4; 2457 -2.3; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.3; 7711 -8.8; 8482 -10.4; 9330 -8.8; 10263 -8.2; 11289 -7.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tascam TH-02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tascam TH-02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.13 | 3.8 dB  |
| Peaking | 367 Hz  | 0.16 | -4.1 dB |
| Peaking | 1643 Hz | 2.29 | -4.5 dB |
| Peaking | 4013 Hz | 0.51 | 8.6 dB  |
| Peaking | 8667 Hz | 1.99 | -7.9 dB |
| Peaking | 427 Hz  | 4.09 | 1.9 dB  |
| Peaking | 723 Hz  | 3.4  | -1.6 dB |
| Peaking | 2721 Hz | 4.39 | 1.8 dB  |
| Peaking | 5323 Hz | 0.8  | -1.4 dB |
| Peaking | 6127 Hz | 3.4  | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Tascam%20TH-02/Tascam%20TH-02.png)