# Beyerdynamic T1 sn3964
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.0; 25 -2.4; 28 -2.9; 31 -3.2; 34 -3.5; 37 -3.8; 41 -4.1; 45 -4.4; 49 -4.6; 54 -4.6; 60 -4.3; 66 -4.4; 72 -5.4; 79 -6.0; 87 -6.5; 96 -6.9; 106 -7.3; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.1; 170 -8.2; 187 -8.3; 206 -8.3; 227 -8.2; 249 -8.1; 274 -8.0; 302 -7.8; 332 -7.6; 365 -7.4; 402 -7.1; 442 -6.9; 486 -6.7; 535 -6.6; 588 -6.1; 647 -5.6; 712 -5.3; 783 -5.2; 861 -5.7; 947 -5.7; 1042 -5.1; 1146 -4.4; 1261 -5.1; 1387 -5.3; 1526 -5.1; 1678 -5.7; 1846 -6.5; 2031 -6.3; 2234 -7.1; 2457 -6.8; 2703 -6.9; 2973 -5.9; 3270 -4.6; 3597 -5.1; 3957 -6.4; 4353 -7.5; 4788 -5.8; 5267 -0.5; 5793 -6.4; 6373 -9.7; 7010 -4.3; 7711 -10.0; 8482 -13.6; 9330 -11.4; 10263 -6.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 sn3964 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sn3964 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 188 Hz  |  0.62 | -3.3 dB |
| Peaking | 2382 Hz |  3.11 | -1.8 dB |
| Peaking | 5240 Hz | 13.14 | 5.8 dB  |
| Peaking | 8538 Hz |  3.87 | -9.0 dB |
| Peaking | 15 Hz   |  0.65 | 4.3 dB  |
| Peaking | 62 Hz   |  4.3  | 1.4 dB  |
| Peaking | 4453 Hz |  4.34 | -3.9 dB |
| Peaking | 5580 Hz |  1.44 | 2.8 dB  |
| Peaking | 6167 Hz |  9.09 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sn3964/Beyerdynamic%20T1%20sn3964.png)