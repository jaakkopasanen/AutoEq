# Beyerdynamic T1 sn3964
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.7; 25 -2.1; 28 -2.6; 31 -3.0; 34 -3.2; 37 -3.5; 41 -3.8; 45 -4.1; 49 -4.3; 54 -4.3; 60 -4.0; 66 -4.1; 72 -5.1; 79 -5.7; 87 -6.2; 96 -6.6; 106 -7.0; 116 -7.1; 128 -7.5; 141 -7.7; 155 -7.8; 170 -7.9; 187 -8.0; 206 -8.0; 227 -7.9; 249 -7.8; 274 -7.8; 302 -7.6; 332 -7.4; 365 -7.2; 402 -6.8; 442 -6.6; 486 -6.4; 535 -6.3; 588 -5.8; 647 -5.4; 712 -5.0; 783 -4.9; 861 -5.4; 947 -5.4; 1042 -4.9; 1146 -4.1; 1261 -4.8; 1387 -5.0; 1526 -4.8; 1678 -5.4; 1846 -6.2; 2031 -6.0; 2234 -6.8; 2457 -6.5; 2703 -6.6; 2973 -5.6; 3270 -4.4; 3597 -4.8; 3957 -6.1; 4353 -7.2; 4788 -5.5; 5267 -0.5; 5793 -6.2; 6373 -9.4; 7010 -4.1; 7711 -9.7; 8482 -13.4; 9330 -11.1; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 sn3964 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sn3964 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  1.19 | 5.1 dB  |
| Peaking | 61 Hz    |  3.99 | 2.1 dB  |
| Peaking | 1152 Hz  |  1.36 | 2.1 dB  |
| Peaking | 5242 Hz  | 10.22 | 7.0 dB  |
| Peaking | 8582 Hz  |  5    | -7.7 dB |
| Peaking | 203 Hz   |  0.97 | -1.7 dB |
| Peaking | 686 Hz   |  3.64 | 1.1 dB  |
| Peaking | 3379 Hz  |  1.57 | -1.9 dB |
| Peaking | 3382 Hz  |  4    | 4.2 dB  |
| Peaking | 22050 Hz |  1.75 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sn3964/Beyerdynamic%20T1%20sn3964.png)