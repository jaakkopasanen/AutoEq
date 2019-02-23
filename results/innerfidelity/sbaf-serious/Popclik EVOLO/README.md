# Popclik EVOLO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.7; 25 -12.8; 28 -12.9; 31 -13.1; 34 -13.2; 37 -13.2; 41 -13.2; 45 -13.2; 49 -13.2; 54 -13.3; 60 -13.3; 66 -13.3; 72 -13.3; 79 -13.4; 87 -13.4; 96 -13.4; 106 -13.2; 116 -12.9; 128 -12.8; 141 -12.5; 155 -12.2; 170 -11.7; 187 -11.3; 206 -10.8; 227 -10.2; 249 -9.7; 274 -9.0; 302 -8.4; 332 -7.7; 365 -7.0; 402 -6.3; 442 -5.6; 486 -5.1; 535 -4.5; 588 -3.6; 647 -3.1; 712 -2.8; 783 -2.3; 861 -2.2; 947 -2.1; 1042 -2.5; 1146 -2.7; 1261 -3.1; 1387 -3.8; 1526 -4.8; 1678 -5.9; 1846 -6.4; 2031 -6.6; 2234 -7.0; 2457 -6.9; 2703 -6.7; 2973 -4.8; 3270 -2.2; 3597 -0.5; 3957 -0.8; 4353 -3.0; 4788 -4.6; 5267 -6.4; 5793 -10.3; 6373 -9.3; 7010 -4.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Popclik EVOLO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclik EVOLO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.31 | -6.5 dB |
| Peaking | 137 Hz  |  0.58 | -4.7 dB |
| Peaking | 802 Hz  |  1.15 | 4.6 dB  |
| Peaking | 3774 Hz |  4.01 | 6.3 dB  |
| Peaking | 5957 Hz |  7.7  | -6.1 dB |
| Peaking | 791 Hz  |  5.64 | -0.6 dB |
| Peaking | 1246 Hz |  2.57 | 1.4 dB  |
| Peaking | 2274 Hz |  1.58 | -2.1 dB |
| Peaking | 3288 Hz |  6.39 | 2.0 dB  |
| Peaking | 7139 Hz | 11.45 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclik%20EVOLO/Popclik%20EVOLO.png)