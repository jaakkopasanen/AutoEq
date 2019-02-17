# Tascam TH-02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.3; 34 -2.7; 37 -2.9; 41 -3.0; 45 -3.0; 49 -3.1; 54 -3.2; 60 -3.4; 66 -3.8; 72 -4.1; 79 -4.4; 87 -4.7; 96 -5.1; 106 -5.5; 116 -6.0; 128 -6.6; 141 -7.1; 155 -7.4; 170 -7.6; 187 -7.7; 206 -7.6; 227 -7.6; 249 -7.7; 274 -7.8; 302 -7.8; 332 -7.8; 365 -7.4; 402 -6.6; 442 -6.5; 486 -7.1; 535 -7.8; 588 -8.3; 647 -8.6; 712 -8.7; 783 -8.7; 861 -8.2; 947 -6.8; 1042 -6.5; 1146 -6.4; 1261 -6.9; 1387 -7.2; 1526 -7.6; 1678 -7.5; 1846 -6.0; 2031 -3.9; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -8.8; 9330 -8.6; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tascam TH-02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tascam TH-02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.85 | 5.7 dB  |
| Peaking | 59 Hz    | 1.46 | 2.3 dB  |
| Peaking | 1187 Hz  | 0.36 | -3.1 dB |
| Peaking | 3812 Hz  | 0.55 | 8.5 dB  |
| Peaking | 8793 Hz  | 2.43 | -5.9 dB |
| Peaking | 457 Hz   | 2.82 | 2.5 dB  |
| Peaking | 1058 Hz  | 1.57 | 5.9 dB  |
| Peaking | 1174 Hz  | 0.62 | -4.8 dB |
| Peaking | 2399 Hz  | 2.98 | 3.9 dB  |
| Peaking | 13657 Hz | 2.45 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Tascam%20TH-02/Tascam%20TH-02.png)