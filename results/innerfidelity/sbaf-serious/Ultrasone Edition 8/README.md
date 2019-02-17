# Ultrasone Edition 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.5; 54 -1.9; 60 -2.1; 66 -2.4; 72 -2.9; 79 -3.3; 87 -3.3; 96 -3.4; 106 -3.9; 116 -4.3; 128 -4.8; 141 -5.2; 155 -5.2; 170 -5.3; 187 -6.4; 206 -7.0; 227 -6.9; 249 -6.6; 274 -6.1; 302 -6.6; 332 -6.5; 365 -6.3; 402 -6.2; 442 -6.0; 486 -6.1; 535 -5.9; 588 -5.4; 647 -5.2; 712 -5.3; 783 -5.2; 861 -5.6; 947 -6.3; 1042 -6.1; 1146 -5.5; 1261 -5.0; 1387 -4.4; 1526 -4.0; 1678 -3.4; 1846 -1.7; 2031 -0.5; 2234 -0.5; 2457 -3.6; 2703 -5.1; 2973 -3.4; 3270 -1.8; 3597 -3.6; 3957 -4.0; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -6.3; 6373 -10.9; 7010 -8.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.4; 15026 -10.8; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.42 | 6.2 dB   |
| Peaking | 2007 Hz  | 2.12 | 5.7 dB   |
| Peaking | 5346 Hz  | 0.98 | 20.9 dB  |
| Peaking | 6300 Hz  | 1.16 | -28.8 dB |
| Peaking | 7181 Hz  | 1.03 | 7.9 dB   |
| Peaking | 215 Hz   | 3.95 | -1.3 dB  |
| Peaking | 721 Hz   | 1.89 | 1.2 dB   |
| Peaking | 975 Hz   | 5.94 | -0.9 dB  |
| Peaking | 12491 Hz | 2.82 | 2.0 dB   |
| Peaking | 14405 Hz | 4.29 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%208/Ultrasone%20Edition%208.png)